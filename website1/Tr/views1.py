from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse,JsonResponse
def test_http2(request):
    return HttpResponse('<h1>test_h2 http</h1>')

def test_http3(request):
    return HttpResponse('<h1>test_h3 http</h1>')

