from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

def home(request):
    return render(request,"home.html")

def signup(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        username = request.POST['username']
        password = request.POST['password']
        repassword = request.POST['repassword']

        user = User.objects.create_user(username=username, password=password, first_name=first_name)
        user.save();
        return redirect("/")
        
    
    else:
        return render(request,"signup.html")
    
def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
            
        else:
            messages.info(request, 'Invalid User')
            return render(request, "signin.html")
            

    return render(request,"signin.html")


