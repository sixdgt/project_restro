from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.request import Request
from app_restro.models import Category, Menu
from .serializers import CategorySerializer, MenuSerializer

# Create your views here.
class CategoryApiView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        if not Category.DoesNotExist:
            return Response({"message": "Data not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        pass