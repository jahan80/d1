from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse,JsonResponse
def home(request):
    return HttpResponse('<h1>Home page </h1>')
def about(request):
    return HttpResponse('<h1>About page </h1>')
def contact(request):
    return HttpResponse('<h1>contact page </h1>')

