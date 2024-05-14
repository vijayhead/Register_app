from django.shortcuts import render
from Regapp.models import UserRegister
from django.http import HttpResponse
# Create your views here.

def register_view(request):
    name = request.POST['t1']
    uname = request.POST['t2']
    password = request.POST['t3']
    user = UserRegister(name = name,uname = uname,password = password)
    user.save()
    msg = "<h1> User Registered</h1>"
    return HttpResponse(msg)

def register_home(request):
    return render(request,"user_register.html")