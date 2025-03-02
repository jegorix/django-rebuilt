from django import forms

class UserForm(forms.Form):
    vyb = forms.NullBooleanField(label = "Do you want to leave this page?")
    basket = forms.BooleanField(label = "Do you want to buy this good?", required = False)
#     name = forms.CharField(label = 'First Name', initial = 'your name...')
#     age = forms.IntegerField(label = 'Full age')
#     sex = forms.CharField(label = 'Gender')
#     text = forms.CharField(label = 'Content', help_text = 'No more 100 symbols')
# f = UserForm(auto_id = False)
