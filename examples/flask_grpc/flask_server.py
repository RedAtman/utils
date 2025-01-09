import grpc
import service_pb2
import service_pb2_grpc
from flask import Flask, jsonify, request

app = Flask(__name__)


def get_grpc_client():
    channel = grpc.insecure_channel("localhost:50051")
    stub = service_pb2_grpc.DemoServiceStub(channel)
    return stub


@app.route("/hello", methods=["POST"])
def say_hello():
    data = request.json
    name = data.get("name")
    stub = get_grpc_client()
    response = stub.SayHello(service_pb2.HelloRequest(name=name))
    return jsonify({"message": response.message})


if __name__ == "__main__":
    app.run(port=5000, debug=True)
