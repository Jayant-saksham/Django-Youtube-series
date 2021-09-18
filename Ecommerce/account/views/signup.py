from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views import View

class SignupMethod(View):

	def post(self, request):
		name = request.POST.get('name')
		email = request.POST.get('email')
		password = request.POST.get('password')
		confirmpassword = request.POST.get('confirmpassword')
		phone = request.POST.get('phone')
		if confirmpassword == password:
			user = User.objects.create_user(
				username=name,
				email=email,
				password=password,
				first_name=phone,
			)
		else:
			print("No valid")
		return render(request, "login.html")

	def get(self, request):
		return render(request, 'signup.html')

