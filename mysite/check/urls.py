from django.contrib import admin
from django.urls import path
from check import views
urlpatterns = [
    path('check/', views.check_name),
    path('login/', views.login),
    path('course/<int:id>/', views.detail)
]
