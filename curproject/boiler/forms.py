from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label = 'First Name')
    age = forms.IntegerField(label = 'Full age')
    sex = forms.CharField(label = 'Gender')
    text = forms.CharField(label = 'Content')
