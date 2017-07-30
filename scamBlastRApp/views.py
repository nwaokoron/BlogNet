from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from . import models

from django.contrib.auth.decorators import login_required
# Create your views here.
# return render(request, 'polls/index.html', context) instead of httpReponse
#@login_required(login_url ='/login/')
@login_required()
def home(request):
    if request.user.is_authenticated:
        context ={'context':  models.Posts.objects.all() }
#    for q in context: 
#        print(q.post_content)
#  for comment in q.comments_set.all():
#            print("      " + comment.comment_content)
        return render(request, 'scamBlastR/home.html',context )


    
# This view lets users login into the site. Note all pages that that requires
# login need to redirect unauthenticated user to this page in order to access
# the content of the site.
def login(request):
    context = {}
    if request.method == "GET" : 
        context.update({'username': 'Username', 'password': 'Password' })
        render(request,'registration/login.html',context)
    elif request.method == "POST":
        return HttpResponse(" This is the login page boy!")
