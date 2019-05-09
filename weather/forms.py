from django import forms
from .models import Pref

class PostForm(forms.ModelForm):
    prefs = forms.ModelChoiceField(
    label='都道府県名',
    queryset=Pref.objects,
    )
    
    class Meta:
        model = Pref
        fields = '__all__'