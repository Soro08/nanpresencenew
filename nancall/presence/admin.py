from django.contrib import admin
from django.utils.safestring import mark_safe
# Register your models here.
from .models import *

#Configuration du site django
admin.site.site_header = "NaN PRESENCE" 
admin.site.site_title = "NaN PRESENCE Admin Portal"
admin.site.index_title = "Welcome to NaN PRESENCE Admin Portal"

@admin.register(Nangroupe)
class NangroupeAdmin(admin.ModelAdmin):
    list_display = ('images', 'name', 'created_by')
    
    search_fields = ("name",)
    exclude = ['created_by',]

    def images(self, obj):

        return mark_safe('<img src="{url}" width="100px" height="50px" />'.format(url=obj.image.url))
    def save_model(self, request, obj, form, change): 
        obj.created_by = request.user
        obj.save()

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('images', 'user', 'email', 'date_connecte', 'location', 'birth_date')
    list_filter = ("location", )
    search_fields = ("location",)
    def date_connecte(self, obj):
        return obj.user.last_login

    def images(self, obj):

        return mark_safe('<img src="{url}" width="100px" height="50px" />'.format(url=obj.image.url))
    




@admin.register(Jours)
class JoursAdmin(admin.ModelAdmin):
    list_display = ('jours', 'created_by', 'slug')
    
    search_fields = ("name",)
    exclude = ['created_by',]

    
    def save_model(self, request, obj, form, change): 
        obj.created_by = request.user
        obj.save()# vim: set fileencoding=utf-8 :


from . import models


class PresenceAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'jours',
        'heure_arrivee',
        'heure_depart',
        'statut',
        'created_at',
        'updated_at',
    )
    list_filter = (
       
        
        'jours',
        
        'statut',
        'created_at',
        'updated_at',
    )
    date_hierarchy = 'created_at'


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Presence, PresenceAdmin)
