from django.shortcuts import render, redirect
from .forms import RegisterForm, ProviderProfileForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user= form.save()
            role = form.cleaned_data['role']
            # Create a profile for the user
            Profile.objects.create(
                user=user,
                role=role,
                phone='',
                society=''
            )
            return redirect('/login/')
    else:
        form = RegisterForm()
    return render(
        request,
        'accounts/register.html',
        {
            'form': form
        }
    )

def user_login(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            error = "Invalid username or password."
    return render(
        request,
        'accounts/login.html',
        {
            'error': error
        }
    )

def user_logout(request):
    logout(request)
    return redirect('/login/')


@login_required
def update_provider_profile(request):
    profile = getattr(request.user, 'profile', None)
    if not profile or profile.role != 'provider':
        return redirect('/')
    if request.method == 'POST':
        form = ProviderProfileForm(
            request.POST,
            instance=profile)
        
        if form.is_valid():
            form.save()
            return redirect(
                '/provider/dashboard/')
    else:
        form = ProviderProfileForm(
            instance=profile)
    return render(
        request,
        'accounts/provider_profile.html',
        {
            'form': form
        }
    )