from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hi, from Karlovy Vary to the Poland ..oh, .... to the Prague ;-D")
