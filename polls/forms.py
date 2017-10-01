from django import forms
      
class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
class AnnonceForm(forms.Form):
    nom = forms.CharField(label="Nom", max_length=100)
    categorie = forms.ChoiceField(label="Type", choices=(),widget=forms.Select(attrs={'class':'selector'}))
    description = forms.CharField(widget=forms.Textarea)
    prix = forms.FloatField(label="Prix")
    owner=forms.CharField(widget=forms.widgets.HiddenInput())
    pwd=forms.CharField(widget=forms.widgets.HiddenInput())
    
    def __init__(self, *args, **kwargs):
        choices = [('of', 'Offre'),('dem', 'Demande')]
        super(AnnonceForm, self).__init__(*args, **kwargs)
        self.fields['categorie'].choices = choices
class InscriptionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    email = forms.EmailField()
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    repassword = forms.CharField(label="Confirmer le mot de passe", widget=forms.PasswordInput)
    