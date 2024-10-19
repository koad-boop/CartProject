
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Customer
from cart_admin.models import Product,Category,Cart
import os
from django.core.mail import send_mail,EmailMessage
from django.conf import settings
import random
# Create your views here.

def fetch_instance(product,cust_id):
    print(product,cust_id)
    
    pro_instance = Product.objects.get(id=product)
    cust_instance = Customer.objects.get(id=cust_id)
    return (pro_instance,cust_instance)
    
def index(request):
    if request.method=="POST":
        pid=request.POST.get('addproduct')
        
        cust_id=request.session.get('cust_id')
        prods=Product.objects.filter(id__in=pid)

        if pid:
            pro_instance,cust_instance = fetch_instance(pid,cust_id)
            cart_obj = None
            

            try:
                cart_obj = Cart.objects.get(pro_id=pro_instance,cust_id=cust_instance)
            except:
                pass
            if cart_obj==None:
                Cart(pro_id=pro_instance,cust_id=cust_instance).save()
            else:
                if request.POST.get("remove"):
                    if cart_obj.quantity == 1:
                        cart_obj.delete()
                    elif cart_obj.quantity > 1:
                        cart_obj.quantity -= 1
                        cart_obj.save()
                else:    
                    cart_obj.quantity += 1
                    cart_obj.save()
                  
    cid=request.GET.get('category')
    if cid:
        prods=Product.objects.filter(category=cid)
    else:
        prods=Product.objects.all()   
    cats=Category.objects.all()
    data={'prods':prods,'cats':cats}
    return render(request,"customer/index.html",data)

def cart_view(request):
    i=request.session.get('cust_id')
    p_result=Cart.objects.filter(cust_id_id=i).values()
    pro_id_list = [item['pro_id_id'] for item in p_result]
    products=Product.objects.filter(id__in=pro_id_list)
    quantities_dict = {item['pro_id_id']: item['quantity'] for item in p_result}
    print(products)
    print(quantities_dict,'=======')

    context = {
        'products': products,
        'quantities_dict': quantities_dict,
    }
    

    return render(request, 'customer/cart.html',context)

       
    

    

def signup_view(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        father=request.POST.get('father')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        phone=request.POST.get('phone')
        img=request.FILES['imag']
        if pass1==pass2:
            cobj=Customer(fname=fname,lname=lname,father=father,email=email,pass1=pass1,phone=phone,image=img)
            cobj.save()
            return redirect('/')
        
        
    
        
        
        else:
            return HttpResponse("Password did not match")   
    return render(request,"customer/signup.html")

def userlogin_view(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        upass=request.POST.get('password')
        cust=Customer.objects.get(email=uname)   
        if cust:
            if uname==cust.email and upass==cust.pass1:
                request.session['cust_id']=cust.id
                request.session['cust_name']=cust.fname
                request.session['cust_email']=cust.email
                return redirect('/')
        else:
            pass
    return render(request,"customer/login.html")

def profile(request):
       cust_id=request.session.get('cust_id')
       if cust_id:
            cust = Customer.objects.get(id=cust_id)
            return render(request,"customer/profile.html",{'cust':cust})
    
def logout_view(request):
    request.session.clear()
    return redirect('/')

def fpf(request):
    if request.method=='POST':
        e=request.POST.get('userInput')
        cust = Customer.objects.all()
        emails = [customer.email for customer in cust]
        if e in emails:
            otp=random.randint(1377,9377)
            request.session['otp']=otp
            subject='OTP'
            message=f"Your otp is {otp} for KD login Please don't share with anyone"
            from_email=settings.EMAIL_HOST_USER
            recipient_list=['ekansh7376@gmail.com']
            send_mail(subject,message,from_email,recipient_list)
            return redirect('password_form/')
    return render(request,'customer/email.html')

def form_otp(request):
    if request.method=='post':
        o=request.POST.get('otp')
        otp=request.session.get('otp')
        if o==otp:
            return render(request,'customer/password_form.html')
        return HttpResponse("Invalid Otp")
    return render(request,'customer/otp.html')

def New_Password(request):
    return render(request,'customer/password_form.html')

def gindex(request):
    return render(request,'customer/gindex.html')
 
 