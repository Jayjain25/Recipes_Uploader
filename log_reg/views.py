from django.shortcuts import *
from add_receipes.models import * 
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout

def Login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)
        if user.exists():
            pass
        else:
            messages.error(request,'Invalide username')
            return redirect('/login/')
        
        user = authenticate(username = username , password = password)

        if user == None:
            messages.error(request,"Invalid Password")
            return redirect("/login/")

        else:
            login(request,user)
            return  redirect('/landpage/')

    return render(request , 'login.html')


def Logout_page(request):
    logout(request)
    return redirect('/login/')



def Register_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # to check user exits or not
        user = User.objects.filter(username = username)
        if user.exists():
            messages.error(request, "UserName Alredy Exists.")
            return redirect('/register/')

        user = User.objects.create(
            first_name = first_name ,
            last_name = last_name,
            username = username,
        )

        user.set_password(password)
        user.save()
        messages.info(request,"Acount Created Succesfully")
        return redirect('/register/')
    return render(request , 'register.html')

# Create your views here.
