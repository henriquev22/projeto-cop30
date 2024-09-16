from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'description', 'image', 'condition']
        labels = {
            'title': 'Título',
            'description': 'Descrição',
            'condition': 'Estado',
            'image': 'Imagem',
        }
