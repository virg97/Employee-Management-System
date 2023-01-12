from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput


class NewAccountForm(forms.ModelForm):

    class Meta:
        model = User
        fields =['first_name', 'last_name', 'email', 'username']

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'first name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'last name', 'class': 'form-control'}),
            'email': TextInput(attrs={'placeholder': 'email address', 'class': 'form-control'}),
            'username': TextInput(attrs={'placeholder': 'username', 'class': 'form-control'}),
        }

    def clean(self):

        field_data = self.cleaned_data
        email_value = field_data.get('email')
        username_value = field_data.get('username')
        if User.objects.filter(email=email_value).exists():
            msg = 'Emailul deja exista. Introduceti alt mail'
            self._errors['email'] = self.error_class([msg])

        if User.objects.filter(username=username_value).exists():
            msg_username = "Usernameul deja exista. Folositi alt username"
            self._errors['username'] = self.error_class([msg_username])

        return field_data