from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import FormPost, RegisterForm, LoginForm
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic import View
from django.contrib.auth.views import LoginView 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from posts.models import Post

class LoginPage(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = LoginForm
    next_page = '/'
        
def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    user = request.POST.get('username')
    password = request.POST.get('password')

    user = auth.authenticate(request, username=user, password=password)

    if not user:
        messages.error(request, 'Usuário ou senha inválidos.')
        return render(request, 'accounts/login.html')

    else:
        auth.login(request, user)
        return redirect('index')


def logout(request):
    auth.logout(request)
    return redirect('index')


class Register(CreateView):
    template_name = 'accounts/register.html'
    form_class = RegisterForm
    success_url = '/accounts/login/'

class DashBoard(LoginRequiredMixin, ListView):
    model = User
    login_url = '/accounts/login'
    permission_denied_message = 'Página restrita apenas para logados.'
    template_name = 'accounts/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loggedin_user = self.request.user
        
        context['user'] = loggedin_user
        return context
    
class CreatePost(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Post
    login_url = '/accounts/login/'
    form_class = FormPost
    template_name = 'accounts/create_post.html'
    
    
    def form_valid(self, form):
        post_form = Post(**form.cleaned_data)
        post_form.author = self.request.user
        
        post_form.save()
        return redirect('index')
    
    success_message = 'Post enviado para análise com sucesso.'

