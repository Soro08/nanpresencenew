from django.db import models
# USEER
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from slugger import AutoSlugField
# Create your models here.

#-------- GROUPE --------#
class Jours_cours(models.Model):
    name = models.CharField(max_length=200)
    weekday = models.PositiveIntegerField(null=True)
    statut = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Nangroupe(models.Model):
    created_by = models.ForeignKey(User,on_delete=models.CASCADE, null=True, related_name='creerpar')
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    responsables = models.ManyToManyField(User, related_name="respogroup")

    etudiants = models.ManyToManyField(User, related_name="useringroup")

    image = models.ImageField(upload_to='pic_folder/',default='nanlogo.png')
    jours_presence = models.ManyToManyField(Jours_cours)
    equipe = models.PositiveIntegerField(null =True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    

#-------- USER --------#
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    
    groupe = models.ForeignKey(Nangroupe, on_delete=models.CASCADE, related_name='usergroupe', null=True)
    genre = models.CharField(max_length=20, null=True)
    contacts = models.CharField(max_length=30, null=True)

    qrcontent = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to='pic_folder/', default='useravatar.png')

    userkey = models.IntegerField(null=True)
    userckey = models.CharField(max_length=255, null=True)
    userpass = models.CharField(max_length=255, null=True)
    location = models.CharField(max_length=30, null=True)
    birth_date = models.DateField(null=True)

    @property
    def email(self):
        return self.user.email

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, created, **kwargs):
        
        instance.profile.save()


#========================= GESTION PRESENCE  ============================#


#----------- JOURS -----------------#


class Jours(models.Model):
    jours = models.DateField()
    created_by = models.ForeignKey(User,on_delete=models.CASCADE, null=True,related_name= 'addby')
    debut_heure_arrivee = models.TimeField(null=True, default='08:00')
    fin_heure_arrivee = models.TimeField(null=True, default='10:00')
    slug = models.TextField(null=True, unique=True)
    #image = models.ImageField(upload_to='pic_folder/',default='nanlogo.png')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str( self.jours)

class Presence(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, related_name='userpresence')
    jours = models.ForeignKey(Jours, on_delete=models.CASCADE, related_name='joursap')
    heure_arrivee = models.TimeField(null=True)
    heure_depart = models.TimeField(null=True, default='17:00')
    statut = models.BooleanField(default=False)
    #image = models.ImageField(upload_to='pic_folder/',default='nanlogo.png')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = ('user', 'jours',)

    