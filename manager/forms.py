from django import forms
from .models import Table, Item


class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ["name"]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full p-2 rounded-lg border border-zinc-800 bg-zinc-950 text-zinc-400',
                'placeholder': 'Enter table name...'
            }),
        }


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'price']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full p-2 rounded-lg border border-zinc-800 bg-zinc-950 text-zinc-400',
                'placeholder': 'Enter food name...'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'w-full p-2 rounded-lg border border-zinc-800 bg-zinc-950 text-zinc-400',
                'placeholder': 'Enter price...'
            }),
        }
