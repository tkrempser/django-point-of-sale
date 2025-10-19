from django.contrib.auth.models import User
from rest_framework import serializers

from pos.models import Customer, Product, Order, OrderProduct


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'first_name', 'last_name', 'email']


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ['url', 'first_name', 'last_name', 'email']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['url', 'name', 'price']


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.HyperlinkedRelatedField(
        many=True, view_name='product-detail', read_only=True)

    class Meta:
        model = Order
        fields = ['url', 'created_at', 'customer', 'seller', 'products']


class OrderProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ['url', 'order', 'product', 'quantity']
