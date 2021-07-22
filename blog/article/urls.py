from django.urls import path
from . import views

# This file is made by me

urlpatterns = [
    path('', views.article, name="article_list"),
    path('comment/', views.comment),
    path('create/', views.create_article),
    path('<slug:slug>/', views.article_details),
]