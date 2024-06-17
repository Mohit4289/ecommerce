from rest_framework import serializers
from .models import *


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]

class BrandSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        
class ProductSerializers(serializers.ModelSerializer):
    brand = BrandSerializers()
    category = CategorySerializers()
    class Meta:
        model = Category
        fields = "__all__"
