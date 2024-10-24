from django import forms
from . import models
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render


class PaymentsForm(forms.ModelForm):
    class Meta:
        model = models.Payment
        fields = ['boleta', 'amount', 'payment_due', 'payment_day', 'payed']
        widgets = {
            'payment_due': forms.DateInput(attrs={'type': 'date'}),
            'payment_day': forms.DateInput(attrs={'type': 'date'}),
        }
        
class PaymentUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Payment
        fields = ['boleta', 'amount', 'payment_due', 'payment_day', 'payed']
        widgets = {
            'payment_due': forms.DateInput(attrs={'type': 'date'}),
            'payment_day': forms.DateInput(attrs={'type': 'date'}),
        }    
    
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full p-4 rounded-lg',
        'placeholder': 'Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full p-4 rounded-lg',
        'placeholder': 'Password'
    }))

class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full p-4 rounded-lg',
        'placeholder': 'Username'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'w-full p-4 rounded-lg',
        'placeholder': 'Email'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full p-4 rounded-lg',
        'placeholder': 'Password'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full p-4 rounded-lg',
        'placeholder': 'Confirm Password'
    }))