from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from moviesapp.forms import Movieform
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def profile(request):
    return render(request,"profile.html")


def signup(request):
        if request.method == 'POST':
            username = request.POST['username']
            first_name = request.POST['first_name']
            email = request.POST['email']
            last_name = request.POST['last_name']
            password = request.POST['password']
            c_password = request.POST['c_password']
            if password == c_password:
                if User.objects.filter(username=username).exists():
                    messages.info(request, "Username exists.")
                    return redirect('profilesapp:signup')
                elif User.objects.filter(email=email).exists():
                    messages.info(request, "Email exists.")
                    return redirect('profilesapp:signup')
                else:
                    user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                    email=email, password=password)
                    user.save();
                    return redirect('profilesapp:login')
            else:
                messages.info(request, "Both passwords not matching")
                return redirect('profilesapp:signup')
            return redirect('profilesapp:signup')
        return render(request, "signup.html")

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return render(request,"profile.html")
        else:
            messages.info(request,"Invalid Credentials.")
            return redirect('profilesapp:login')
    return render(request,"login.html")

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('profilesapp:login')
