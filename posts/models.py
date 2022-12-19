from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from categorias.models import Categoria
from PIL import Image
from django.conf import settings

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
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.imagem:
            self.resize_image(self.imagem.name, 800)
        
    @staticmethod
    def resize_image(img_name, new_width):
        img_path = settings.MEDIA_ROOT / img_name
        img = Image.open(img_path)
        width, height = img.size
        new_height = (new_width * height) / width

        if width <= new_width:
            img.close()
            return

        new_img = img.resize((new_width, new_height), Image.ANTIALIAS)
        new_img.save(
            img_path,
            optimize=True,
            quality=60,
        )
        new_img.close()