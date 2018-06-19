from django.db import models

from .basic import BlogUser


class Post(models.Model):
    user = models.ForeignKey(
        BlogUser,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=80)
    content = models.TextField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    @property
    def show_post(self):
        return Post.objects.filter(user__name=self.user.name)

    @property
    def show_like_post(self):
        return PostLike.objects.filter(post_like_unlike='L')


class PostLike(models.Model):
    POST_LIKE_UNLIKE = (
        ('L', 'Like'),
        ('N', 'Nothing'),
        ('U', 'Unlike'),
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='posts_like'
    )

    user = models.ForeignKey(
        BlogUser,
        on_delete=models.CASCADE,
        related_name='posts_like_user'
    )

    post_like_unlike = models.CharField(max_length=1, choices=POST_LIKE_UNLIKE)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name
