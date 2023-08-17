from django.shortcuts import render
from .models import Advertisement

# Create your views here.
from django.http import HttpResponse

def example(request):
    # return HttpResponse("hi welcome")
    advertisements= Advertisement.objects.all()
    
    # print(advertisements)
    context = {"name": "exampleeee", "name1": "exampleeee1", "name3":["dfdf1", "sdfsdf2", ["dasa0","sada1"]], "advertisements":advertisements}
    return render(request, 'index.html', context)

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
    advertisements= Advertisement.objects.all()
    
    # print(advertisements)
    context = {"name": "exampleeee", "name1": "exampleeee1", "name3":["dfdf1", "sdfsdf2", ["dasa0","sada1"]], "advertisements":advertisements}
    print (context)
    return render(request,'adv.html',context)


