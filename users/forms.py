from django import forms
from .models import Customer
from django.contrib.auth.forms import UserCreationForm

class CustomerCreateForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=255)

    class Meta:
        model = Customer
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'email', 'user_image', 'phone')

