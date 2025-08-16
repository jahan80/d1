
from django.http import HttpResponse,JsonResponse
def test_http(request):
    return HttpResponse("Hello, world. ")

def test_json(request):
        return JsonResponse({'test':'json'})


def test_http1(request):
    return HttpResponse('<h1>test http</h1>')
