import faker_commerce
import pytest

from products.models import Product
from faker import Faker

fake = Faker("pl_PL")
fake.add_provider(faker_commerce.Provider)


@pytest.fixture
def product(db):
    """fixture for create product
    :param: db: db fixture, adds db handling
    :return: obj of Product class, representing row in table.
    :rtype: Product
    """
    name = "Polish onion"
    return Product.objects.create(
        name=name,
        description=fake.sentence(),
        price=fake.ecommerce_price(),
        image=fake.file_name(category="image", extension="png"),
        stock_count=fake.unique.random_int(min=1, max=100),
        barcode=fake.ean(length=13),
    )


def test_correct_gui_representation():
    name = fake.ecommerce_name()
    product = Product(
        name=name,
        description=fake.sentence(),
        price=fake.ecommerce_price(),
        image=fake.file_name(category="image", extension="png"),
        stock_count=fake.unique.random_int(min=1, max=100),
        barcode=fake.ean(length=13),
    )
    assert str(product) == name


def test_auto_slug(product):
    assert product.slug == "polish-onion"


def test_custom_slug(db):
    name = fake.ecommerce_name()
    product = Product(
        name=name,
        description=fake.sentence(),
        price=fake.ecommerce_price(),
        image=fake.file_name(category="image", extension="png"),
        stock_count=fake.unique.random_int(min=1, max=100),
        barcode=fake.ean(length=13),
        slug="test-custom-slug",
    )
    assert product.slug == "test-custom-slug"


@pytest.mark.skip(reason="WIP")
def test_custom_invalid_slug(db):
    name = fake.ecommerce_name()
    product = Product(
        name=name,
        description=fake.sentence(),
        price=fake.ecommerce_price(),
        image=fake.file_name(category="image", extension="png"),
        stock_count=fake.unique.random_int(min=1, max=100),
        barcode=fake.ean(length=13),
        slug="test custom-slug",
    )
    assert product.slug == "test-custom-slug"
