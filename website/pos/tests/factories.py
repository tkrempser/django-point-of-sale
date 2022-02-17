import factory

from django.contrib.auth.models import User

from pos.models import Customer, Product, Order


class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer

    first_name = factory.faker.Faker('first_name')
    last_name = factory.faker.Faker('last_name')
    email = factory.faker.Faker('ascii_email')


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.faker.Faker('word')
    price = factory.faker.Faker('pyfloat', positive=True)
    commission = factory.faker.Faker(
        'pyfloat', min_value=0.0, max_value=10.0)


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.faker.Faker('word')
    first_name = factory.faker.Faker('first_name')
    last_name = factory.faker.Faker('last_name')
    email = factory.faker.Faker('ascii_email')


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Order

    customer = factory.SubFactory(CustomerFactory)
    seller = factory.SubFactory(UserFactory)
    created_at = factory.faker.Faker('date')
