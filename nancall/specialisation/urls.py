#  IMAGE STATIC URL

from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

from .apical import apiviews

from rest_framework.routers import DefaultRouter
from .apiviews import QuizViewSet


router = DefaultRouter()
router.register('apiquiz', QuizViewSet, base_name='apiquiz')


urlpatterns = [
    path('', views.homespe,name = "homespe"),

    path('groupe', views.mygroupe,name = "groupe"),
    path('profile', views.myprofile,name = "profile"),
    path('project', views.myproject,name = "project"),
    path('quiz', views.myquiz,name = "quiz"),
    path('resultat', views.myresultat,name = "resultat"),
     path('quizresult', views.quizresult, name="quizresult"),

    path('connexion', views.mylogin,name = "mylogin"),
    path('deconnexion', views.deconnexion,name = "deconnexion"),

    #--------- API --------#

    path('sendprojet', apiviews.sendlien,name = "sendlien"),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT )

urlpatterns += router.urls