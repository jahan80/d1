from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
def home(request):
    return  render(request, 'website/index.html')
def about(request):
    return render(request, 'website/../templates/about.html')
def contact(request):
    return render(request, 'website/contact.html')

