from django.shortcuts import render
from MainViewController.models import MainViewController
# Create your views here.
def home(request):
    context = {}
    template = 'home.html'
    return render(request, template, context)