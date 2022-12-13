from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from categorias.models import Categoria

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    data = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    excerto = models.TextField()
    category = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, null=True, blank=True)
    imagem = models.ImageField(upload_to='post_img/%Y/%m', blank=True, null=True)
    published = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.title