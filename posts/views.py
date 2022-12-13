from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.base import RedirectView
from django.views.generic import View
from posts.models import Post
from django.db.models import Q, Case, When, Count
from comentarios.forms import PublicForm, AuthForm
from comentarios.models import Comentario
from django.contrib import messages
from posts.forms import FormEditing
from django.urls import reverse_lazy
from django.http import Http404


class Index(ListView):
    model = Post
    template_name = 'posts/index.html'
    paginate_by = 3
    context_object_name = 'posts'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.select_related('category')
        qs = qs.order_by('-id')
        qs = qs.filter(published=True)
        qs = qs.annotate(num_comment=Count(
            Case(
                When(comentario__published_comment=True, then=1)
            )
        ))

        return qs


class Busca(Index):
    template_name = 'posts/busca.html'

    def get_queryset(self):
        qs = super().get_queryset()
        termo = self.request.GET.get('termo')

        if not termo:
            return qs

        qs = qs.filter(
            Q(title__icontains=termo) |
            Q(author__first_name__iexact=termo) |
            Q(content__icontains=termo) |
            Q(excerto__icontains=termo) |
            Q(category__name_cat__iexact=termo)

        )

        return qs


class Post_Categoria(Index):
    template_name = 'posts/categoria.html'

    def get_queryset(self):
        qs = super().get_queryset()
        categoria = self.kwargs.get('categoria', None)

        if not categoria:
            return qs

        qs = qs.filter(category__name_cat__iexact=categoria)

        return qs


class Post_Detalhes(View):
    template_name = 'posts/post_detalhes.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        self.pk = self.kwargs.get('pk')
        post = get_object_or_404(Post, pk=self.pk)
        self.context = {
            'post': post,
            'comments': Comentario.objects.filter(post_comment=post, published_comment=True),
            'publicform': PublicForm(request.POST or None),
            'authform': AuthForm(request.POST or None),
        }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):

        publicform = self.context['publicform']
        authform = self.context['authform']

        if request.user.is_authenticated:
            authform = self.context['authform']

            if not authform.is_valid():
                return render(request, self.template_name, self.context)

            comment = authform.save(commit=False)
            
            comment.user_comment = request.user
            comment.email = request.user.email
            comment.name = request.user.first_name
            comment.post_comment = self.context['post']
            comment.save()


        else:
            publicform = self.context['publicform']
            
            if not publicform.is_valid():
                return render(request, self.template_name, self.context)

            comment = publicform.save(commit=False)
            
            comment.post_comment = self.context['post']
            comment.save()
            
        messages.success(
            self.request, 'Comentário enviado para análise com sucesso.')
        return redirect('post_detalhes', pk=self.pk)


class EditPost(UpdateView):
    model = Post
    form_class = FormEditing
    success_url = '/'
    template_name = 'posts/edit_post.html'


class DeletePost(DeleteView):
    model = Post
    success_url = '/'
    template_name = 'posts/confirm_delete.html'


class Handler404(RedirectView):
    url = '/'
