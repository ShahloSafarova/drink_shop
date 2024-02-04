from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import Ichimliklar, ReviewDrinkModel


class UpdateDrinkForm(forms.ModelForm):
    class Meta:
        model = Ichimliklar
        fields = ['name','short_description','company','image_drink']

    def __init__(self, *args, **kwargs):
        super(UpdateDrinkForm, self).__init__(*args, **kwargs)

class CommentForm(forms.ModelForm):
    class Meta:
        model = ReviewDrinkModel
        fields = ['comment_body','star_given']

class CommentUpdateForm(forms.ModelForm):
    class Meta:
        model = ReviewDrinkModel
        fields = ['comment_body','star_given']