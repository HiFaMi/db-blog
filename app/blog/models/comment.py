from django.db import models
from .basic import BlogUser


class Comment(models.Model):
    user = models.ForeignKey(
        BlogUser,
        on_delete=models.CASCADE,
        related_name='comment_user',
    )

    content = models.TextField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    @property
    def show_comment(self):
        return Comment.objects.filter(user__name=self.user.name)

    @property
    def show_like_comment(self):
        return self.comment_like_user.filter(comment_like_unlike='L')


class CommentLike(models.Model):
    COMMENT_LIKE_UNLIKE = (
        ('L', 'Like'),
        ('N', 'Nothing'),
        ('U', 'Unlike'),
    )

    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        related_name='comment_like',
    )
    user = models.ForeignKey(
        BlogUser,
        on_delete=models.CASCADE,
        related_name='comment_like_user',
    )

    comment_like_unlike = models.CharField(max_length=1, choices=COMMENT_LIKE_UNLIKE)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name
