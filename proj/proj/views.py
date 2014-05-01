from django.http import HttpResponse


def home(request):
    return HttpResponse('Hello')

def auth(request):
    return HttpResponse('Okay')
