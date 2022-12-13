from django import forms
from posts.models import Post
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django_summernote.widgets import SummernoteWidget

class FormPost(forms.ModelForm):
    content = forms.CharField(widget=SummernoteWidget)
    
    def clean(self):
        data = self.cleaned_data
        
        title = data.get('title')
        content = data.get('content')
        excerto = data.get('excerto')
        
        if len(title) < 10:
            self.add_error(
                'title',
                'O título precisa ter mais de 10 caracteres.'
            )

        if len(content) < 20:
            self.add_error(
                'title',
                'O conteúdo precisa ter mais de 10 caracteres.'
            )   
            
        if len(excerto) < 20:
            self.add_error(
                'title',
                'O excerto precisa ter mais de 10 caracteres.'
            )
        
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ('author', 'data', 'published', )
        
        
class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = '__all__'