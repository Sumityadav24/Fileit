from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Image
from .forms import ImageForm

# Create your views here.

def HandleSignUp(request):
 
    if request.method == "POST":
        username = request.POST.get('name')
        password = request.POST.get('pass')
        email = request.POST.get('email')    
        user = User.objects.create_user(username, email, password)   
        user.save()
        return redirect('login')
    else:
        messages.info(request,"Username already exists!")
    return render(request, 'myapp/signup.html',)


def HandleLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('upload')
        else:
            messages.info(request, 'Username or Password is incorrect') 
    return render(request, 'myapp/login.html')

def HandleLogout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/login/')
def HandleUpload(request):
    user=User()
    if user.is_authenticated:
        if request.method == "POST":
            fm = ImageForm(request.POST, request.FILES)
            # files = request.FILES.getlist('img')
            if fm.is_valid():
                # for i in files:
                   fm.save()
        form = ImageForm()
        img = Image.objects.all()
        return render(request, 'myapp/upload.html', {"form": form, 'img': img})
    else:
        return render(request, 'myapp/login.html',)
