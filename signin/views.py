from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def HomeView(request):
  return render(request,'signin/home.html')

def SigninView(request):
  if request.method == 'POST':
    username = request.POST['username']
    pass1 = request.POST['password1']
    user = authenticate(username=username,password=pass1)

    if user is not None:
      login(request,user)
      fname = user.username
      return render(request,'signin/home.html',{'fname':fname})
    else:
      messages.error(request,'error')
      return redirect('home')
  return render(request,'signin/index.html')

def Sign_out(request):
  if request.method == 'GET':
    logout(request)
    messages.success(request,"Logged out Successfully")
    return redirect('home')


  

def SignupView(request):
  if request.method == 'POST':
    username = request.POST['username']
    email = request.POST['email']
    pass1 = request.POST['password1']
    pass2 = request.POST['password2']

    if User.objects.filter(username=username):
      messages.error(request,"Username already exist! Please try some other username")
      return redirect('home')
    # if User.objects.filter(email=email):
    #   messages.error(request)
    myuser = User.objects.create_user(username=username, email=email, password=pass1)
    myuser.save()
    messages.success(request,"Your Account has been succesfully created")
    return redirect('signin')
  return render(request,'signin/index2.html')