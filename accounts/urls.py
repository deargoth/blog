from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginPage.as_view(), name='index_login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.DashBoard.as_view(), name='dashboard'),
    path('register/', views.Register.as_view(), name='register'),
    path('post_create/', views.CreatePost.as_view(), name='post_create'),
]