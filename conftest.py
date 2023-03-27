import pytest
from faker import Faker
import faker_commerce
from products.models import Product
import factory
from pytest_factoryboy import register

fake = Faker("pl_PL")
fake.add_provider(faker_commerce.Provider)


@pytest.fixture
def product_onion():
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


@register
class ProductFactory(factory.Factory):
    class Meta:
        model = Product

    name = "Onion"
