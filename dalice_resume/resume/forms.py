from django import forms
from .models import Blog 
from django.forms import ModelForm, DateInput


#  A form for the input required for the commenting functionality.
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['body']
        labels = {'body': 'Enter text'}