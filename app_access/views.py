from django.shortcuts import render,HttpResponse,HttpResponseRedirect,Http404,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.core.cache import cache

# Create your views here.

def acc_login(request):
    err_msg = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(request.GET.get("next") if request.GET.get("next") else "/index/")

        else:
            err_msg["error"] = 'Wrong username or password!'

def acc_logout(request):
    logout(request)
    pass