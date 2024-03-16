from django import forms
from .models import table
from .models import staf
from .models import jew

class AddForm(forms.ModelForm):
    class Meta:
        model = table


        fields = ('name','password','email')

        widgets = {
            'name':forms.TextInput (attrs={'class':'form-control'}),
            'email':forms.TextInput (attrs={'class':'form-control'}),
            'password':forms.TextInput (attrs={'class':'form-control'}),
            
        }

class Adds(forms.ModelForm):
    class Meta:
        model = staf


        fields = ('name','password','email')

        widgets = {
            'name':forms.TextInput (attrs={'class':'form-control'}),
            'email':forms.TextInput (attrs={'class':'form-control'}),
            'password':forms.TextInput (attrs={'class':'form-control'}),
            
            
        }

class up(forms.ModelForm):
    class Meta:
        model = staf


        fields = ('name','password','email','lname','age','gender','department')

        widgets = {
            'name':forms.TextInput (attrs={'class':'form-control'}),
            'lname':forms.TextInput (attrs={'class':'form-control'}),
            'email':forms.TextInput (attrs={'class':'form-control'}),
            'password':forms.TextInput (attrs={'class':'form-control'}),
            'genter':forms.TextInput (attrs={'class':'form-control'}),
            'age':forms.TextInput (attrs={'class':'form-control'}),
            'department':forms.TextInput (attrs={'class':'form-control'}),
            
            
        }

class im(forms.ModelForm):
    class Meta:
        model = jew


        fields = ('name','price','gram','image','mod')
        widgets = {
           
            
        }