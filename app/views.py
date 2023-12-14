from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def display_topic(request):
    
    return render(request,'display_topic.html')

def display_webpage(request):

    return render(request,'display_webpage.html')