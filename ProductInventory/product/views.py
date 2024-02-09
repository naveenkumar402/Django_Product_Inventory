from django.shortcuts import render,redirect
from .models import Products

# Create your views here.
def addproduct(request):
    if request.method =='POST' :
        product_name=request.POST.get('product_name')
        price=request.POST.get('price')
        category=request.POST.get('category')
        email=request.POST.get('email')
        if Products.objects.filter(product_name=product_name).exists():
             return render(request, 'add_product.html', {'error_message': 'Product already exists'})
        Products.objects.create(product_name=product_name,price=price,category=category,email=email)
        return redirect('viewproduct')
    

    return render(request,'add_product.html')
def viewproduct(request):
    products=Products.objects.all()
    return render(request, 'view_Products.html', {'Products': products})


def deleteproduct(request,id):
    products = Products.objects.get(id=id)
    if request.method == 'POST':
        products.delete()
        return redirect('viewproduct')  
    return render(request, 'delete_product.html', {'Products': products})


def showproduct_price_exceed_20000(request):
    products=Products.objects.all()
    for product in products:
        if product.price > 20000:
            return render(request ,'view_products1.html',{'Products':product})
    return products


def updateproduct(request,id):
    product = Products.objects.get(id=id)
    if request.method == 'POST':
        product.product_name = request.POST.get('product_name')
        product.price = request.POST.get('price')
        product.category = request.POST.get('category')
        product.email = request.POST.get('email')
        product.save()
        return redirect('viewproduct')
    return render(request, 'edit_product.html', {'product': product})
    