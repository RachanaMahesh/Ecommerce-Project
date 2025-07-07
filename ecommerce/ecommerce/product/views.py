from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Category,Brand, Product
from .serializers import CatergorySerializer,BrandSerializer, ProductSerializer

from drf_spectacular.utils import extend_schema,OpenApiResponse, OpenApiParameter

class CategoryView(viewsets.ViewSet):
    """
    A Simple Viewsets to view category
    """

    queryset = Category.objects.all()

    @extend_schema(responses= CatergorySerializer)
    def list(self,request):
        serializer = CatergorySerializer(self.queryset, many=True)
        return Response(serializer.data)

    
    # GET /api/greet/?name=John
    # class GreetView(APIView):
    #   def get(self, request):
    #     name = request.GET.get('name', 'Guest')
    #     return Response({'message': f'Hello, {name}!'})

    # class GreetView(APIView):

    # @extend_schema(
    #     parameters=[
    #         OpenApiParameter(
    #             name='name',
    #             type=str,
    #             location=OpenApiParameter.QUERY,
    #             description='Name of the person to greet',
    #             required=False
    #         ),
    #     ],
    #     responses={200: {'type': 'object', 'properties': {'message': {'type': 'string'}}}},
    # )
    # def get(self, request):
    #     name = request.GET.get('name', 'Guest')
    #     return Response({'message': f'Hello, {name}!'})
    # @extend_schema(
    #     summary= "Say hello",
    #     description= "returns a greeting message.",
    #     responses= {200: OpenApiResponse(description="A greeting.")}

    # )
    # def list(self,request):
    #     serializer = CatergorySerializer(self.queryset, many=True)
    #     return Response(serializer.data)