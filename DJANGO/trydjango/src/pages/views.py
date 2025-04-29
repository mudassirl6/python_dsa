from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def homepage_view(request,*args, **kwargs):
    print(args,kwargs)
    print(request.user)
    
    
    # return HttpResponse("<h1> Hello World</h1>")
    return render(request,"home.html",{})
    
    
def contact_page(request,*args,**kwargs):
    return render(request,"contact.html",{})

def about_page(request,*args,**kwargs):
    myContext = {"my_text":"This is about us",
                 "mynumber":123,
                 "mylist":[1,2,3,4]}
    
    return render(request,"about.html",myContext)

def social_page(request,*args,**kwargs):
    return render(request,"social.html",{})