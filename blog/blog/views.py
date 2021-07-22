from django.shortcuts import render 

# This file is made by me

def home(request):
    return render(request, 'home.html')

