from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm, LoginForm


# Create your views here.

def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display blank registration form.
        form = RegisterForm()
    else:
        # Process completed form.
        form = RegisterForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
        return redirect('resume:admin_blogs')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'registration/register.html', context)


def logout(request):
    logout(request)
    return redirect('')


def login(request, user):
    """Log in a user."""

    if request.method == 'POST':
        # Display blank login form.
        form = LoginForm()
        
    else:
        # Process completed form.
        form = LoginForm(data=request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('resume:admin_blogs')
    
    # Display a blank or invalid form.
    context = {'form':form}
    return render(request, '/users/login/')

