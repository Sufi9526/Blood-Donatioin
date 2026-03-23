from django import forms
from app1.models import *

class SignupForm(forms.ModelForm):
    class Meta:
        model = Udata
        fields = '__all__'
    
