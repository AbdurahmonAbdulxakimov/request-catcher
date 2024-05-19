from rest_framework import generics
from rest_framework.response import Response

from domain.serializers import RequestsCatcherSerializer
from domain.utils import send_info


class RequestsCatcherView(generics.GenericAPIView):
    serializer_class = RequestsCatcherSerializer

    @send_info
    def get(self, request, *args, **kwargs):
        return Response({"message": "GET request"})

    @send_info
    def post(self, request, *args, **kwargs):
        return Response({"message": "POST request"})

    @send_info
    def put(self, request, *args, **kwargs):
        return Response({"message": "PUT request"})

    @send_info
    def patch(self, request, *args, **kwargs):
        return Response({"message": "PATCH request"})

    @send_info
    def delete(self, request, *args, **kwargs):
        return Response({"message": "DELETE request"})

    @send_info
    def head(self, request, *args, **kwargs):
        return Response({"message": "HEAD request"})

    @send_info
    def options(self, request, *args, **kwargs):
        return Response({"message": "OPTIONS request"})
