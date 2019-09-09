from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from datetime import date, datetime, time



today = date.today()
print(today)
from .models import *


from .gestions.manager import Hello
# Create your views here.
def mylogin(request):
    username = request.POST.get('username', False)
    password = request.POST.get('password', False)

    next = request.POST.get('next', False)
    user = authenticate(username=username, password=password)
    
    if user is not None and user.is_active:
        print('connect user')
        login(request, user)

        if next: 

            return redirect(next)
        else:
            return redirect('homespe')
    else:
        return render(request, 'specialisation/login.html')

    
def deconnexion(request):
    logout(request)

    return redirect('mylogin') 


@login_required(login_url='/connexion')
def homespe(request):
    try:
        quiz = Quiz.objects.filter(groupe_quiz = request.user.profile.groupe, date = today)[:1].get()
        is_quiz = True
    except:
        is_quiz = False

    if is_quiz:

        data = {
            'quiz':quiz,
            'is_quiz':True
        }
    else:
        data = {
            'is_quiz':False
        }
    return render(request, 'specialisation/pages/index.html', data)

@login_required(login_url='/connexion')
def mygroupe(request):
    return render(request, 'specialisation/pages/groupe.html')

@login_required(login_url='/connexion')
def myprofile(request):
    return render(request, 'specialisation/pages/profil.html')

@login_required(login_url='/connexion')
def myproject(request):
    return render(request, 'specialisation/pages/project.html')

@login_required(login_url='/connexion')
def myquiz(request):
    return render(request, 'specialisation/pages/quiz.html')


@login_required(login_url='/connexion')
def myresultat(request):
    return render(request, 'specialisation/pages/resultat.html')
