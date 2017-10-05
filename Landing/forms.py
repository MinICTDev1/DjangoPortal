from django import forms

from .models import Submision

class submissionForm(forms.ModelForm):
    class Meta:
        model = Submision
        fields = '__all__'

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
    