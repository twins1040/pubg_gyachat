from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("hello, victims! I will goso hack user")

def searchPlayer(request, playerName):
    response = "You're looking at the result %s."
    return HttpResponse(response % playerName)

