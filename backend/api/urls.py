from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'articles_list', views.ArticleViewSet, basename='articles_list')
router.register(r'category_list', views.CategoryViewSet, basename="category_list")



urlpatterns = [
    path('', views.EndPointsAPI.as_view(), name="endpoints"),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    path('', include(router.urls)),
] 