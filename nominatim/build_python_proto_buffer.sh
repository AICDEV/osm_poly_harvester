python -m grpc_tools.protoc -I ../proto --python_out=. osm.proto --grpc_python_out=. -I ../proto -I .
