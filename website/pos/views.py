from django.contrib.auth.models import User
from django.utils import timezone
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

        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        if start_date and end_date:
            start_date = timezone.datetime.strptime(start_date, "%Y-%m-%d")
            end_date = timezone.datetime.strptime(end_date, "%Y-%m-%d")
            start_date = timezone.make_aware(timezone.datetime(year=start_date.year, month=start_date.month,
                                                               day=1, hour=0, minute=0, second=0))  # represents 00:00:00 of start date
            end_date = timezone.make_aware(timezone.datetime(year=end_date.year, month=end_date.month,
                                                             day=end_date.day, hour=23, minute=59, second=59))  # represents 23:59:59 of end date

            order_products = OrderProduct.objects.filter(
                order__seller=user, order__created_at__gte=start_date, order__created_at__lte=end_date)
        else:
            order_products = OrderProduct.objects.filter(order__seller=user)

        commissions = 0.0
        for order_product in order_products:
            commissions += order_product.commission * \
                order_product.quantity * order_product.product.price

        return Response(round(commissions, 2))


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
                                         day=1, hour=0, minute=0, second=0))  # represents 00:00:00 of start date
        end_date = timezone.make_aware(timezone.datetime(year=timezone_now.year, month=timezone_now.month,
                                       day=timezone_now.day, hour=12, minute=00, second=00))  # represents 12:00:00 of end date

        product_commission = serializer.validated_data['product'].commission
        max_commission = 0.05 if timezone_now >= start_date and timezone_now <= end_date else 0.04

        if product_commission > max_commission:
            product_commission = max_commission

        serializer.save(commission=product_commission)
