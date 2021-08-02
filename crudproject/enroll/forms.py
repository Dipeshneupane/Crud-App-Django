from django import forms
from .models import User
from django.core import validators
from django.forms import ModelForm



class StudentRegistration(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
    

    def clean(self):
 
        # data from the form is fetched using super function
        super(StudentRegistration, self).clean()
         
        # extract the username and text field from the data
        username = self.cleaned_data.get('name')
        password = self.cleaned_data.get('password')
 
        # conditions to be met for the username length
        if len(username) < 5:
            self._errors['name'] = self.error_class([
                'Minimum 5 characters required'])
        if len(password) <10:
            self._errors['password'] = self.error_class([
                'password Should Contain a minimum of 8 characters'])
 
        # return any errors if found
        return self.cleaned_data


