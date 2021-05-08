from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status
# permission
from rest_framework.permissions import IsAuthenticated
from .serializers import ArticleSerializer, CategorySerializer
from .models import Article, Category


class EndPointsAPI(APIView):
    """
        Showing all the endpoinsts in project
    """

    def get(self, request):
        endpoints = [
            '127.0.0.1:8000/api/',
            '127.0.0.1:8000/api/article_list',
        ]
        return Response(endpoints, status=status.HTTP_200_OK)


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated,]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated,]