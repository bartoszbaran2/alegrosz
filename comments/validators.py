from rest_framework.exceptions import ValidationError


class CommentValidator:
    requires_context = True

    def __call__(self, attrs, serializer, *args, **kwargs):
        product_id = serializer.root.context.get("product_pk")
        if product_id and product_id.isdigit():
            product_id = int(product_id)

        parent_comment = attrs.get("parent_comment")

        if parent_comment is not None and parent_comment.product.id != product_id:
            raise ValidationError("Cannot add subcomment to this comment")


def profanity_check(value):
    profane_words = ["kurwa", "chuj", "fuck"]

    for word in profane_words:
        if word in value:
            raise ValidationError("Not allowed word!")
