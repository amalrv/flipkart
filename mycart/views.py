from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"mycart/index.html")

def home(request):
    return HttpResponse('welcome')

def face(request):
    return render(request,"mycart/face.html")

def baabtra(request):
    return render(request,"mycart/baabtra.html")


def about(request):
    return render(request,"mycart/about.html")


def contact(request):
    return render(request,"mycart/contact.html")


def viewpage(request):
    return render(request,"mycart/viewpage.html")