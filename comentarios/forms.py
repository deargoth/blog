from django.forms import ModelForm
from .models import Comentario
from django.contrib.auth.models import User, AnonymousUser


class PublicForm(ModelForm):
    def clean(self):
        data = self.cleaned_data

        name = data.get('name')
        email = data.get('email')
        comment = data.get('comment')

        if len(name) < 3:
            self.add_error(
                'name',
                'Seu nome precisa de mais de 3 carácteres.'
            )

        if len(comment) < 5:
            self.add_error(
                'comment',
                'O seu comentário precisa possuir mais de 5 carácteres.'
            )

    class Meta:
        model = Comentario
        fields = ('name', 'email', 'comment')


class AuthForm(ModelForm):
    def clean(self):
        data = self.cleaned_data

        comment = data.get('comment')

        if len(comment) < 5:
            self.add_error(
                'comment',
                'O seu comentário precisa possuir mais de 5 carácteres.'
            )

    class Meta:
        model = Comentario
        fields = ('comment',)
