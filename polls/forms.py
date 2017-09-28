from django import forms
      
class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
class OffreForm(forms.Form):
    name = forms.CharField(label="Nom", max_length=100)
    desc = forms.CharField(label="Nom", max_length=1000)
    price = forms.FloatField(label="Prixrix")
class InscriptionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    email = forms.EmailField()
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    repassword = forms.CharField(label="Confirmer le mot de passe", widget=forms.PasswordInput)
    