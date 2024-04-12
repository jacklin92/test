from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "index.html")


def menu1(request):
    return render(request, "menu1.html")


def page2(request):
    return render(request, "page2.html")


def login(request):
    return render(request, "login.html")


def createAc(request):
    return render(request, "createAc.html")
