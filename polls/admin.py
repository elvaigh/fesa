# -*- coding: utf-8 -*-

from django.contrib import admin

# Register your models here.

from .models import Profil,Annonce

admin.site.register(Profil)
admin.site.register(Annonce)