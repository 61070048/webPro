from django.contrib import admin
from django.urls import path
from admin import views
urlpatterns = [
    path('list/', views.student_list),
    path('add/', views.add),
    path('edit/', views.edit),
    
]
