from django import forms
from .models import Recept

class ReceptForm(forms.ModelForm):
    class Meta:
        model = Recept
        fields = ['titul', 'popis', 'ingredience', 'postup', 'kategorie', 'kuchar', 'obrazek']
        labels = {
            'titul': 'Název receptu',
            'popis': 'Popis',
            'ingredience': 'Ingredience',
            'postup': 'Postup',
            'kategorie': 'Kategorie',
            'kuchar': 'Kuchař',
            'obrazek': 'Obrázek',
        }
        widgets = {
            'titul': forms.TextInput(attrs={'class': 'form-control'}),
            'popis': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'ingredience': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'postup': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'kategorie': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'kuchar': forms.Select(attrs={'class': 'form-control'}),
            'obrazek': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }



