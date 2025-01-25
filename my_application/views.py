from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class Test_API(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        return Response(
                {
                    'status_code': status.HTTP_200_OK,
                    'data': data
                },
                status=status.HTTP_200_OK
            )

    def get(self, request, *args, **kwargs):
        return Response(
                {
                    'status_code': status.HTTP_200_OK,
                    'data':'API is working fine!'
                },
                status=status.HTTP_200_OK
            )