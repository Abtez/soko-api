from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=200)
    class Meta:
        model = Product
        fields = '__all__'