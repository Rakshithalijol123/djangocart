from django.shortcuts import render,redirect
from django .http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Registration
from django.core.mail import send_mail
import random
from django.conf import settings
from googlevoice import voice
from googlevoice.util import input
# Create your views here.

def signin(request):
    if request.method == "POST":
        sname = request.POST.get('sname','')
        semail = request.POST.get('semail','')
        smbno = request.POST.get('smbno','')
        spass1 = request.POST.get('spass1','')
        spass2 = request.POST.get('spass2','')

        if sname == '':
            messages.error(request,'Username can\'t be empty')
            return redirect('/accounts/signin/')
        if semail == '':
            messages.error(request,'E-mail can\'t be empty')
            return redirect('/accounts/signin/')
        if spass1 == '':
            messages.error(request,'Password can\'t be empty')
            return redirect('/accounts/signin/')
        if spass1 == spass2:
            get_email = User.objects.filter(email=semail)
            if len(get_email) == 0:
                get_name = User.objects.filter(username=sname)
                if len(get_name) == 0:
                    user = User.objects.create_user(username=sname,email=semail,password=spass1)
                    add_user_mbno = Registration.objects.create(user=user,no=smbno)
                    add_user_mbno.save()
                    otp = random.randint(1000,9999)
                    msg = f"Your OTP for verifying MyCart is {otp}"
                    request.session["email_otp"] = otp
                    send_mail("Email verification OTP",msg,settings.EMAIL_HOST_USER,[semail],fail_silently=False)
                    messages.success(request,"Varify your no to confirm your account")
                    return render(request,'otp.html',{'semail':semail})
                else:
                    messages.error(request,"Username already taken")
                    return redirect('/accounts/signin/')

            else:
                messages.error(request,'Email already taken')
                return redirect('/accounts/signin/')
        else:
            messages.error(request,'password mismatches')
            return redirect('/accounts/signin/')
    else:
        return render(request,'signin.html')

def otp(request,gmail):

    # get_detials = Registration.objects.filter(no=no)
    # get_user = Registration.objects.filter(user=get_detials[0].user)
    if request.method == "POST":
        read_otp = int(request.POST.get('otp',''))
        get_otp = request.session["email_otp"]
        if read_otp == '':
            messages.error(request,"OTP feild cannot be empty")
            return redirect(f"/accounts/otp/{gmail}/")
        else:
            if get_otp == read_otp:
                messages.success(request,"You successfully joined MyCart family")
                return redirect('/accounts/login/')
            else:
                delete_user = User.objects.filter(email=gmail)
                delete_user[0].delete()
                messages.error(request,'You entered wrong OTP Pls signin again')
                return redirect("/accounts/signin/")

def login(request):
    if request.method == "POST":
        lname = request.POST.get("lname",'')
        lpass = request.POST.get("lpass",'')
        # print(f"the user entered otp is {lemail}\n")
        # print(f"the session otp is {lpass}\n")
        if lpass == '':
            messages.error(request,"Please enter your password")
            return redirect("/accounts/login/")
        if lname == '':
            messages.error(request, "Please enter your registered E-Mail")
            return redirect("/accounts/login/")
        user = auth.authenticate(username=lname,password=lpass)
        print(user)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.error(request,"Please enter your proper details")
            return redirect("/accounts/login/")

    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
