from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from . import models

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as log_in, authenticate, logout
# Create your views here.
def index(request):
    return render(request,"scamBlastR/base.html",{} )

# return render(request, 'polls/index.html', context) instead of httpReponse
@login_required(login_url ="/login/")
#@login_required()
def home(request):
# if request.user.is_authenticated:
    print(request)
    if request.method == "POST":
       logout(request)
       return render(request,"registration/logout.html",{})

    context ={"context":  models.Post.objects.all() }
    context["username"] = request.user.username
#    for q in context: 
#        print(q.post_content)
#  for comment in q.comments_set.all():
#            print("      " + comment.comment_content)
    return render(request, "scamBlastR/home.html",context )
#else:
#return HttpResponse("you are not login buddy!")

    
# This view lets users login into the site. Note all pages that that requires
# login need to redirect unauthenticated user to this page in order to access
# the content of the site.
def login(request):
    print(request)
    context = {}
    if request.method == "GET" : 
        print("I'm inside the GET Request")
        context.update({"username": "Username", "password": "Password",
                "error_msg": "" })
        
        context["next"] = request.GET.get("next")
        return render(request,"registration/login.html",context)
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username =username, password = password)
        
        if user != None and user.is_active : 
            log_in(request,user)        
            print("you been loggin ")
            return redirect("/home/")
        else:
            print("bad username or password")
            context["error_msg"] = "Try Again: Bad username or password" 
            context["username"] = request.POST.get("username")
            context["password"] = request.POST.get("password")
            context["next"] = request.POST.get("next")
            return render(request,"registration/login.html",context )
        return HttpResponse(" This is the login page boy!")
