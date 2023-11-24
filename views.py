from django.shortcuts import render
from django.http import HttpResponse
from .models import Rooms


def index(request):
    #return HttpResponse("<h4>Hello</h4>")
    return render(request, 'main/index.html')

def about(request):
    return HttpResponse("<h4>About</h4>")


