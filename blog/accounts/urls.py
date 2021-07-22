from django.urls import path
from . import views

# This file is made by me

urlpatterns = [
    path('', views.signup_view),
    path('login/', views.login_view, name="login_view"),
    path('logout/', views.logout_view),
]