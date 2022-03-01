from django.forms import ModelForm, TextInput, EmailField
from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class ProfileForm(forms.ModelForm):
    email = forms.EmailField(required=False)
    
    class Meta:
        model = User
        fields = ('email', 'title', 'first_name', 'last_name', 'phone', 'affiliation', 'designation', 'industry')
        widgets = {
            'email': forms.TextInput(attrs={
                'disabled': True, 'class': 'disabled-input', 'readonly': True
            }),
        }
        extra_kwargs = {
            'email': {'read_only': True},
        }