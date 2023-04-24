from comments.models import Comment


def test_create_comment_reply(product_db, user):
    comment = Comment.objects.create(product=product_db, author=user, content="test content")

    reply = Comment.objects.create(product=product_db, author=user, content="test reply", parent_comment=comment)

    parent_comment = Comment.objects.first()
    reply_comment = Comment.objects.filter(parent_comment__isnull=False).first()

    assert parent_comment.replies.first() == reply
    assert reply_comment.parent_comment == parent_comment
