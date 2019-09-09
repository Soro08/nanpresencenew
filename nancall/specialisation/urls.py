#  IMAGE STATIC URL

from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

urlpatterns = [
    path('', views.homespe,name = "homespe"),

    path('groupe', views.mygroupe,name = "groupe"),
    path('profile', views.myprofile,name = "profile"),
    path('project', views.myproject,name = "project"),
    path('quiz', views.myquiz,name = "quiz"),
    path('resultat', views.myresultat,name = "resultat"),




    path('connexion', views.mylogin,name = "mylogin"),
    path('deconnexion', views.deconnexion,name = "deconnexion"),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT )
