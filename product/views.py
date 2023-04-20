from django.shortcuts import render,HttpResponse
from .models import item


# Create your views here.
def home(request):
    products = item.objects.all()
    a = request.POST.get('psearch')
    print(a)
    return render(request,'home.html',{'products':products})
def detail(request):
    return render (request,'details.html')
def login(request):
    return render (request,'login.html')