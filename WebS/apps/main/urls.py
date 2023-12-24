from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name="about"),
    path('to_do_app/', views.to_do_app, name="to_do_app"),
]

