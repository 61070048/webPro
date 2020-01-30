from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def student_list(request):
    return HttpResponse("students List")
def add(request):
    return HttpResponse("students added")
def edit(request):
    return HttpResponse("students edited")
