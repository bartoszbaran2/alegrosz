from django.core.validators import BaseValidator
from rest_framework.exceptions import ValidationError


class CommentValidator:
    def __call__(self, serializer, *args, **kwargs):
        print("*" * 20)
        print(serializer)
        print("*" * 20)
        product = serializer.data.get("product")
        parent_comment = serializer.data.get("parent_comment")

        if product.id != parent_comment.product.id:
            raise ValidationError("something is no yes")
