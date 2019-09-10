from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.validators import URLValidator
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
    quiz = None
    projet = None
    try:
        quiz = Quiz.objects.filter(groupe_quiz = request.user.profile.groupe, date = today)[:1].get()
        is_quiz = True
    except:
        is_quiz = False

    try:
        projet = Projet.objects.filter(groupe_projet = request.user.profile.groupe, date_debut__lte = today, date_fin__gte = today)[:1].get()
        is_projet = True
    except:
        is_projet = False
    print(projet)
    data = {
            'quiz':quiz,
            'projet':projet,
            'is_quiz':is_quiz,
            'is_projet':is_projet,
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
    quiz = None
    projet = None
    
    try:
        projet = Projet.objects.filter(groupe_projet = request.user.profile.groupe, date_debut__lte = today, date_fin__gte = today)[:1].get()
        is_projet = True
    except:
        is_projet = False
    print(projet)
    data = {
            
            'projet':projet,
           
            'is_projet':is_projet,
        }
    return render(request, 'specialisation/pages/project.html', data)

@login_required(login_url='/connexion')
def myquiz(request):
    quiz = None

    try:
        quiz = Quiz.objects.filter(groupe_quiz = request.user.profile.groupe, date = today)[:1].get()
        is_quiz = True
    except:
        is_quiz = False
    
    ## Tratement de quiz
  

    quest_1 = request.POST.get('qr-'+str(1)+'', False)
    quest_rad = request.POST.get('radio-group-1', None)
    quest_check = request.POST.getlist('check1[]')
    # print(quest_1)
    # print(quest_rad)
    print(quest_check)
    if quest_check:
        #for item in quest_check:
        print(quest_check)
        print(len(quest_check))
    


    data = {
            'quiz':quiz,
            'is_quiz':is_quiz,
            
        }

    return render(request, 'specialisation/pages/quiz.html', data)


@login_required(login_url='/connexion')
def myresultat(request):
    return render(request, 'specialisation/pages/resultat.html')


def quizresult(request):
    return render(request, 'specialisation/pages/quizresult.html')