from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from domain.serializers import RequestsCatcherSerializer

# Create your views here.


class RequestsCatcherView(generics.GenericAPIView):
    serializer_class = RequestsCatcherSerializer

    def get(self, request, *args, **kwargs):
        headers = request.headers
        print(kwargs)
        print(headers)
        path = kwargs.pop("path", "/")
        print(path)
        print("GET HOOOMEEE")
        return Response({"message": "GET HOMEE"})
