from rest_framework import serializers
from .models import Category

# name 과 kind 가 JSON 으로 어떻게 표현하는지 설명
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "name",
            "kind",
        )