from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    path('detalhes/<int:pk>', views.Post_Detalhes.as_view(), name="post_detalhes"),
    path('busca/', views.Busca.as_view(), name="busca"),
    path('categoria/<str:categoria>', views.Post_Categoria.as_view(), name="categoria"),
    path('delete/<int:pk>', views.DeletePost.as_view(), name="delete"),
    path('editing/<int:pk>', views.EditPost.as_view(), name="edit_post"),
]