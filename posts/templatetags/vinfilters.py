from django import template


register = template.Library()

@register.filter(name='plural_comment')
def plural_comment(num_comment):
    if num_comment == 0:
        return f'Nenhum comentário'
    
    elif num_comment == 1:
        return f'{num_comment} comentário'
    
    else:
        return f'{num_comment} comentários'
    