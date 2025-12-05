from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .auth_forms import UserSignUpForm, AdminSignUpForm, UserLoginForm
from .models import User, VideoUploadHistory

def user_signup(request):
    if request.user.is_authenticated:
        return redirect('ml_app:home')
    
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now login.')
            return redirect('ml_app:login')
    else:
        form = UserSignUpForm()
    
    return render(request, 'auth/signup.html', {'form': form, 'user_type': 'User'})


def admin_signup(request):
    if request.user.is_authenticated:
        return redirect('ml_app:home')
    
    if request.method == 'POST':
        form = AdminSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Admin account created for {username}! You can now login.')
            return redirect('ml_app:login')
    else:
        form = AdminSignUpForm()
    
    return render(request, 'auth/admin_signup.html', {'form': form, 'user_type': 'Admin'})


def user_login(request):
    if request.user.is_authenticated:
        return redirect('ml_app:home')
    
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                next_url = request.GET.get('next', 'ml_app:home')
                return redirect(next_url)
    else:
        form = UserLoginForm()
    
    return render(request, 'auth/login.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('ml_app:login')


@login_required
def user_profile(request):
    # Get user's upload history
    upload_history = VideoUploadHistory.objects.filter(user=request.user)
    
    context = {
        'user': request.user,
        'upload_history': upload_history,
        'total_uploads': upload_history.count()
    }
    
    return render(request, 'auth/profile.html', context)


@login_required
def admin_dashboard(request):
    if request.user.user_type != 'admin':
        messages.error(request, 'You do not have permission to access the admin dashboard.')
        return redirect('ml_app:home')
    
    # Get statistics
    total_users = User.objects.filter(user_type='user').count()
    total_admins = User.objects.filter(user_type='admin').count()
    total_videos = VideoUploadHistory.objects.count()
    recent_uploads = VideoUploadHistory.objects.all()[:10]
    
    context = {
        'total_users': total_users,
        'total_admins': total_admins,
        'total_videos': total_videos,
        'recent_uploads': recent_uploads
    }
    
    return render(request, 'auth/admin_dashboard.html', context)
