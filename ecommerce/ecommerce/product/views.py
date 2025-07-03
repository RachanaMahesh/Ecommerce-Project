from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Category,Brand, Product
from .serializers import CatergorySerializer,BrandSerializer, ProductSerializer

class CategoryView(viewsets.ViewSet):
    """
    A Simple Viewsets to view category
    """

    queryset = Category.objects.all()

    def list(self,request):
        serializer = CatergorySerializer(self.queryset, many=True)
        return Response(serializer.data)