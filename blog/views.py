from django.shortcuts import render,redirect
from  django.http import HttpResponse
from .models import BlogPost,Contact_us
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login ,logout



def index(request):
    blogger = BlogPost.objects.all()
    return render(request,'bloghome.html',{'mypost':blogger})

def blogpost(request,id):
    post = BlogPost.objects.filter(post_id = id)[0]
    return render(request,'blogpost.html',{'vlog':post})

def blogaboutus(request):
    return render(request,'blogaboutus.html')

def contact_us(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('contactemail', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact_us(name=name, email=email, phone=phone, description=desc)
        contact.save()
        messages.success(request,'YOur query is successfully submitted to us , we will contact you shortly.')
    return render(request, 'contact_us.html')

def handlesignup(request):
    if request.method=="POST":
        email = request.POST['email']
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        myuser= User.objects.create_user(username ,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,"Congratatulations , You have successfully register to our website")
        return redirect('blog_homepage')
    else:
        return HttpResponse("error")


def handlelogin(request):
    if request.method=='POST':
        loginusername = request.POST['loginusername']
        loginPassword = request.POST['loginPassword']

        user = authenticate(username=loginusername,password=loginPassword)
        if user is not None:
            login(request,user)
            messages.success(request,'Successfully Logged In ')
            return redirect('base_homepage')
        else:
            messages.error(request,' Invalid Credentials, please try again...')
            return redirect('base_homepage')

def handlelogout(request):
     logout(request)
     messages.success(request,'Successfully Logged Out')
     return redirect('base_homepage')

def search(request):
    query = request.GET['query']
    if len(query) > 60:
        mypost = BlogPost.objects.none()
    else:
        myposttitle = BlogPost.objects.filter(post_title__contains=query)
        mypostdescription = BlogPost.objects.filter(description__contains=query)
        mypost = myposttitle.union(mypostdescription)

    if mypost.count()==0:
        messages.warning(request,"NO search result found . Please refine your query.")
    else:
        messages.success(request,"Search result found.")
    params ={'mypost': mypost,'query': query}

    return render(request,'searched.html',params)