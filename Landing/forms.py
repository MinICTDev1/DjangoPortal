from django import forms

from .models import Submision

class submissionForm(forms.ModelForm):
    class Meta:
        model = Submision
        fields = '__all__'
