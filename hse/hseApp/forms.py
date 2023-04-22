from django import forms

class UserForm(forms.Form):
    username = forms.CharField(label = 'UserName', max_length=50)
    pwd = forms.CharField(label= 'Password', widget=forms.PasswordInput, max_length=20)
    email = forms.EmailField(label='Email')


class LoisForm(forms.Form):
    name = forms.CharField(label='name of lois', widget=forms.Textarea)
    date = forms.DateField(initial="YYYY-MM-DD")
    description = forms.CharField(label='description of lois', widget=forms.Textarea)
    section = forms.CharField(max_length=255)

class LoginForm(forms.Form):
    email = forms.EmailField(label = 'email')
    password = forms.CharField(label= 'Password', widget=forms.PasswordInput, max_length=20)

class SearchLois(forms.Form):
    name = forms.CharField(label = 'name', max_length=50, required=False, initial='')
    date = forms.DateField(initial="YYYY-MM-DD", required=False)
