import factory
import json
import pytest

from django.urls import reverse
from django_mock_queries.mocks import MockSet
from django.contrib.auth.models import User

from pos.views import CustomerViewSet, ProductViewSet, UserViewSet, OrderViewSet
from pos.models import Customer, Product, Order
from pos.tests.factories import CustomerFactory, ProductFactory, UserFactory, OrderFactory


@pytest.mark.django_db
class TestCustomerViewSet:
    def test_list(self, mocker, rf):
        url = reverse('customer-list')
        request = rf.get(url)
        qs = MockSet(
            CustomerFactory.build(),
            CustomerFactory.build(),
            CustomerFactory.build(),
        )
        view = CustomerViewSet.as_view(
            {'get': 'list'}
        )

        mocker.patch.object(
            CustomerViewSet, 'get_queryset', return_value=qs
        )

        response = view(request).render()

        assert response.status_code == 200
        assert json.loads(response.content)

    def test_create(self, mocker, rf):
        valid_data_dict = factory.build(
            dict,
            FACTORY_CLASS=CustomerFactory
        )
        valid_data_dict['url'] = None
        url = reverse('customer-list')
        request = rf.post(
            url,
            content_type='application/json',
            data=json.dumps(valid_data_dict)
        )
        mocker.patch.object(
            Customer, 'save'
        )
        view = CustomerViewSet.as_view(
            {'post': 'create'}
        )

        response = view(request).render()

        assert response.status_code == 201
        assert json.loads(response.content) == valid_data_dict

    def test_update(self, mocker, rf):
        old_customer = CustomerFactory.build()
        new_customer = CustomerFactory.build()
        customer_dict = {
            'url': None,
            'first_name': new_customer.first_name,
            'last_name': new_customer.last_name,
            'email': new_customer.email
        }
        url = reverse('customer-detail', kwargs={'pk': old_customer.id})
        request = rf.put(
            url,
            content_type='application/json',
            data=json.dumps(customer_dict)
        )
        mocker.patch.object(
            CustomerViewSet, 'get_object', return_value=old_customer
        )
        mocker.patch.object(
            Customer, 'save'
        )
        view = CustomerViewSet.as_view(
            {'put': 'update'}
        )

        response = view(request, pk=old_customer.id).render()

        assert response.status_code == 200
        assert json.loads(response.content) == customer_dict

    def test_delete(self, mocker, rf):
        customer = CustomerFactory.build()
        url = reverse('customer-detail', kwargs={'pk': customer.id})
        request = rf.delete(url)
        mocker.patch.object(
            CustomerViewSet, 'get_object', return_value=customer
        )
        del_mock = mocker.patch.object(
            Customer, 'delete'
        )
        view = CustomerViewSet.as_view(
            {'delete': 'destroy'}
        )

        response = view(request).render()

        assert response.status_code == 204
        assert del_mock.assert_called


@pytest.mark.django_db
class TestProductViewSet:
    def test_list(self, mocker, rf):
        url = reverse('product-list')
        request = rf.get(url)
        qs = MockSet(
            ProductFactory.build(),
            ProductFactory.build(),
            ProductFactory.build(),
        )
        view = ProductViewSet.as_view(
            {'get': 'list'}
        )

        mocker.patch.object(
            ProductViewSet, 'get_queryset', return_value=qs
        )

        response = view(request).render()

        assert response.status_code == 200
        assert json.loads(response.content)

    def test_create(self, mocker, rf):
        valid_data_dict = factory.build(
            dict,
            FACTORY_CLASS=ProductFactory
        )
        valid_data_dict['url'] = None
        url = reverse('product-list')
        request = rf.post(
            url,
            content_type='application/json',
            data=json.dumps(valid_data_dict)
        )
        mocker.patch.object(
            Product, 'save'
        )
        view = ProductViewSet.as_view(
            {'post': 'create'}
        )

        response = view(request).render()

        assert response.status_code == 201
        assert json.loads(response.content) == valid_data_dict

    def test_update(self, mocker, rf):
        old_product = ProductFactory.build()
        new_product = ProductFactory.build()
        product_dict = {
            'url': None,
            'name': new_product.name,
            'price': new_product.price,
            'commission': new_product.commission
        }
        url = reverse('product-detail', kwargs={'pk': old_product.id})
        request = rf.put(
            url,
            content_type='application/json',
            data=json.dumps(product_dict)
        )
        mocker.patch.object(
            ProductViewSet, 'get_object', return_value=old_product
        )
        mocker.patch.object(
            Product, 'save'
        )
        view = ProductViewSet.as_view(
            {'put': 'update'}
        )

        response = view(request, pk=old_product.id).render()

        assert response.status_code == 200
        assert json.loads(response.content) == product_dict

    def test_delete(self, mocker, rf):
        product = ProductFactory.build()
        url = reverse('product-detail', kwargs={'pk': product.id})
        request = rf.delete(url)
        mocker.patch.object(
            ProductViewSet, 'get_object', return_value=product
        )
        del_mock = mocker.patch.object(
            Product, 'delete'
        )
        view = ProductViewSet.as_view(
            {'delete': 'destroy'}
        )

        response = view(request).render()

        assert response.status_code == 204
        assert del_mock.assert_called


@pytest.mark.django_db
class TestUserViewSet:
    def test_list(self, mocker, rf):
        url = reverse('user-list')
        request = rf.get(url)
        qs = MockSet(
            UserFactory.build(),
            UserFactory.build(),
            UserFactory.build(),
        )
        view = UserViewSet.as_view(
            {'get': 'list'}
        )

        mocker.patch.object(
            UserViewSet, 'get_queryset', return_value=qs
        )

        response = view(request).render()

        assert response.status_code == 200
        assert json.loads(response.content)

    def test_create(self, mocker, rf):
        valid_data_dict = factory.build(
            dict,
            FACTORY_CLASS=UserFactory
        )
        valid_data_dict['url'] = None
        url = reverse('user-list')
        request = rf.post(
            url,
            content_type='application/json',
            data=json.dumps(valid_data_dict)
        )
        mocker.patch.object(
            User, 'save'
        )
        view = UserViewSet.as_view(
            {'post': 'create'}
        )

        response = view(request).render()

        assert response.status_code == 201
        assert json.loads(response.content) == valid_data_dict

    def test_update(self, mocker, rf):
        old_user = UserFactory.build()
        new_user = UserFactory.build()
        user_dict = {
            'url': None,
            'username': new_user.username,
            'first_name': new_user.first_name,
            'last_name': new_user.last_name,
            'email': new_user.email
        }
        url = reverse('user-detail', kwargs={'pk': old_user.id})
        request = rf.put(
            url,
            content_type='application/json',
            data=json.dumps(user_dict)
        )
        mocker.patch.object(
            UserViewSet, 'get_object', return_value=old_user
        )
        mocker.patch.object(
            User, 'save'
        )
        view = UserViewSet.as_view(
            {'put': 'update'}
        )

        response = view(request, pk=old_user.id).render()

        assert response.status_code == 200
        assert json.loads(response.content) == user_dict

    def test_delete(self, mocker, rf):
        user = UserFactory.build()
        url = reverse('user-detail', kwargs={'pk': user.id})
        request = rf.delete(url)
        mocker.patch.object(
            UserViewSet, 'get_object', return_value=user
        )
        del_mock = mocker.patch.object(
            User, 'delete'
        )
        view = UserViewSet.as_view(
            {'delete': 'destroy'}
        )

        response = view(request).render()

        assert response.status_code == 204
        assert del_mock.assert_called


@pytest.mark.django_db
class TestOrderViewSet:
    def test_list(self, mocker, rf):
        url = reverse('order-list')
        request = rf.get(url)
        qs = MockSet(
            OrderFactory.build(),
            OrderFactory.build(),
            OrderFactory.build(),
        )
        view = OrderViewSet.as_view(
            {'get': 'list'}
        )

        mocker.patch.object(
            OrderViewSet, 'get_queryset', return_value=qs
        )

        response = view(request).render()

        assert response.status_code == 200
        assert json.loads(response.content)

    def test_delete(self, mocker, rf):
        order = OrderFactory.build()
        url = reverse('order-detail', kwargs={'pk': order.id})
        request = rf.delete(url)
        mocker.patch.object(
            OrderViewSet, 'get_object', return_value=order
        )
        del_mock = mocker.patch.object(
            Order, 'delete'
        )
        view = OrderViewSet.as_view(
            {'delete': 'destroy'}
        )

        response = view(request).render()

        assert response.status_code == 204
        assert del_mock.assert_called
