from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Users
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from blog.models import Blog

def index(request):
    if request.user.is_authenticated:
        if request.user.usertype == 'Doctor':
            return render(request,'doctor_home.html',{"user":request.user})
        else:
            return render(request,'patient_home.html',{"user":request.user})
    else:
        return redirect("/login/")

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name').split(" ")
        email = request.POST.get("email")
        address = request.POST.get("Adress")
        city = request.POST.get("city")
        state = request.POST.get("state")
        pincode = request.POST.get("pincode")
        username = request.POST.get("Username")
        usertype = request.POST.get("usertype")
        password = request.POST.get("pass")
        repassword = request.POST.get("re_pass")
        if password != repassword:
            messages.error(request, "Passwords do not match")
            return redirect("/signup/")
        if Users.objects.filter(username=username):
            messages.error(request, "Username already exists")
            return redirect("/signup/")
        
        try:
        
            Users.objects.create_user(
                first_name=name[0],
                last_name=name[1],
                email=email,
                address=address,
                city=city,
                state=state,
                pincode=pincode,
                username=username,
                usertype=usertype,
                password=password  
            )
            messages.success(request, "Registration successful! You can now log in.")
        except Exception as e:
            messages.error(request,e)
        return redirect("/login/")
    return render(request,'signup.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('password')        
        user = authenticate(request=request,username=username, password=password)
        if user :
            login(request, user)
            # messages.error(request, "Logouted successfuly!.")
            return redirect("/")
        else:
            # messages.error(request, "Invalid Username or Password")
            return redirect("/login/")
    return render(request,'login.html')
        

def logout_user(request):
    logout(request)
    return redirect("/login")


def blogs(request):
    allBlogs = Blog.objects.filter(uploaded = True)
    categories = allBlogs.values('category').distinct()
    
    return render(request,'blogDisplay.html',{"blogs":allBlogs,"category":categories})

def readBlog(request,id):
    blog = Blog.objects.filter(id=id).first()
    return render(request,"readBlog.html",{'blog':blog})

def selfblogs(request):
    allBlogs = Blog.objects.filter(doc_id=request.user.id,uploaded=True)
    return render(request,'blogDisplay.html',{"blogs":allBlogs})


