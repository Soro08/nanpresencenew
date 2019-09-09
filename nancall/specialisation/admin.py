from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('groupe_quiz', 'nom','duree_du_quiz','statut','positonduquiz', 'cota_validation','date', 'created_at')
    
    search_fields = ("nom",)
    

    list_filter = ('statut','positonduquiz','groupe_quiz',)


@admin.register(QuestionType)
class QuestionTypeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'statut',)
    
    search_fields = ("nom",)

    list_filter = ('statut',)

# Inline 2-1
class ReponseInLine(admin.TabularInline):
    model = Reponse
    extra = 0


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('type_question','question', 'statut',)
    
    search_fields = ("question",)
    
    inlines = [
        ReponseInLine
    ]

    list_filter = ('statut','type_question')

@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    list_display = ('groupe_projet', 'nom','statut', 'cota_validation','date_debut','date_fin')
    
    search_fields = ("nom",)
    

    list_filter = ('statut','groupe_projet',)








# vim: set fileencoding=utf-8 :

from . import models


class CompositionQuizAdmin(admin.ModelAdmin):

    list_display = (
       
        'quiz_compo',
        'user',
        'statut',
        'note',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'quiz_compo',
        'user',
        'statut',
        'created_at',
        
    )
    date_hierarchy = 'created_at'


class CompositionProjetAdmin(admin.ModelAdmin):

    list_display = (
        
        'project_compo',
        'user',
        'lien',
        'statut',
        'note',
        'created_at',
        
    )
    list_filter = (
        'project_compo',
        'user',
        'statut',
        'created_at',
        
    )
    date_hierarchy = 'created_at'


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.CompositionQuiz, CompositionQuizAdmin)
_register(models.CompositionProjet, CompositionProjetAdmin)
