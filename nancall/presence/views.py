from django.shortcuts import render

# Create your views here.
def home(request):

    return render(request,'myadmin/pages/index.html')

def generateQrcodes(request):

    return render(request,'myadmin/pages/qrcode.html')

def userliste(request):

    return render(request,'myadmin/pages/userliste.html')

def groupliste(request):

    return render(request,'myadmin/pages/groupliste.html')

def nanpresence(request):

    return render(request,'myadmin/pages/presence.html')