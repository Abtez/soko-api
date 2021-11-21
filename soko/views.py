from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from .serializers import ProductSerializer
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



# @csrf_exempt
# def product_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         items = Product.objects.all()
#         serializer = ProductSerializer(items, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         # data = JSONParser().parse(request)
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
    
# @csrf_exempt
# def product_detail(request, uuid):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         items = Product.objects.get(uuid=uuid)
#     except Product.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = ProductSerializer(items)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = ProductSerializer(items, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         items.delete()
#         return HttpResponse(status=204)