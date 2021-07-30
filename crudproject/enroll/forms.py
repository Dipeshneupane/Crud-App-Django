from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        widget = {
            'name' :forms.TextInput(attrs = {'class': 'form-control'}),
            'email' : forms.EmailInput(attrs = {'class': 'form-control'}),
            'password' : forms.PasswordInput(render_value = True, attrs = {'class': 'form-control'}),
        }