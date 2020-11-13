from django.contrib.auth.forms import UserCreationForm
from django import forms
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
# from . import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Username', 'size':'12', 'class': "form-control"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter First Name', 'size':'12', 'class': "form-control"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Last Name', 'size':'12', 'class': "form-control"}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Email', 'size':'12', 'class': "form-control"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password', 'size':'12', 'class': "form-control"}), label='Password', help_text='')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Retype Password', 'size':'12', 'class': "form-control"}), label='Retype Password')
    

    class Meta():
        model = User
        fields = (
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'password1', 
            'password2', 
             )
        
        # labels = {
        #     'username':_('user name'),
        #     'first_name':_('first name'),
        #     'last_name':_('last name'),
        #     'email': _('email'),
        #     'password1': _('passwordLKL'),
        #     'password2': _('re-type password'),
        # }

        help_texts = {
            'username': _(''),
            'email': _('')
        }
        error_messages = {
            'name': {
                'max_length': _("too long."),
            },
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs['autofocus'] = True


    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_('Password mismatch'), code='invalid')
        return password2

        
        
    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email=self.cleaned_data["email"]
        user.first_name=self.cleaned_data["first_name"]
        user.last_name=self.cleaned_data["last_name"]
        # user.username=self.cleaned_data['username']
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()
        return user

# class UserSignInForm(forms.ModelForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your Username', 'size':'40', 'class': "form-control"}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'size':'40', 'class': "form-control"}))

#     class Meta:
#         model = User
#         fields = [ 'username','password']

#         error_messages = {
#             'name': {
#                 'max_length': _("too long."),
#             },
#         }
