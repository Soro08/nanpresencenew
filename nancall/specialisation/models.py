from django.db import models

from presence.models import Nangroupe
from django.contrib.auth.models import User

# Create your models here.

#Quiz

class Quiz(models.Model):
    groupe_quiz = models.ForeignKey(Nangroupe, on_delete = models.CASCADE, related_name='quizgroup')
    nom = models.CharField(max_length=255)
    duree_du_quiz = models.PositiveIntegerField(default=10)
    cota_validation = models.PositiveIntegerField(default=70)
    positonduquiz = models.BooleanField(default=True)
    statut = models.BooleanField(default=True)
    date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom

class QuestionType(models.Model):
    nom = models.CharField(max_length=255)
    statut = models.BooleanField(default=True)

    def __str__(self):
        return self.nom


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete = models.CASCADE, related_name = 'questionquiz', null = True)
    question = models.TextField()
    type_question = models.ForeignKey(QuestionType, on_delete=models.CASCADE, related_name='typequestion')
    statut = models.BooleanField(default=True)

class Reponse(models.Model):
    question_resp = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_rep', null = True)
    reponse = models.TextField()
    statut = models.BooleanField(default=False)

class CompositionQuiz(models.Model):
    quiz_compo = models.ForeignKey(Quiz, on_delete = models.CASCADE, related_name='compoquiz')
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='quiztuser')
    
    statut = models.BooleanField(default=False) 
    note = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#projet
class Projet(models.Model):
    groupe_projet = models.ForeignKey(Nangroupe, on_delete = models.CASCADE, related_name='projetgroup')
    nom = models.CharField(max_length=255)
    description = models.TextField()
    source = models.FileField(upload_to='projet/')
    cota_validation = models.PositiveIntegerField(default=70)
    statut = models.BooleanField(default=True)
    date_debut = models.DateField()
    date_fin = models.DateField()


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom


class CompositionProjet(models.Model):
    project_compo = models.ForeignKey(Projet, on_delete = models.CASCADE, related_name='compoprojet')
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='projetuser')
    lien = models.URLField()
    statut = models.BooleanField(default=False)
    note = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
