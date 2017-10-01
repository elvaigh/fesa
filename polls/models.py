# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
class Profil(models.Model):
    user = models.OneToOneField(User)  # La liaison OneToOne vers le modèle User
    pseudo = models.CharField(max_length=30)
    avatar = models.ImageField(null=True, blank=True, upload_to="avatars/")
    def __str__(self):
        return "Profil de {0}".format(self.user.username)
      
class Annonce(models.Model):
    titre = models.CharField(max_length=2000)
    genre = models.CharField(max_length=20)
    price=models.FloatField()
    owner = models.ForeignKey(Profil)
    published = models.DateTimeField('date published')
    
