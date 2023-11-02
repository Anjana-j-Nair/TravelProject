from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.shortcuts import redirect

# Create your views here.
#for login
def login(request):
    if request.method=='POST':
        u=request.POST['username']
        p=request.POST['Password']
        user=auth.authenticate(username=u,password=p)#first is db username
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid")
            return redirect('login') #html file name
    return render(request,'login.html')
#for registration
def reg(request):#fetching builtin table
    if request.method=='POST':
        uname=request.POST['username']#first on is object name second one is form field name
        fname=request.POST['First name']
        lname=request.POST['Last name']
        email=request.POST['Email']
        pwd=request.POST['Password']
        cpwd=request.POST['Confirm']
        if cpwd==pwd:#this is user for confirm password
            if User.objects.filter(username= uname).exists(): 
                 messages.info(request, "Username is taken")
                 return redirect('reg')
            elif User.objects.filter(email = email).exists():  # checking it is same
                messages.info(request, "email is taken")
                return redirect('reg')
            else:
                obj=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=pwd)#first is db username
                obj.save()
                return redirect('login')
        else:
            messages.info(request,"Password is not matching")
            return redirect('reg')
        return redirect('/')
    return render(request,'reg.html')
#for log out
def logout(request):
    auth.logout(request)
    return redirect('/')
