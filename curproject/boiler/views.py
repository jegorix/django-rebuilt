from django.core.signals import request_started
from django.shortcuts import render
from .forms import UserForm
from django.http import HttpResponse
# Create your views here.


def home(request):

    data = {
        'age': 19
    }
    head_items = [
        'info', 'about', 'goods', 'contact',
    ]

    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        sex = request.POST.get("sex")
        output = f"<h2>Username: {name}<h2> <h3>Age: {age}<h3> <h3>Sex: {sex}<h3>"
        return HttpResponse(output)
    else:
        userform = UserForm()
        return render(request, 'boiler/index.html', context={'form': userform, 'data': data})




    # return render(request, 'boiler/index.html', context= {'head_items': head_items, 'data':data})





def about(request):
    # return render(requset, '<h1>Hi message!</h1>')
    return render(request, 'boiler/pointer.html')

def goods(request):
    return HttpResponse('GOODS PAGE')

def contact(request):
    return render(request, 'boiler/contacts.html')

def info(request):
    return render(request, 'boiler/info.html')
