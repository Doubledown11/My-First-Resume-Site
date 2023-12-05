from django import forms
from .models import Blog 
from django.forms import ModelForm, DateInput


#  A form for the input required for the commenting functionality.
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['entry_name', 'body', 'blog_desc']
        labels = {
            'entry_name' : 'Enter Entry Title',
            'body': 'Enter text',
            'blog_desc' : 'Enter a Short Description'
            }