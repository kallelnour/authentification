from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['prenom', 'adresse_mail', 'numero', 'date_naissance']  # Utilise 'numero' au lieu de 'telephone'
