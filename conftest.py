import pytest
from django.contrib.auth import get_user_model
from faker import Faker
import faker_commerce
from products.models import Product, Category
import factory
from pytest_factoryboy import register

fake = Faker("pl_PL")
fake.add_provider(faker_commerce.Provider)


@pytest.fixture
def user(db, django_user_model):
    return django_user_model.objects.create_user(username="test_user", password="test_pass", email="test@test.com")


@pytest.fixture
def product_onion(user):
    """fixture for create product_onion without save to DB.
    :return: obj of Product class, representing row in table.
    :rtype: Product
    """
    name = "Polish onion"
    return Product(
        name=name,
        description=fake.sentence(),
        price=fake.ecommerce_price(),
        image=fake.file_name(category="image", extension="png"),
        stock_count=fake.unique.random_int(min=1, max=100),
        barcode=fake.ean(length=13),
        owner=user,
    )


@pytest.fixture
def product_db(product_onion, db):
    """fixture for create product_onion
    :param: db: db fixture, adds db handling
    :return: obj of Product class, representing row in table.
    :rtype: Product
    """
    product_onion.save()
    return product_onion


@pytest.fixture
def api_request_factory():
    from rest_framework.test import APIRequestFactory

    return APIRequestFactory()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    username = factory.Sequence(lambda n: f"{factory.Faker('sentence', nb_words=3)} {n}")
    password = factory.Faker("word")
    email = factory.Faker("email")


@register
class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "products.Product"

    name = factory.Sequence(lambda n: f"{factory.Faker('sentence', nb_words=2)}" + f"{n}")
    description = factory.Faker("paragraph")
    price = factory.Faker("pydecimal", left_digits=2, right_digits=2, positive=True, min_value=10, max_value=34)
    image = factory.Faker("image_url")
    stock_count = factory.Faker("pyint", min_value=1, max_value=50)
    barcode = factory.Faker("ean13")
    owner = factory.SubFactory(UserFactory)


@pytest.fixture
def products_batch(db):
    return ProductFactory.create_batch(60)


@pytest.fixture
def category_db(db):
    return Category.objects.create(name="Potato")
