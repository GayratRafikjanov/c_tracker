from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from food_consuming.api import views as api_views      # api/views.py

router = DefaultRouter()

router.register(r'users', api_views.UserViewSet)
router.register(r'foods', api_views.FoodViewSet)
router.register(r'consumes', api_views.ConsumeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]