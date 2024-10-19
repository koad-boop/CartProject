from django.shortcuts import render,redirect
from .forms import admin_form
from .models import Category,Product,Admin
import os
from django.core.mail import send_mail,EmailMessage
from django.conf import settings

# Create your views here.
def index(request):
    if request.method=='POST':
        fm=admin_form(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            phone = fm.cleaned_data['phone']
            fm.save()
            obj=Admin(name=name,email=email,phone=phone)
            obj.save()
            return redirect('/')
    fm=admin_form   
    return render(request,'adminn/index.html',{'fm':fm})

def login(request):
    return render(request,'adminn/login.html')

def dashboard(request):
    return render(request,"adminn/dashboard.html")

def addproduct_view(request):
    if request.method=="POST":
        pname=request.POST.get('name')
        price=request.POST.get('price')
        cat=request.POST.get('category')
        des=request.POST.get('des')
        img=request.FILES['imag']
        print(img)
        cobj=Category.objects.get(id=cat)
        pobj=Product(name=pname,price=price,category=cobj,des=des,image=img)
        pobj.save()
        return redirect('/viewproduct/')
    cats=Category.objects.all()
    return render(request,"adminn/addproduct.html",{'cats':cats})

def viewproduct_view(request):
    prods=Product.objects.all()
    return render(request,'adminn/viewproduct.html',{'prods':prods})

def addcategory_view(request):
    if request.method=="POST":
        cname=request.POST.get('name')
        des=request.POST.get('des')
        cobj=Category(name=cname,des=des)
        cobj.save()
    return render(request,"adminn/addcategory.html")

def deleteproduct_view(request,id):
    rec=Product.objects.get(id=id)
    rec.delete()
    os.remove(rec.image.path)
    return redirect('/viewproduct/')

def edit_view(request,id):
    p=Product.objects.get(id=id)
    if request.method == "POST":
        pname=request.POST.get('name')
        price=request.POST.get('price')
        cat=request.POST.get('category')
        des=request.POST.get('des')
        img=request.FILES['imag']
        
        #remove old image
        #if p.image:
            #if os.path.isfile(p.image.path):
                #os.remove(p.image.path)    
        cobj=Category.objects.get(id=cat)
        #Product.objects.filter(id=id).update(name=pname,price=price,category=cobj,#des=des,image=img)
        pobj=Product(id=id,name=pname,price=price,category=cobj,des=des,image=img)
        pobj.save()
        prods= Product.objects.all()
        return render(request, 'adminn/viewproduct.html',{"prods":prods})
    cats=Category.objects.all()
    return render(request,'adminn/p_edit.html',{"p":p,'cats':cats})



def email(request):
    return render(request,'adminn/mail.html')

def send_email(request):
    subject='Acount Update'
    message='this is from django server'
    from_email=settings.EMAIL_HOST_USER
    recipient_list=['ekansh7376@gmail.com']
    file_path=f'{settings.BASE_DIR}/hi.txt'
    #send_mail(subject,message,from_email,recipient_list)
    mail=EmailMessage(subject=subject,body=message,
    from_email=from_email,to=recipient_list)
    mail.attach_file(file_path)
    mail.send()
    return redirect('/')

def formforotp(request):
    if request.method=='POST':
        mail=request.POST.get('email')
        
    return render(request,'adminn/formfor_otp.html')

def otp(request):
    return render(request,'adminn/otp.html')



