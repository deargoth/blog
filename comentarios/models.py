from django.db import models
from posts.models import Post
from django.contrib.auth.models import User
from django.utils import timezone


class Comentario(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField()
    post_comment = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_comment = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, blank=True, null=True)
    date_comment = models.DateTimeField(default=timezone.now)
    published_comment = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def first_name(self):
        name = self.user_comment.get_full_name()
        print(name)
        return name

    def user_email(self, username):
        for i in range(0,10):
            print('oi')
            
        email = self.user_comment.email
        print(email)
        return email
