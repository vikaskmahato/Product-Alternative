from django import forms
from .models import Profile

class Profileform(forms.ModelForm):
    class Meta:
        model=Profile
        fields={'firstname','lastname','email','category','product','desc','contact_details','photo'}
        widgets={ 'firstname':forms.TextInput(attrs={'class': 'form-control'}),
                  'lastname':forms.TextInput(attrs={'class': 'form-control'}),
                  'email':forms.EmailInput(attrs={'class': 'form-control'}),
                  'category':forms.TextInput(attrs={'class': 'form-control'}),
                  'product':forms.TextInput(attrs={'class': 'form-control'}),
                  'desc':forms.Textarea(attrs={'class': 'form-control'}),
                  'contact_details':forms.Textarea(attrs={'class': 'form-control'}),
                  

                    }

class Searchform(forms.Form):
    name=forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Category e.g. toothpaste'}))
    

class Registerform(forms.Form):
    name=forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Username'}))
    email=forms.EmailField(label='',widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Email' }))
    password1=forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Password'}))
    password2=forms.CharField(label='',widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Confirm Password'}))

class Loginform(forms.Form):
    name=forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Username'}))
    password1=forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Password'}))        