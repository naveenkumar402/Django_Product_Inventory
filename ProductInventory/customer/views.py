from django.shortcuts import render , redirect
from .models import Customer
# Create your views here.
def addcustomer(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        state=request.POST.get('state')
        country=request.POST.get('country')
        if not Customer.objects.filter(email=email).exists :
            Customer.objects.create(name=name,email=email,mobile=mobile,state=state,country=country)
            return redirect('viewcustomer')
        return render(request,'add_customer.html',{'error_message': 'Email already exists'})        
    return render(request,'add_customer.html')
def viewcustomer(request):
    customer = Customer.objects.all()
    return render(request, 'view_customer.html', {'customer': customer})
def deletecustomer(request,id):
    customer= Customer.objects.get(id=id)
    if request.method == 'POST':
        customer.delete()
        return redirect('viewcustomer')  
    return render(request, 'delete_customer.html', {'customer': customer})