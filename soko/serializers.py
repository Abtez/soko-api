from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password


class ProductSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=200)
    class Meta:
        model = Product
        fields = '__all__'
        
class VendorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorProfile
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    profile = VendorProfileSerializer()
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).create(validated_data)

    class Meta:
        model = User
        optional_fields = ['profile']
        fields = ('first_name', 'last_name', 'email', 'password', 'profile')
        extra_kwargs = {"profile": {"required": False, "allow_null": True}}
        
class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'