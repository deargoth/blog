from django import template
from posts.models import Post
from comentarios.models import Comentario
from django.contrib.auth.models import User

register = template.Library()

@register.filter(name='count_posts')
def count_posts(username):
    user_posts = Post.objects.filter(author=username)
    count = 0

    for post in user_posts:
        count += 1

    if count == 0:
        return f"Você não tem nenhum post."

    elif count == 1:
        return f'Você tem {count} post!'

    else:
        return f'Você tem {count} posts!'
    
    
@register.filter(name='count_comment')
def count_comment(username):
    user_comments = Comentario.objects.filter(user_comment=username)
    count = 0
    
    for comment in user_comments:
        count += 1

    if count == 0:
        return f'Você não tem nenhum comentário.'

    elif count == 1:
        return f'Você tem {count} comentário!'

    else:
        return f'Você tem {count} comentários!'
    
@register.filter(name='first_na')
def first_name(username):
    user = User.objects.filter(username__exact=username)
    return f'{user.first_na}'