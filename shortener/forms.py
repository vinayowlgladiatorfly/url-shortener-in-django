from django import forms
from .models import *

class shortener_form(forms.ModelForm):
    long_url = forms.URLField(widget=forms.URLInput(
        attrs={"class": "form-control-lg","placeholder": "your url is shorten:"}
    ))

    class Meta:
        model = Shortener

        fields = ('long_url',)