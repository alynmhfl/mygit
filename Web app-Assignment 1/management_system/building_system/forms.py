from django import forms
from .models import *


class ElectricalForm(forms.ModelForm):
    class Meta:
        model = Electrical
        fields = ('facilities', 'level', 'status', 'issues')


class MechanicalForm(forms.ModelForm):
    class Meta:
        model = Mechanical
        fields = ('facilities', 'level', 'status', 'issues')


class CleaningForm(forms.ModelForm):
    class Meta:
        model = Cleaning
        fields = ('facilities', 'level', 'status', 'issues')
