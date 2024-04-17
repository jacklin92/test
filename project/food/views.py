from django.shortcuts import render, redirect
from .models import Account
from django.contrib.auth import logout

loginv = True


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


def create(request):
    if request.method == "POST":
        clientname = request.POST.get("clientname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        if clientname and email and password:
            account = Account(
                client_name=clientname, email_address=email, password=password
            )
            if Account.objects.filter(email_address=email).exists():
                context = {"error_message": "This email is already registered."}
                return render(request, "createAc.html", context)
            account.save()
            return redirect("/login/")
        else:
            context = {
                "error_message": "All fields are required. Please provide all the necessary information.",
                "client_name": clientname,
                "email_address": email,
            }
            return render(request, "createAc/", context)
    else:
        context = {}
        return render(request, "createAc/", context)


def loginsys(request):

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        if email and password:
            account = Account.objects.filter(email_address=email).first()
            if account and account.password == password:
                request.session["client_name"] = account.client_name
                loginv = True
                return redirect("/menu1/")
        else:
            context = {"error_message": "Invalid email or password. Please try again."}
            loginv = False
            return render(request, "login/", context)

    else:
        loginv = False
        context = {}
        return render(request, "login/", context)


def logoutsys(request):
    request.session.flush()
    return redirect("/login/")



