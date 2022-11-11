from django import forms
from . models import dispform
class mform(forms.ModelForm):
    class Meta:
        model=dispform
        fields=['username','age','address']