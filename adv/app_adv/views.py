from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def example(request):
    # return HttpResponse("hi welcome")
    return render(request, 'index.html')

def top_sellers(request):
    return render(request, 'topsellers.html')

def profile(request):
    return render(request,'profile.html')

def login(request):
    return render(request,'login.html')
def register(request):
    return render(request,'register.html')
def advpost(request):
    return render(request,'advpost.html')
def adv(request):
    return render(request,'adv.html')


