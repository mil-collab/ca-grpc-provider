from grpc_reflection.v1alpha import reflection
import grpc
from concurrent import futures

import externalgrpc_pb2 as ext_pb2
import externalgrpc_pb2_grpc as ext_grpc

class CloudProvider(ext_grpc.CloudProviderServicer):
    def NodeGroups(self, request, context):
        return ext_pb2.NodeGroupsResponse(nodeGroups=[
            ext_pb2.NodeGroup(id="ng-1", minSize=1, maxSize=5, debug="hello"),
            ext_pb2.NodeGroup(id="ng-2", minSize=1, maxSize=3, debug="hi")
        ])

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ext_grpc.add_CloudProviderServicer_to_server(CloudProvider(), server)

    SERVICE_NAMES = (
        ext_pb2.DESCRIPTOR.services_by_name['CloudProvider'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC server with reflection is running on port 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
