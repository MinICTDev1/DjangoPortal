from django import forms
from .models import Submision, FormTest

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Div, Button
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions, TabHolder, Tab)

class submissionForm(forms.ModelForm):
    '''Form to do with submission of proposals'''
    class Meta:
        '''Meta describing whihc model the class is being loaded from'''
        model = Submision
        fields = '__all__'

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.layout = Layout(
        TabHolder(
            Tab('Submitter',
                Div(
                    Div('individual_Name', css_class='col-xs-4'),
                    Div('gender', css_class='col-xs-4'),
                    Div('email', css_class='col-xs-4'),
                    css_class='row-fluid'),
                Div(
                    Div('current_address', css_class='col-xs-6'),
                    Div('phone_number', css_class='col-xs-6'),
                    css_class='row-fluid'),),
            Tab('Introduction',
                'title',
                'probelemStatement',
                'background',
                'concept'),
            Tab('Owner',
                'ownership'),
            Tab('Individual',
                'individualBD',
                'individual_NIN'),
            Tab('Team',
                'teamName',
                'Commncementdate'),
            Tab('Company',
                'company_regDate'),
            Tab('Hub',
                'hubName',
                'duration'),
            Tab('Details',
                Div(
                    Div('BusinessPlan', css_class='col-xs-12'),
                    css_class='row-fluid'),
                Div(
                    Div('FeasibilityStudy', css_class='col-xs-6'),
                    Div('StudyUpload', css_class='col-xs-6'),
                    css_class='row-fluid'),
                Div(
                    Div('ActionStatement', css_class='col-xs-12'),
                    css_class='row-fluid'),
                Div(
                    Div('EstimatedCost', css_class='col-xs-12'),
                    css_class='row-fluid'),
                Div(
                    Div('InnovationStage', css_class='col-xs-4'),
                    Div('Stage_Description', css_class='col-xs-8'),
                    css_class='row-fluid'),
                Div(
                    Div('Amount_invested', css_class='col-xs-4'),
                    css_class='row-fluid'),
                Div(
                    Div('Market_Study', css_class='col-xs-10'),
                    css_class='row-fluid'),
                'Market_Std_Descrip',
                'Market_STd_file',
                'Market',
                'Value_Added',
                'Time_to_product',
                'End_User_Invol',
                'Monitoring',
                'Fund_Raise',
                ),
            Tab('Problems',
                'Problems',
                'Impacts',
                'Remedies'),
            Tab('Safety',
                'Safety'),
            Tab('Future',
                'Locations',
                'Sustainability',
                'MultiCultural',
                ),
            )
    )
    helper.add_input(Submit('Submit', 'Submit', css_class='btn-primary'))


class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
 
class PostForm(forms.ModelForm):

    class Meta:
        model = FormTest
        fields = ('title', 'text',)

# Test forms from godjango.com
# class SimpleForm(forms.Form):
#     username = forms.CharField(label="Username", required=True)
#     password = forms.CharField(
#         label="Password", required=True, widget=forms.PasswordInput)
#     remember = forms.BooleanField(label="Remember Me?")

#     helper = FormHelper()
#     helper.form_method = 'POST'
#     helper.add_input(Submit('login', 'login', css_class='btn-primary'))

# class CartForm(forms.Form):
#     item = forms.CharField()
#     quantity = forms.IntegerField(label="Qty")
#     price = forms.DecimalField()

#     helper = FormHelper()
#     helper.form_method = 'POST'
#     helper.layout = Layout(
#         'item',
#         PrependedText('quantity', '#'),
#         PrependedAppendedText('price', '$', '.00'),
#         FormActions(Submit('login', 'login', css_class='btn-primary'))
#     )


# class CreditCardForm(forms.Form):
#     fullname = forms.CharField(label="Full Name", required=True)
#     card_number = forms.CharField(label="Card", required=True, max_length=16)
#     expire = forms.DateField(label="Expire Date", input_formats=['%m/%y'])
#     ccv = forms.IntegerField(label="ccv")
#     notes = forms.CharField(label="Order Notes", widget=forms.Textarea())

#     helper = FormHelper()
#     helper.form_method = 'POST'
#     helper.form_class = 'form-horizontal'
#     helper.label_class = 'col-sm-2'
#     helper.field_class = 'col-sm-4'
#     helper.layout = Layout(
#         Field('fullname', css_class='input-sm'),
#         Field('card_number', css_class='input-sm'),
#         Field('expire', css_class='input-sm'),
#         Field('ccv', css_class='input-sm'),
#         Field('notes', rows=3),
#         FormActions(Submit('purchase', 'purchase', css_class='btn-primary'))
#     )