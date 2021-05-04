from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.EndPointsAPI.as_view(), name="endpoints"),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]