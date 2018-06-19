from django.contrib import admin
from .models import BlogUser, UserInfo, Post, PostLike, Comment, CommentLike

admin.site.register(BlogUser)
admin.site.register(UserInfo)
admin.site.register(Post)
admin.site.register(PostLike)
admin.site.register(Comment)
admin.site.register(CommentLike)
