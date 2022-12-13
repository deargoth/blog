from django.db import models
from django import forms
# from django.forms import ModelForm
from posts.models import Post
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote.fields import SummernoteTextField



class FormEditing(forms.ModelForm):
    content = forms.CharField(widget=SummernoteWidget())
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ('author', 'data', 'category', )