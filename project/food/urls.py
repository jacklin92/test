from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("menu1/", views.menu1, name="menu1"),
    path("page2/", views.page2, name="page2"),
    path("login/", views.login, name="login"),
    path("createAc/", views.createAc, name="createAc"),
    path("create/", views.create, name="create"),
    path("loginsys/", views.loginsys, name="loginsys"),
    path("logoutsys/", views.logoutsys, name="logoutsys"),
    path("posting/",views.posting,name="posting"),
 ]
