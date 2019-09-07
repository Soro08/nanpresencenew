from django.shortcuts import render
import uuid
from .models import *
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from datetime import date, datetime, time

today = datetime.now().replace(tzinfo=None)

weekday = datetime.today().isoweekday()
print(datetime.today().isoweekday())
#___ G E T P H P D A T A______###

import json

# Create your views here.
def home(request):
    users = User.objects.all()
    groupes = Nangroupe.objects.all()
    presence = Presence.objects.filter(statut = True)
    absence = Presence.objects.filter(statut = False)

    data = {
        'users':users,
        'groupes':groupes,
        'presence': presence,
        'absence':absence,
    }

    


    return render(request,'myadmin/pages/index.html', data)

def generateQrcodes(request):
    jours = request.POST.get('jours')
    arriveheure = request.POST.get('arriveheure')
    arrivefin = request.POST.get('arrivefin')

    daterange = request.POST.get('daterange')
    print(daterange)
    if jours is not None and arriveheure is not None and arrivefin is not None:
        print('save')
        keys = uuid.uuid1()
        print(keys)
        myday = Jours(jours = jours, debut_heure_arrivee = arriveheure, fin_heure_arrivee = arrivefin, created_by = request.user, slug = keys)
        #myday.save()
    else:
        print(jours , arriveheure, arrivefin)
    print(jours)
    return render(request,'myadmin/pages/qrcode.html')

def userliste(request):

    return render(request,'myadmin/pages/userliste.html')

def groupliste(request):

    return render(request,'myadmin/pages/groupliste.html')

def nanpresence(request):

    return render(request,'myadmin/pages/presence.html')
@csrf_exempt
def apilogin(request):

   

    sortie = {}
    is_login = False
    try:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(username)
        if user is not None and user.is_active:
            print(1)
            is_login = True
        else:
            is_login = False   
            print(2)  
    except:
        is_login = False
        print(3)

    if is_login:
        sortie['statut'] = "succes"
        sortie['username'] = user.username
       
        
        sortie['usergroupe'] = user.profile.groupe.name
    else:
        sortie['statut'] = "error"

    
   
    
    return JsonResponse(sortie)



def apisendqrcode(request):
    
    datas = []

    sortie = {}
    
    is_valid = False
    try:
        username = request.POST.get('username')
        qrcode = request.POST.get('qrcode')
        user = User.objects.filter(username=username)[:1].get()
        if user.is_active:

            qrjour = Jours.objects.filter(slug = qrcode, debut_heure_arrivee__gte = today)[:1].get()
            try:
                presence = Presence.objects.filter(user = user, jours = qrjour)

                presence.statut = True
                presence.heure_arrivee = today
                presence.save()

                is_valid = True
            except:
                is_valid = False
        else:
            is_valid = False    
    except:
        is_valid = False

    if is_valid:
        sortie['statut'] = "succes"
    else:
        sortie['statut'] = "error"

    datas.append(sortie)
    retour = json.dumps(datas)
   
    
    return JsonResponse(retour, safe=False)