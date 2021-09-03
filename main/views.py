from django.shortcuts import render,redirect
from .models import customer
from .models import product

# Create your views here.
def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        custs=customer.objects.all()
        for cust in custs:
            if email==cust.email:
                if password==cust.password:
                    prods=product.objects.all()
                    return redirect('products')

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
    prods=product.objects.all()
    return render(request,"products-view.html",{'prods':prods})

def buy(request):
    return render(request,"buy.html")


def success(request):
    if request.method=='POST':
        return render(request,"success.html")

