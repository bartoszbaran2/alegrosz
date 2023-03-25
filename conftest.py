import pytest
from faker import Faker
import faker_commerce
from products.models import Product

fake = Faker("pl_PL")
fake.add_provider(faker_commerce.Provider)


@pytest.fixture
def product():
    """fixture for create product without save to DB.
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
def product_db(product, db):
    """fixture for create product
    :param: db: db fixture, adds db handling
    :return: obj of Product class, representing row in table.
    :rtype: Product
    """
    product.save()
    return product
