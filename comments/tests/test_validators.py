from collections import OrderedDict
from unittest.mock import MagicMock

import pytest
from rest_framework.exceptions import ValidationError

from comments.serializers import CommentSerializer
from comments.validators import profanity_check, CommentValidator


def test_profanity_check_catches_profane_words():
    with pytest.raises(ValidationError) as ctx:
        profanity_check("co to kurwa jest?")

    assert "Not allowed word!" in str(ctx)


def test_profanity_check_allo_correct_words():
    result = profanity_check(" test comment")

    assert result is None


@pytest.fixture
def serializer_stub():
    serializer = MagicMock()
    serializer.root.context.get.return_value = "1"
    return serializer


@pytest.fixture
def serializer_stub_11():
    serializer = MagicMock()
    serializer.root.context.get.return_value = "11"
    return serializer


@pytest.fixture
def attrs_stub():
    return OrderedDict([("content", "test comment content.")])


@pytest.fixture
def attrs_stub_parent_comment(attrs_stub, comment_db):
    return attrs_stub | {"parent_comment": comment_db}


def test_comment_validator_add_comment_without_parent_comment(serializer_stub, attrs_stub):
    validator = CommentValidator()
    effect = validator(attrs_stub, serializer_stub)
    assert effect is None


def test_comment_validator_add_comment_with_parent_comment_proper_product(serializer_stub, attrs_stub_parent_comment):
    validator = CommentValidator()
    effect = validator(attrs_stub_parent_comment, serializer_stub)
    assert effect is None


def test_comment_validator_add_comment_with_parent_comment_improper_product(
    serializer_stub_11, attrs_stub_parent_comment
):
    validator = CommentValidator()
    with pytest.raises(ValidationError) as ctx:
        validator(attrs_stub_parent_comment, serializer_stub_11)

    assert "Cannot add subcomment to this comment" in str(ctx)


def test_validate_parent_comment_with_correct_data(comment_db):
    assert CommentSerializer.validate_parent_comment(comment_db) == comment_db


def test_validate_parent_comment_with_incorrect_data(subcomment_db):
    with pytest.raises(ValidationError) as ctx:
        CommentSerializer.validate_parent_comment(subcomment_db)

    assert "cannot add subcomment to this comment" in str(ctx)
