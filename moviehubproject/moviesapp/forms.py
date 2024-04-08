from django import forms
from moviesapp.models import Movie,Category
from django.forms import ModelForm
from django.forms.widgets import TextInput,Select,DateInput


class Movieform(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['name','description','category','date','actors','youtube','image']
        widgets= {
            'name': forms.CharField(max_length=250),
            'description': forms.CharField(max_length=250),
            'category': forms.Select(attrs={'class':'form-control'}),
            'date':forms.DateField(attrs={'class':'form-control'}),
            'actors':forms.CharField(attrs={'class':'form-control'}),
            'youtube':forms.URLField(attrs={'class':'form-control'}),
            'image':forms.TextInput(attrs={'class':'form-control'}),
            'created' : forms.DateTimeField(attrs={'class':'form-control'}),
            'updated' : forms.DateTimeField(attrs={'class':'form-control'})
        }