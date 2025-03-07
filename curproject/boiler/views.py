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

    # if request.method == "POST":
    #     name = request.POST.get("name")
    #     age = request.POST.get("age")
    #     sex = request.POST.get("sex")
    #     text = request.POST.get("text")
    #     output = f"<h2>Username: {name}<h2> <h3>Age: {age}<h3> <h3>Sex: {sex}<h3> <h3>Text: {text}</h3>"
    #     return HttpResponse(output)
    # else:
    #     userform = UserForm(field_order = ["name", "age", "comment"])
    #     return render(request, 'boiler/index.html', context={'form': userform, 'data': data})
    userform = UserForm()
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data["name"]
            return HttpResponse(f"<h2>Name entered successfully - {name}</h2>")

    return render(request, "boiler/index.html", {"form": userform})



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
