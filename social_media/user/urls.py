from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home_page"),
    path('<int:pk>', views.delete_view),
    path('<str:username>', views.profile_view)
]
