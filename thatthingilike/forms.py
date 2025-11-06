from django import forms
from .models import Tag, Location


class TagForm(forms.Form):
    tag = forms.ModelChoiceField(queryset=Tag.objects.all())

class LocationForm(forms.Form):
    location = forms.ModelChoiceField(queryset=Location.objects.all())