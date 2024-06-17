from http.client import responses
from itertools import product
from pickle import TRUE
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .models import *
from .serializers import CategorySerializers,BrandSerializers,ProductSerializers
from drf_spectacular.utils import extend_schema

class CategoryView(viewsets.ViewSet):

    queryset = Category.objects.all()
    
    @extend_schema(responses=CategorySerializers)
    def list(self,request):
        serializer = BrandSerializers(self.queryset, many=TRUE)
        return Response(serializer.data)

class BrandView(viewsets.ViewSet):

    queryset = Brand.objects.all()
    print(queryset)
    
    @extend_schema(responses=BrandSerializers)
    def list(self,request):
        serializer = BrandSerializers(self.queryset, many=TRUE)
        return Response(serializer.data)

class ProductView(viewsets.ViewSet):

    queryset = Product.objects.all()
    print(queryset)
    
    @extend_schema(responses=ProductSerializers)
    def list(self,request):
        serializer = ProductSerializers(self.queryset, many=TRUE)
        return Response(serializer.data)

