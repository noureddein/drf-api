from rest_framework import serializers
from products.models import Products


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'description',
                  'image_link', "timestamp", "user")
        model = Products
