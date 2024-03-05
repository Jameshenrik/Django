from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello darkness my old friend")

def about(request):
    return HttpResponse("I've come to speak with you again")