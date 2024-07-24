from argparse import OPTIONAL
import email
from itertools import product
from optparse import Option
import random
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
from django.shortcuts import redirect,render,get_object_or_404
from django.contrib.auth import authenticate,login
from labproject import settings
from django.core.mail import send_mail
from .models import Options, Userans, detail, order, register   #storing data in database customers
from django.contrib.auth.decorators import login_required


ppid=0

def index(request):
    return render(request,"index.html")

def signup(request):
    if request.method=="POST":
        
        username=request.POST.get('username')
        firstname=request.POST.get('fname')
        lastname=request.POST.get('lname')
         
        email=request.POST.get('email')
        dob=request.POST.get('dob') 
        password=request.POST.get('pass1')
        pass1=request.POST.get('pass2')

        if register.objects.filter(username=username) and register.objects.filter(email=email):
            messages.warning(request,"Account already exist, please Login to continue")
            redirect('signup')

        elif(len(username)<3):
            messages.warning(request,"Username Field must be greater than 3 character.")

        elif(len(password)<5):
            messages.warning(request,"Password should be more than 5 letters")

        elif(len(email)==0):
            messages.warning(request,"Email field can't be empty")

        elif password!=pass1:
            messages.warning(request,"Password is not equal")
            
        elif register.objects.filter(username=username):
            messages.warning(request,"username already exist")

        else:
            myuser=register.objects.create(username=username,firstname=firstname,lastname=lastname,dob=dob,email=email,password=password)
            myuser.save()
            
            #welcome the email
            subject="Welcome to CIEL"
            message="Hello "+ myuser.firstname + "!! \n" +"Welcome to CIEL!! n Thank you for visiting our website \n We Hope you have a great day.\n\n Thanking You"
            from_email= settings.EMAIL_HOST_USER 
            to_list=[myuser.email]
            send_mail(subject,message,from_email,to_list, fail_silently=True)

            messages.success(request,f'Account Created Successfully for {myuser.username}! \n please Login to continue')
            return render(request,'signin.html')

    else:
            redirect('signup')

    return render(request,"signup.html")

def signin(request):
    if request.method == "POST":
        email1=request.POST['email']
        passw1=request.POST['password']
        print(email1)

        if not len(email1):
            messages.warning(request,"Username field is empty")
            redirect('signin')
        elif not len(passw1):
            messages.warning(request,"Password field is empty")
            redirect('signin')
        
        else:
            register.objects.filter(email=email1)
            user=register.objects.filter(email=email1)[0]
            #print(user.password)
            password_hash=user.password
            #print("hash"+password_hash)
            if passw1==password_hash:
                res=1
                #print(res)
            else:
                res=0

            if res==1:
                request.session['email'] = email1
                return render(request,'welcme.html',{})
            else:
                messages.warning(request,"Email or password is incorrect")
                redirect('signin')

    else:
        redirect('signin')

    return render(request,'signin.html',{})

def welcme(request):
    return render(request,"welcme.html")


def logout(request):
   return render(request,"index.html")


def oorder(request):
    return render(request,'oorder.html')

def quiz(request):
    if request.method == "POST":
        username=request.POST.get('username')
        ans1=request.POST.get('ans1')
        ans2=request.POST.get('ans2')
        ans3=request.POST.get('ans3')
        ans4=request.POST.get('ans4')
        data=Userans.objects.create(qans1=ans1,qans2=ans2,qans3=ans3,qans4=ans4)
        data.save()

    
        info=Options.objects.filter(qans1=ans1,qans2=ans2,qans3=ans3,qans4=ans4).first()
        ppid=info.pid
        print(ppid)
        prdt=detail.objects.filter(pid=ppid)


        return render(request,'oorder.html',{'prdt':prdt})
    else:
        return render(request,'quiz.html')

def payment(request):
    if request.method=="POST":
        fullname=request.POST.get('fullname')
        email1=request.POST.get('email')
        address=request.POST.get('address')
        contact=request.POST.get('contact')
        
        orderno=random.randint(1000,2000)
        data=order.objects.create(fullname=fullname,contact=contact,address=address,email=email1,Orderno=orderno)
        data.save()

        return render(request,'confirm.html')

    else:   
        return render(request,'payment.html')



def confirm(request):
    return render(request,'welcme.html')


