import re
from django.shortcuts import render

# Create your views here.

def home(request):
    '''
    this will render/display 
    https:127.0.0.1:8000/home/
    '''
    return render(request,'home.html',{})