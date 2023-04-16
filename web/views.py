from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import auth

@login_required
def index(request):
    return render(request, 'index/index.html')

@login_required
def q(request):
    return render(request, 'index/q.html')

def my_login(request):
    if request.method == "GET":
        return render(request, "index/login.html")
    username = request.POST.get("username")
    password = request.POST.get("pwd")
    user_obj = auth.authenticate(username=username, password=password)
    #print(user_obj.username)
    if not user_obj:
        return redirect("/login/")
    else:
        auth.login(request, user_obj)
        path = request.GET.get("next") or "/"
        print(path)
        red = redirect(path)
        red.set_cookie('username',user_obj.get_username())
        return red
    
def my_logout(request):
    ppp = auth.logout(request)
    red = redirect("/login/")
    red.set_cookie('username','')
    return red
# Create your views here.
