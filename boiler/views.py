from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    data = {
        'age': 5,
    }
    return render(request, 'boiler/index.html', data)

def about(requset):
    # return render(requset, '<h1>Hi message!</h1>')
    return HttpResponse("HELLOOOOO")

