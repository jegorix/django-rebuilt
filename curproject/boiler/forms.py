from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label = "Имя клиента")
    age = forms.IntegerField(label = "Возраст клиента")
    # name = forms.CharField(label = "Имя", help_text="Enter your name", min_length = 2, max_length = 20)
    # age = forms.IntegerField(label = "Возраст", help_text = "Enter your age", min_value = 1, max_value = 120)
    # comment = forms.CharField(label = "Комментарий", widget = forms.Textarea)
    # reklama = forms.BooleanField(label = "Согласны получать рекламу?", required = False)
    # field_order = ["name", "age", "comment"]
    # file = forms.FileField(label = "Select a file", required = False)
    # nums = forms.DecimalField(label = 'Enter a decimal number', decimal_places = 2, required = False)
    # ling = forms.ChoiceField(label = "language", choices = (
    #     (1, "English"), (2, "Russian"), (3, "Spanish")
    # ))
    # vyb = forms.NullBooleanField(label = "Do you want to leave this page?")
    # basket = forms.BooleanField(label = "Do you want to buy this good?", required = False)
    # name = forms.CharField(label = "username", required = False)
    # email = forms.EmailField(label = "email", required = False)
    # ip_adress = forms.GenericIPAddressField(label = "IP adress", help_text = "Example: 192.168.127.12")
    # reg_text =  forms.RegexField(label = "special field", regex = "^[0-9][A-F][0-9]$" )
#     name = forms.CharField(label = 'First Name', initial = 'your name...')
#     age = forms.IntegerField(label = 'Full age')
#     sex = forms.CharField(label = 'Gender')
#     text = forms.CharField(label = 'Content', help_text = 'No more 100 symbols')
# f = UserForm(auto_id = False)
