from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    data = {
        'age': 5,
    }
    return HttpResponse("Hello, world. You're at the polls page.")

def about(requset):
    # return render(requset, '<h1>Hi message!</h1>')
    return HttpResponse("HELLOOOOO")
