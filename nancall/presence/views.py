from django.shortcuts import render

# Create your views here.
def home(request):

    return render(request,'myadmin/pages/index.html')

def generateQrcodes(request):

    return render(request,'myadmin/pages/qrcode.html')