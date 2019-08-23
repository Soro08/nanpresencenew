#  IMAGE STATIC URL

from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('generatecode', views.generateQrcodes),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT )
