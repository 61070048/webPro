from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Dashboard(request):
    return HttpResponse('PRESENT 50 ')
def export(request):
    return HttpResponse('search & export')
