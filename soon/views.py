from django.shortcuts import render,HttpResponse
from soon.models import Index

# Create your views here.

def index(request):
    if request.method =="POST":
        email=request.POST['email']
        index=Index(email=email)
        index.save()
    return render(request, 'index.html')