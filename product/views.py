from django.shortcuts import render
from .models import item


# Create your views here.
def home(request):
    products = item.objects.all()
    return render(request,'home.html',{'products':products})
