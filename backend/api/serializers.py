from rest_framework import serializers
from .models import Article, Category
from drf_dynamic_fields import DynamicFieldsMixin


class ArticleSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    def get_author(self, obj):
        return {
            "username": obj.author.username,
            "first_name": obj.author.first_name,
            "last_name": obj.author.last_name,
        }

    def get_category(self, obj):
        return {
            "title": obj.category.title,
        }

    author = serializers.SerializerMethodField("get_author")
    category = serializers.SerializerMethodField("get_category")

    class Meta:
        model = Article
        fields = '__all__'


class CategorySerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
