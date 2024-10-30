from django import forms
from . import models
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render

class BoletaForm(forms.ModelForm):
    class Meta:
        model = models.Boleta
        fields = ('name', )
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full p-3 rounded-lg',
                'placeholder': 'Boleta'
            })
        } 
class PaymentsForm(forms.ModelForm):
    class Meta:
        model = models.Payment
        fields = ['boleta', 'amount', 'payment_due', 'payment_day', 'payed']
        widgets = {
            'boleta': forms.Select(attrs={
                'class': 'w-full p-3 rounded-lg'
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'w-full p-3 rounded-lg',
                'placeholder': 'Amount'
            }),
            'payed': forms.CheckboxInput(attrs={
                'class': 'rounded-lg',
            }),
            'payment_due': forms.DateInput(attrs={
                'type': 'date', 'class': 'w-full rounded-md'
            }),
            'payment_day': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full rounded-md'
            }),
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
        'class': 'w-full p-3 rounded-lg',
        'placeholder': 'Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full p-3 rounded-lg',
        'placeholder': 'Password'
    }))

class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full p-3 rounded-lg',
        'placeholder': 'Username'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'w-full p-3 rounded-lg',
        'placeholder': 'Email'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full p-3 rounded-lg',
        'placeholder': 'Password'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full p-3 rounded-lg',
        'placeholder': 'Confirm Password'
    }))