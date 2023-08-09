from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def lesson_4(requests):
    return HttpResponse("«Домашка по 4 занятию»")