from django.shortcuts import render,redirect
from.models import User
from django.contrib import messages

# Create your views here.
def dashboard(request):
    return render (request, 'admins/dashboard.html')

def signup(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name =request.POST.get('last_name')
        school_name =request.POST.get('school_name')
        password = request.POST.get('password')
        password1 =request.post.get('password1')
        recovery_code =request.post.get('recovery_code')
        if password != password1:
            if User.objects.filter(recovery_code=recovery_code).exists():
                messages.error(request, 'recovery code alrealdy exist')
                return redirect('signup')
            else:
               User.objects.create_user(first_name=first_name,last_name=last_name ,school_name=school_name,password=password)
               return redirect('login')
            

        else:
            messages.error(request, 'password do not match')
            return redirect('signup')
               

    return render (request, 'admins/signup.html')

def login(request):
    return render (request,'admins/login.html')
