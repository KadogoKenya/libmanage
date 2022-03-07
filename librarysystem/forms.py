from django.db import models
from . import forms
from django import forms
from django.contrib.auth.models import User
from . import models

from django.contrib.auth.models import User
from datetime import datetime,timedelta
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']

class StudentUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']

class StudentExtraForm(forms.ModelForm):
    class Meta:
        model=models.StudentExtra
        fields=['enrollment','branch']

class BookForm(forms.ModelForm):
    class Meta:
        model=models.Book
        fields=['name','isbn','author','category']

class IssuedBookForm(forms.Form):
   
    isbn2 = forms.ModelChoiceField(queryset=models.Book.objects.all(),empty_label="Name and isbn", to_field_name="isbn",label='Name and Isbn')
    enrollment2 = forms.ModelChoiceField(queryset=models.StudentExtra.objects.all(),empty_label="Name and enrollment",to_field_name='enrollment',label='Name and enrollment')
    
