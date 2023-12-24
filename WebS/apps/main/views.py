from threading import Thread

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth.decorators import login_required

from WebS.apps.main.apps import MainConfig
from WebS.apps.main.tasks import update_prices


def index(request):
    return render(request, 'main/index.html')


@login_required(login_url='login')
def about(request):
    return HttpResponse('<h1>about</h1>')


def to_do_app(request):
    return HttpResponse('<h1>abouqqwet</h1>')