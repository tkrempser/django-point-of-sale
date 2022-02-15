from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Sum
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from pos.models import Customer, OrderProduct, Product, Order
from pos.serializers import UserSerializer, CustomerSerializer, ProductSerializer, OrderSerializer, OrderProductSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True)
    def commissions(self, request, pk):
        user = self.get_object()
        commissions = OrderProduct.objects.filter(
            order__seller=user).aggregate(Sum('commission'))

        return Response(commissions['commission__sum'])


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderProductViewSet(viewsets.ModelViewSet):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer

    def perform_create(self, serializer):
        timezone_now = timezone.localtime(timezone.now())
        start_date = timezone.make_aware(timezone.datetime(year=timezone_now.year, month=timezone_now.month,
                                         day=1, hour=0, minute=0, second=0))  # represents 00:00:00
        end_date = timezone.make_aware(timezone.datetime(year=timezone_now.year, month=timezone_now.month,
                                       day=timezone_now.day, hour=12, minute=00, second=00))  # represents 12:00:00

        product_commission = serializer.validated_data['product'].commission
        max_commission = 0.05 if timezone_now >= start_date and timezone_now <= end_date else 0.04

        if product_commission > max_commission:
            product_commission = max_commission

        serializer.save(commission=product_commission)
