from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views import View

class LoginMethod(View):

	def post(self, request):
		name = request.POST.get('name')
		password = request.POST.get('password')
		user = authenticate(username=name, password=password)
		if user is not None:
			login(request, user)
			return redirect("home_page")
		else:
			return redirect("/")

	def get(self, request):
		return render(request, 'login.html')
