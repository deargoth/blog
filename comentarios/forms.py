from django.forms import ModelForm
from .models import Comentario
import requests


class PublicForm(ModelForm):
    def clean(self):
        raw_data = self.data

        cleaned_data = self.cleaned_data
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        comment = cleaned_data.get('comment')

        if len(name) < 3:
            self.add_error(
                'name',
                'Seu nome precisa de mais de 3 caracteres.'
            )

        if len(comment) < 5:
            self.add_error(
                'comment',
                'O seu comentário precisa possuir mais de 5 caracteres.'
            )

    class Meta:
        model = Comentario
        fields = ('name', 'email', 'comment')


class AuthForm(ModelForm):
    def clean(self):
        raw_data = self.data
        recaptcha_response = raw_data.get('g-recaptcha-response')
        
        # https://www.google.com/recaptcha/api/siteverify
        # secret
        # response

        recaptcha_request = requests.post(
            'https://www.google.com/recaptcha/api/siteverify',
            data = {
                'secret': '6LeFS5cjAAAAAKCQOIoVfJjm8kLOtg5CK6LV-PMt',
                'response': recaptcha_response
            }
        )
        recaptcha_result = recaptcha_request.json()

        if not recaptcha_result.get('success'):
            self.add_error(
                'comment',
                'Desculpe! Ocorreu um erro, tente novamente.'
            )
            return
        
        cleaned_data = self.cleaned_data
        comment = cleaned_data.get('comment')

        if len(comment) < 5:
            self.add_error(
                'comment',
                'O seu comentário precisa possuir mais de 5 carácteres.'
            )

    class Meta:
        model = Comentario
        fields = ('comment',)
