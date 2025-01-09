import logging
from concurrent import futures

import grpc
import service_pb2
import service_pb2_grpc

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class DemoService(service_pb2_grpc.DemoServiceServicer):
    def SayHello(self, request, context):
        logger.info(f"Received request: {request.name}")
        return service_pb2.HelloResponse(message=f"Hello, {request.name}!")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_DemoServiceServicer_to_server(DemoService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("gRPC server started on port 50051")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
