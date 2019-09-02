from django.shortcuts import render
import uuid
from .models import *
from django.contrib.auth.models import User
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