from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status


class EndPointsAPI(APIView):
    """
        Showing all the endpoinsts in project
    """

    def get(self, request):
        endpoints = [
            '127.0.0.1:8000/api/',
        ]
        return Response(endpoints, status=status.HTTP_200_OK)
