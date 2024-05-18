from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from domain.serializers import RequestsCatcherSerializer
from domain.utils import sendInfo


class RequestsCatcherView(generics.GenericAPIView):
    serializer_class = RequestsCatcherSerializer

    def get(self, request, *args, **kwargs):
        domain = request.META.get("HTTP_HOST").split(".")[0]
        method = request.method
        headers = request.headers
        path = kwargs.pop("path", "/")

        data = {"method": method, "headers": dict(headers), "path": path}

        sendInfo(domain, data)
        return Response({"message": "GET request"})

    # def post(self, request, *args, **kwargs):
    #     headers = request.headers
    #     path = kwargs.pop("path", "/")

    #     data = {"headers": dict(headers), "path": path, "data": dict(request.data)}

    #     sendInfo(data)
    #     return Response({"message": "POST request"})

    # def put(self, request, *args, **kwargs):
    #     print("PUT request")
    #     return Response({"message": "PUT request"})

    # def patch(self, request, *args, **kwargs):
    #     print("PATCH request")
    #     return Response({"message": "PATCH request"})

    # def delete(self, request, *args, **kwargs):
    #     print("DELETE request")
    #     return Response({"message": "DELETE request"})

    # def head(self, request, *args, **kwargs):
    #     print("HEAD request")
    #     return Response({"message": "HEAD request"})

    # def options(self, request, *args, **kwargs):
    #     print("OPTIONS request")
    #     return Response({"message": "OPTIONS request"})
