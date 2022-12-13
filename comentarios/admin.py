from django.contrib import admin
from .models import Comentario


class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'user_comment', 'date_comment', 'published_comment')
    list_display_links = ('id', 'name', )
    list_editable = ('published_comment', )
    
    
admin.site.register(Comentario, ComentarioAdmin)