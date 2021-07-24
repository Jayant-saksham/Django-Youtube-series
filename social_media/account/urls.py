
from django.urls import path
from . import views

urlpatterns = [
    path('', views.sigup_view, name="sigup_page"),
    path('login/', views.login_view, name="login_page")
]
