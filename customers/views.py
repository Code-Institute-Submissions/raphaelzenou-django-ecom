from django.shortcuts import render, redirect
from storemain.models import User
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from .forms import CreateProfileForm, EditProfileForm
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth import get_user_model
User = get_user_model()

def signup(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created ! You can now sign in.')
            return redirect('login')
    else:
        form = CreateProfileForm()
        context = {
            'page': 'Create Profile',
            'form': form,
        }
        return render(request, 'registration/signup.html', context)

@login_required
def profile(request):

    if request.user.is_authenticated:
        context = {
            'page': 'Profile',
            'user': request.user,
        }
        return render(request, 'customers/profile.html', context)
    else:
        context = {
            'page': 'Sign In',
        }
        return redirect(settings.LOGIN_URL, request.path)

@login_required
def editprofile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated !')
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)
        context = {
            'page': 'Edit Profile',
            'form': form,
        }
        return render(request, 'customers/editprofile.html', context)