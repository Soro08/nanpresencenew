#  IMAGE STATIC URL

from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name = "home"),
    
    path('userliste', views.userliste, name="userliste"),
    path('groupliste', views.groupliste, name="groupliste"),
    
    path('generatecode', views.generateQrcodes, name="generatecode"),
    path('nanpresence', views.nanpresence, name="nanpresence"),


    #path('nanpresence', views.nanpresence, name="nanpresence"),


    path('testresence', views.testqrcode, name="api"),
    path('apiqrcode', views.apisendqrcode, name="apiqrcode"),


    # API
    path('apilogin', views.apilogin, name="apilogin"),
    

    

    #### API C A LL E D
    
   


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT )
