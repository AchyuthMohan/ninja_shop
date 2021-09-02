from django.shortcuts import render,redirect
from .models import customer

# Create your views here.
def login(request):
    return render(request,"login.html")
def register(request):
    if request.method=='POST':
        email=request.POST['email']
        name=request.POST['name']
        address=request.POST['address']
        address2=request.POST['address2']
        password=request.POST['password']
        state=request.POST['state']
        city=request.POST['city']


        c=customer(email=email,name=name,address=address,address2=address2,password=password,state=state,city=city)
        c.save();
        return redirect('/')
    else:
        return render(request,"register.html")

def products(request):
    if request.method=="POST":
        return render(request,"products-view.html")
