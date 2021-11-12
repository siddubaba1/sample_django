from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index (request):
          return  render(request,"hades/new.html")

def gelos(request):
          return HttpResponse("sup")

def rufus(request):
          return HttpResponse("hoja,bc!")


def greet(request,name): 
          return render(request,"hades/greet.html",
          {
               "name":name.capitalize()
          } )