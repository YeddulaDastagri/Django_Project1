from django.shortcuts import render

# Create your views here. 
from diango.http import HttpResponse  
def nikki(request):
    return HttpResponse('nikki is good girl')
