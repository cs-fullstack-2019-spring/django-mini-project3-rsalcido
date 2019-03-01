from django import forms
from .models import TimeCardModel


# linked to model
class TimeCardForm(forms.ModelForm):
    class Meta:
        model = TimeCardModel
        fields = ['name', 'school', 'subject', 'hours', 'dow',]


