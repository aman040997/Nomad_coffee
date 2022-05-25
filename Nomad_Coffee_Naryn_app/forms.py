from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
from .models import Profile

class ContactsForm(forms.ModelForm):

    class Meta:
        model = ContactForm
        fields = ['full_name', 'email', 'phone_number', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'tm-form-control', 'placeholder': 'Ф.И.О'}),
            'email': forms.EmailInput(attrs={'class': 'tm-form-control', 'placeholder': 'Email'}),
            'phone_number': forms.NumberInput(attrs={'class': 'tm-form-control', 'placeholder': 'Телефон'}),
            'message': forms.Textarea(attrs={'class': 'tm-form-control', 'placeholder': 'Сообщения'}),
        }



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('products',)


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'tm-form-control'}))
    first_name = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'tm-form-control'}))
    last_name = forms.CharField(max_length=150, required=True, widget=forms.TextInput(attrs={'class': 'tm-form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'tm-form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'tm-form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'tm-form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']