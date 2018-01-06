from __future__ import unicode_literals
from . models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from . models import profile
from . models import login
from . models import create

# Create your views here.
def index(request):
    return render(request,'exam/logreg.html')

def registration(request):
    print request.POST
    errs = User.objects.validate_registration(request.POST)
    if errs:
         for e in errs:
             messages.error(request, e)
    else:
        new_user = User .objects.create_user(request.POST)
        request.session['id'] = new_user.id
    return redirect('/index.html')

def login(request):
    print request.POST
    return redirect('/index.html')

def create(request):
    print request.POST
    errors = User.objects.create_user(request.POST)
    if errors:
        for err in error:
            error(request, err)
    else:
        User.objects.get(
             name=request.POST['name'],
             alias=request.POST['alias'],
             email_address=request.POST['email'],
             poke_history=request.POST['poke']
        )
    return render(request,'exam/create.html')

def formView(request):
    if request.session.has_key('username'):
      username = request.session['username']
      return render(request, 'create.html', {"username" : username})

    else:
        return render(request, 'logreg.html', {})
        messages.poke(request, "Welcome, {}! {} people poked you!".format(new_user.username))
        return render(request, 'exam/list.html', context)

def delete(request, user_id):
    User.objects.get(id=username).delete()
    return redirect('/')
