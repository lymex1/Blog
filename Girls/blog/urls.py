from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('post/<int:pk>/', views.post_detail, name='post_detail')
]