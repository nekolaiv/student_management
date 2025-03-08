from django import forms
from .models import Table, Student


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


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id','first_name', 'last_name', 'email', 'date_of_birth', 'course', 'enrollment_date']
        widgets = {
            'student_id': forms.TextInput(attrs={
                'class': 'w-full p-2 rounded-lg border border-zinc-800 bg-zinc-950 text-zinc-400',
                'placeholder': 'Enter first name...'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'w-full p-2 rounded-lg border border-zinc-800 bg-zinc-950 text-zinc-400',
                'placeholder': 'Enter first name...'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'w-full p-2 rounded-lg border border-zinc-800 bg-zinc-950 text-zinc-400',
                'placeholder': 'Enter last name...'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full p-2 rounded-lg border border-zinc-800 bg-zinc-950 text-zinc-400',
                'placeholder': 'Enter email...'
            }),
            'date_of_birth': forms.DateInput(attrs={
                'class': 'w-full p-2 rounded-lg border border-zinc-800 bg-zinc-950 text-zinc-400',
                'type': 'date'
            }),
            'course': forms.Select(attrs={
                'class': 'w-full p-2 rounded-lg border border-zinc-800 bg-zinc-950 text-zinc-400'
            }),
            'enrollment_date': forms.DateInput(attrs={
                'class': 'w-full p-2 rounded-lg border border-zinc-800 bg-zinc-950 text-zinc-400',
                'type': 'date'
            }),
        }
