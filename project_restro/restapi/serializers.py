from rest_framework import serializers
from app_restro.models import Category, Menu

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "category_name", )
        model = Category

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "menu_title", "category_id", "menu_desc", "menu_price", "menu_ingredient")
        model = Menu