from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from .serializers import *
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *

def index(request):
    return render(request, 'index.html')

class AllProductsViews(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    
    def get(self, request, uuid=None):
        if uuid:
            item = Product.objects.get(uuid=uuid)
            serializer = ProductSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Product.objects.all()
        serializer = ProductSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)   

    def patch(self, request, uuid=None):
        item = Product.objects.get(uuid=uuid)
        serializer = ProductSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})


    def delete(self, request, uuid=None):
        item = get_object_or_404(Product, uuid=uuid)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})
    
class VendorProfileViews(APIView):
    def post(self, request):
        serializer = VendorProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    
    def get(self, request, user=None):
        if user:
            user = VendorProfile.objects.get(user=user)
            serializer = VendorProfileSerializer(user)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        users = VendorProfile.objects.all()
        serializer = VendorProfileSerializer(users, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)   

    def patch(self, request, user=None):
        user = VendorProfile.objects.get(user=user)
        serializer = VendorProfileSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})


    def delete(self, request, user=None):
        user = get_object_or_404(VendorProfile, user=user)
        user.delete()
        return Response({"status": "success", "user": "Item Deleted"})

class UserViews(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    
    def get(self, request, id=None):
        if id:
            user = User.objects.get(id=id)
            serializer = UserSerializer(user)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)   

    def patch(self, request, id=None):
        user = User.objects.get(id=id)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})


    def delete(self, request, id=None):
        user = get_object_or_404(User, id=id)
        user.delete()
        return Response({"status": "success", "user": "Item Deleted"})


