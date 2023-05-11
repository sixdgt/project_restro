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
        data = request.data
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryApiIdView(APIView):
    def get_object(self, id):
        try:
            data = Category.objects.get(id=id)
            return data
        except Category.DoesNotExist: 
            return None
    
    def get(self, request, id):
        data = self.get_object(id)
        if not data:
            return Response({"msg": "Data not found"}, status=status.HTTP_404_NOT_FOUND)    
        serializer = CategorySerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, id):
        data = self.get_object(id)
        if not data:
            return Response({"msg": "Data not found"}, status=status.HTTP_404_NOT_FOUND) 
        
        data.delete()
        return Response({"msg": "Deleted successfully"}, status=status.HTTP_200_OK)

    def put(self, request, id):
        instance = self.get_object(id)
        if not instance:
            return Response({"msg": "Data not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CategorySerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MenuApiView(APIView):
    def get(self, request):
        menus = Menu.objects.all()
        if not Menu.DoesNotExist:
            return Response({"message": "Data not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = MenuSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MenuApiIdView(APIView):
    def get_object(self, id):
        try:
            data = Menu.objects.get(id=id)
            return data
        except Menu.DoesNotExist:
            return None
    
    def get(self, request, id):
        menu_obj = self.get_object(id)
        if not menu_obj:
            return Response({"msg": "Data not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = MenuSerializer(menu_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        menu_obj = self.get_object(id)
        if not menu_obj:
            return Response({"msg": "Data not found"}, status=status.HTTP_404_NOT_FOUND)

        menu_obj.delete()
        return Response({"msg": "Deleted successfully"}, status=status.HTTP_200_OK)

    def put(self, request, id):
        menu_obj = self.get_object(id)
        if not menu_obj:
            return Response({"msg": "Data not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MenuSerializer(instance=menu_obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    