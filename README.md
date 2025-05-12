# ca-grpc-provider
Cluster Autoscaler provider that uses gRPC and Protobufs as an API interface

Generate python API from the provider protobuf:
```bash
mkdir generated
python -m grpc_tools.protoc \
  -I=protos \
  --python_out=generated \
  --grpc_python_out=generated \
  $(find protos -name "*.proto")
```
