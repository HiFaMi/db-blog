from django.db import models


class BlogUser(models.Model):
    name = models.CharField(max_length=50)
    friends = models.ManyToManyField(
        'self',
        related_name='my_friends'
    )
    block_users = models.ManyToManyField(
        'self',
        related_name='block_friends',
        symmetrical=False,
    )

    def __str__(self):
        return self.name


class UserInfo(models.Model):
    user = models.OneToOneField(
        BlogUser,
        on_delete=models.CASCADE,
        related_name='user_info'
    )

    address = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=50)


