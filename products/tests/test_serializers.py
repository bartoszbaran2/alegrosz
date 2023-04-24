from products import serializers


def test_serializer_all_fields_present(product_db):
    serializer = serializers.ProductSerializer(instance=product_db)
    assert tuple(serializer.data.keys()) == (
        "id",
        "name",
        "description",
        "price",
        "image",
        "stock_count",
        "popularity",
        "rank",
        "barcode",
        "categories",
        "subcategories",
    )
