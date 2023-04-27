from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import ReadOnlyField

from users.serializers import CustomUserSerializer
from . import models
from .models import Comment
from .validators import CommentValidator, profanity_check


class CommentSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer(read_only=True)
    content = serializers.CharField(validators=[profanity_check])  # dla pola osobna z pliku

    class Meta:
        model = models.Comment
        fields = ("id", "product", "author", "content", "created_at", "parent_comment")
        read_only_fields = ("product",)
        validators = (CommentValidator(),)  # validator dla całego serializatora

    @staticmethod
    def validate_parent_comment(value):  # validator pola (tzw. wew validator)
        if value.parent_comment:
            raise ValidationError("cannot add subcomment to this comment")

        return value
