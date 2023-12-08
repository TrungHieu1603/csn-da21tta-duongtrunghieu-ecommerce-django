from django.urls import reverse
from .models import Resume
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

def resume_view(request):
    resumes = Resume.objects.all()
    return render(request, 'resumes.html', {'resumes': resumes})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Đăng nhập người dùng ngay sau khi đăng ký (tùy chọn)
            login(request, user)
            admin_url = reverse('admin:index')
            return redirect(admin_url)
              # Chuyển hướng sau khi đăng ký thành công
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})