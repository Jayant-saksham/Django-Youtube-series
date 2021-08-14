from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def login_view(request):
	return render(request, 'login.html')


def signup_view(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		password = request.POST.get('password')
		confirmpassword = request.POST.get('confirmpassword')
		phone = request.POST.get('phone')
		if confirmpassword == password:
			user = User.objects.create_user(
				username = name,
				email = email,
				password = password,
			)
		else:
			print("No valid")
		return render(request, "login.html")

	else:
		return render(request, 'signup.html')