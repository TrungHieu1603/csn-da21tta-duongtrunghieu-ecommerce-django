from django.urls import path
from django.contrib import admin
from .views import resume_view
from .views import register_view
urlpatterns = [
    path('', resume_view, name='resume-list'),
    path('register/', register_view, name='register'),
    path('admin/', admin.site.urls, name='admin:index'),
]


