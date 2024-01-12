from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request,'index.html')
def buttonpage(request):
    return render(request,"buttonpage.html")
def newpage(request):
    return render(request,"newpage.html")
def order(request):
    return render(request,'order.html')