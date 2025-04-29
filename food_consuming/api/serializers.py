from django.contrib.auth.models import User
from food_consuming.models import Food, Consume
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['name', 'carbs', 'proteins', 'fats', 'calories',]


class ConsumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consume
        fields = ['food_consumed', 'user']
