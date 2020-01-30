from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def check_name(request):
    return HttpResponse("checked")

def login(request):
    return HttpResponse("Loged In")

def detail(request, id):
    return HttpResponse("Subject:%d, Total:80, Present:50, Absent:30"%id)