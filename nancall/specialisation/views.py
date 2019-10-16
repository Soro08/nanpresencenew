from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.validators import URLValidator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse

from datetime import date, datetime, time



today = date.today()
print(today)
from .models import *
from presence.models import Nangroupe

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
    if is_projet == False:
        return redirect('homespe')
    print(projet)
    data = {
            
            'projet':projet,
           
            'is_projet':is_projet,
        }
    return render(request, 'specialisation/pages/project.html', data)

@login_required(login_url='/connexion')
def myquiz(request):
    quiz = None
    nbquestion = 0
    questions_list = []
    try:
        quiz = Quiz.objects.filter(groupe_quiz = request.user.profile.groupe, date = today)[:1].get()
        for quest in quiz.questionquiz.all():
            questions_list.append(quest.pk)
        print(questions_list)
        nbquestion = Question.objects.filter(quiz = quiz).count()
        
        is_quiz = True
    except:
        is_quiz = False

        
    if is_quiz == False:
        return redirect('homespe')
    
    ## Tratement de quiz
    note_user = 0
    for i in questions_list:
        print(i)
        
        quest_1 = request.POST.get('qr-'+str(i)+'', False)
        quest_rad = request.POST.get('radio-group-'+str(i)+'', None)
        quest_check = request.POST.getlist('check-'+str(i)+'[]')
        if quest_check:
            #for item in quest_check:
            print(quest_check)
            print(len(quest_check))
        if quest_1:
            #qr_pk = quest_1.replace('qr-', '')
            #reponse_q_r = Reponse.object.get(pk = quest_1)
            pass
        if len(quest_check) > 0:
            rep_chek_box = Reponse.objects.filter(question_resp__quiz__pk = quiz.pk, question_resp__type_question__pk = 3, statut =True).count()
            print("reponse corecte :" , rep_chek_box)
            if rep_chek_box == len(quest_check):
                is_vois = True
            else:
                is_vois = False

            if is_vois:
                trouver_chek = 0
                for chek_rp in quest_check:
                    try:
                        rep_chek_pk = int(chek_rp)
                        rep_chek_box_verify = Reponse.objects.get(pk = rep_chek_pk, statut = True)
                        trouver_chek += 1
                        
                    except:
                        pass
                if trouver_chek == rep_chek_box:
                    note_user += 1

        if quest_rad:
            try:
                rep_rad_pk = int(quest_rad)
                rep_radio = Reponse.objects.filter(question_resp__quiz__pk = quiz.pk, pk = quest_rad, statut =True)[:1].get()
                note_user += 1
            except:
                pass
    print('note :', note_user)
    # print(quest_1)
    print(quest_rad)
    
    
    print('on a  :', nbquestion)

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









def register(request):
    special = Nangroupe.objects.all()
    data = {
        'specialisation': special,
    }
    return render(request, 'specialisation/pages/register.html', data)

def regist(request):
    key = json.loads(request.body.decode('utf-8'))
    
    datas = []

    sortie = {}
    nom = key['nom']
    prenom = key['prenom']
    date_nassance = key['date_nassance']
    phone = key['phone']
    password = key['password']
    email = key['email']
    commune = key['commune']
    github = key['github']
    special = key['special']
    genre = key['genre']
    if nom == "" or prenom == "" or phone == "" or email == "" or github == "" or password == "":
        valid = False
    else:
        valid = True

    print(nom, special, valid)
    if valid:

        
        try:
            
            user = User(username = github, first_name = nom, last_name = prenom, email = email)
            #user.save()
            special = int(special)
            group = Nangroupe.objects.get(pk = special)

            print(group)
            # user.profile.contacts = phone
            # user.profile.genre = genre
            
            # user.profile.location = commune
            # user.profile.birth_date = date_nassance
            
            # user.profile.nanplus = False
            #user.save()
            # user.password = password

            # user.set_password(user.password)

            # user.save()
            sortie['succes'] = "cool"
            print('save')
        except:
            sortie['succes'] = "fail"
            print('error')
        
    else:
        sortie['succes'] = "fail"


    datas.append(sortie)
    retour = json.dumps(datas)

    
    return JsonResponse(retour, safe=False)
