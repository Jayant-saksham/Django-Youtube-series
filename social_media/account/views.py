from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def sigup_view(request):
    '''function to create a new user'''

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        if password == confirmpassword:
            user = User.objects.create_user(
                first_name = username, 
                username = username,
                email = email, 
                password = password
            )
            messages.success(request, f"User {username} Created")
        else:
            messages.error(request, "Invalid credentials")
    return render(request, 'account/signup.html')


def login_view(request):
    '''Function to login the user'''

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully loggedIN")
            return redirect("home_page")
        else:
            messages.error(request,"Invalid credentials")
            return HttpResponse("Invalid credentials")

    return HttpResponse("GET request")


def logout_view(request):
    logout(request)
    messages.success(request, "User loggedout")
    return redirect("/")
