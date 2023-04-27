import pytest

from comments.serializers import CommentSerializer


def test_comment_serializer_with_valid_data(product_db, comment_db):
    data = {"content": "test content", "parent_comment": 1}

    serializer = CommentSerializer(data=data, context={"product_pk": "1"})

    assert serializer.is_valid()


def test_comment_serializer_with_invalid_data(product_db, comment_db):
    data = {"parent_comment": 1}

    serializer = CommentSerializer(data=data, context={"product_pk": "1"})

    assert not serializer.is_valid()


def test_comment_serializer_saves_data(user, product_db, comment_db):
    data = {"content": "test content", "parent_comment": 1}

    serializer = CommentSerializer(data=data, context={"product_pk": "1"})

    if serializer.is_valid():
        instance = serializer.save(author=user, product=product_db)
        assert instance.content == "test content"
    else:
        pytest.fail("Serializer validation failed.")


def test_comment_serializer_updates_data(comment_db):
    data = {
        "content": "test update content",
    }
    serializer = CommentSerializer(instance=comment_db, data=data, partial=True)
    if serializer.is_valid():
        instance = serializer.save()
        assert instance.content == "test update content"
    else:
        pytest.fail("Serializer validation failed.")


def test_comment_serializer_serializes_data(comment_db):
    serializer = CommentSerializer(instance=comment_db)

    assert serializer.data["content"] == comment_db.content


def test_comment_serializer_parent_comment_validator_valid_data(comment_db):
    data = {"content": "test content", "parent_comment": 1}
    serializer = CommentSerializer(data=data, context={"product_pk": "1"})

    assert serializer.is_valid()


def test_comment_serializer_parent_comment_validator_invalid_data(comment_db, subcomment_db):
    data = {"content": "test content", "parent_comment": 2}
    serializer = CommentSerializer(data=data, context={"product_pk": "1"})

    assert not serializer.is_valid()


# TODO napisze test case do pozostałych walidatorów
# TODO napisze liste test casów do serializatorów
