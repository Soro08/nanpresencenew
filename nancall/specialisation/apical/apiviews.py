from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.validators import URLValidator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from datetime import date, datetime, time

from specialisation.models import CompositionProjet, Projet

from django.http import JsonResponse

import json

def sendlien(request):
    
    sortie = {}
    is_post = False

    try:
        send = json.loads(request.body.decode('utf-8'))
        liengit = send['liengithub']
        projetkey = send['projetkey']
        print(liengit, projetkey)
        projet = Projet.objects.get(pk = projetkey)
        validate = URLValidator(schemes=('http', 'https', 'ftp', 'ftps', 'rtsp', 'rtmp'))
        validate(liengit)
        try:
            
            is_projet = CompositionProjet.objects.filter(project_compo = projet, user= request.user)
            sortie['message'] = "projet déjà envoyé en attente de correction" 

        except:
            sendprojet = CompositionProjet(project_compo = projet, user= request.user, lien = liengit)
            sendprojet.save()
            is_post = True
            sortie['message'] = "projet envoyé avec succèes en attente de correction" 
            
    except:
        is_post = False
        sortie['message'] = "Une erreur s'est produite lors de l'envoie du projet" 
        

    if is_post:
        sortie['statut'] = "succes"
    else:
        sortie['statut'] = "error"

    retour = sortie
    print(retour)
    
    return JsonResponse(retour)
