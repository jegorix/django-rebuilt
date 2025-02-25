from django.shortcuts import render
from .forms import UserForm
from django.http import HttpResponse
# Create your views here.


def home(request):
    userform = UserForm()
    data = {
        'age': 19,
        'form': userform,
    }
    head_items = [
        'info', 'about', 'goods', 'contact',
    ]
    return render(request, 'boiler/index.html', context= {'head_items': head_items, 'data':data})

def about(request):
    # return render(requset, '<h1>Hi message!</h1>')
    return render(request, 'boiler/pointer.html')

def goods(request):
    return HttpResponse('GOODS PAGE')



