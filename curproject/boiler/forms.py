from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label = 'First Name')
    age = forms.IntegerField(label = 'Full age')
