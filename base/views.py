from django.shortcuts import render
from django.http import HttpResponse
from .models import Network

# Create your views here.

def home(request):
    #return HttpResponse('Home page')
    return render(request, "home.html")

def networks(request):
    #return HttpResponse('Second page')
    networks = Network.objects.all()
    context = {'networks': networks}
    return render(request, "networks.html", context)
