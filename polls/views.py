# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404
from datetime import datetime
from django.contrib.auth import authenticate, login
from .forms import ConnexionForm,InscriptionForm,AnnonceForm

from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from .models import Profil,Annonce
from django.core import serializers
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def accueil(request):
	# Nous sélectionnons tous nos capteurs
	return render(request,'polls/accueil.html',{'motes': []})

def connexion(request):
	error = False
	if request.method == "POST":
		form = ConnexionForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]
			user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
			if user:  # Si l'objet renvoyé n'est pas None
				login(request, user)  # nous connectons l'utilisateur
				request.session['logged']=True				
			else: # sinon une erreur sera affichée
				error = True
	else:
		form = ConnexionForm()
	return render(request, 'polls/connexion.html', locals())
	
	
def inscription(request):
    error = False
    if request.method == "POST":
        form = InscriptionForm(request.POST)
        if form.is_valid():
						username = form.cleaned_data["username"]
						password = form.cleaned_data["password"]
						repassword = form.cleaned_data["repassword"]
						email = form.cleaned_data["email"]
						user = User.objects.create_user(username, email, password)
						user = authenticate(username=username, password=password)
						if user:
							login(request, user)
						else: 
							error = True
    else:
        form = InscriptionForm()
    return render(request, 'polls/inscription.html', locals())
	
def annonce(request):
    error = False
    if request.method == "POST":
			form = AnnonceForm(request.POST)
			if form.is_valid():
					name = form.cleaned_data["nom"]
					desc = form.cleaned_data["description"]
					price=form.cleaned_data["prix"]
					owner=form.cleaned_data["owner"]
					pwd=form.cleaned_data["pwd"]
					print(owner,pwd)
										
					if pwd!="logged":
						user = authenticate(username=owner, password=pwd)
						if user:
							login(request, user)
						return render(request, 'polls/accueil.html', locals())
    else:
			form = AnnonceForm()
    return render(request, 'polls/annonce.html', locals())
	
def deconnexion(request):
    logout(request)
    return render(request, 'polls/accueil.html', locals())
	
def offres(request):
    #offres = Annonce.objects.get(genre="Offre")
    return render(request, 'polls/offres.html', locals())