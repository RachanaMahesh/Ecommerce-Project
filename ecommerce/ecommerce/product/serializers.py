from rest_framework import serializers
from .models import Category,Brand,Product

class CatergorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # fields = "__all__"
        fields = ["id","name"]

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    category = CatergorySerializer()
    class Meta:
        model = Product
        fields = "__all__"