from django.contrib.auth.models import User, Group
from food_consuming.models import Food, Consume
from food_consuming.api.serializers import UserSerializer, FoodSerializer, ConsumeSerializer
from rest_framework import viewsets, permissions


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [permissions.IsAuthenticated]

class ConsumeViewSet(viewsets.ModelViewSet):
    queryset = Consume.objects.all()
    serializer_class = ConsumeSerializer
    permission_classes = [permissions.IsAuthenticated]
