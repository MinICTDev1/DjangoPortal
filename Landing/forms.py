from django import forms
from .models import Submision, FormTest

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Div, Button
from crispy_forms.bootstrap import FormActions, TabHolder, Tab, InlineRadios

class submissionForm(forms.ModelForm):
    '''Form to do with submission of proposals'''
    class Meta:
        '''Meta describing whihc model the class is being loaded from'''
        model = Submision
        fields = '__all__'
        widgets = {
            'individualBD': forms.DateInput(attrs={'id': 'datetimepicker4'}),
            'Commncementdate': forms.DateInput(attrs={'id': 'datetimepicker12'}),
            'company_regDate': forms.DateInput(attrs={'id': 'datetimepicker4'}),
            }

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
                    css_class='row-fluid'),
                Button('Next', 'Next', css_class="btnNext"),
               ),
            Tab('Introduction',
                'title',
                'probelemStatement',
                'background',
                'concept',
                Button('Previous', 'Previous', css_class="btnPrevious"),
                Button('Next', 'Next', css_class="btnNext")
               ),
            Tab('Owner',
                InlineRadios('ownership', id="radio_id"),
                # individual div
                Div(
                    Div('individual_NIN', css_class='col-xs-6'),
                    Div('individualBD', css_class='col-xs-6'),
                    css_class='row_fluid', css_id="id_ownership_1 box"),

                #Team Div
                Div(
                    Div('teamName', css_class='col-xs-6'),
                    Div('Commncementdate', css_class='col-xs-6'),
                    css_class='row_fluid'),

                # Company div
                Div(
                    Div('company_regDate', css_class='col-xs-12'),
                    css_class='row_fluid'),

                #Hub div
                Div(
                    Div('hubName', css_class='col-xs-6'),
                    Div('duration', css_class='col-xs-6'),
                    css_class='row_fluid'),

                Button('Previous', 'Previous', css_class="btnPrevious"),
                Button('Next', 'Next', css_class="btnNext")
               ),
            Tab('Details',
                Div(
                    Div('BusinessPlan', css_class='col-xs-12'),
                    css_class='row-fluid'),
                Div(
                    Div('FeasibilityStudy', css_class='col-xs-6'),
                    Div('StudyUpload', css_class='col-xs-6'),
                    css_class='row'),
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
                    Div('Amount_invested', css_class='col-xs-12'),
                    css_class='row-fluid'),
                Div(
                    Div(InlineRadios('Market_Study'), css_class='col-xs-12'),
                    css_class='row-fluid'),
                Div(
                    Div('Market_Std_Descrip', css_class='col-xs-8'),
                    Div('Market_STd_file', css_class='col-xs-4'),
                    css_class='row'),
                Div(
                    Div('Market', css_class='col-xs-8'),
                    Div('Value_Added', css_class='col-xs-4'),
                    css_class='row-fluid'),
                Div(
                    Div('Time_to_product', css_class='col-xs-12'),
                    css_class='row-fluid'),
                Div(
                    Div('End_User_Invol', css_class='col-xs-12'),
                    css_class='row-fluid'),
                Div(
                    Div('Monitoring', css_class='col-xs-12'),
                    css_class='row-fluid'),
                Div(
                    Div('Fund_Raise', css_class='col-xs-12'),
                    css_class='row-fluid'),
                Div(
                    Div(css_class='col-xs-12'),
                    css_class='row_fluid'),

                Button('Previous', 'Previous', css_class="btnPrevious"),
                Button('Next', 'Next', css_class="btnNext")
               ),
            Tab('Problems',
                'Problems',
                'Impacts',
                'Remedies',

                Button('Previous', 'Previous', css_class="btnPrevious"),
                Button('Next', 'Next', css_class="btnNext")
               ),
            Tab('Safety',
                'Safety',
                Button('Previous', 'Previous', css_class="btnPrevious"),
                Button('Next', 'Next', css_class="btnNext")
               ),
            Tab('Future',
                'Locations',
                'Sustainability',
                'MultiCultural',
                Button('Previous', 'Previous', css_class="btnPrevious"),
                Div(
                    Div(css_class='col-xs-4'),
                    Div(FormActions(Submit('Submit', 'Submit', css_class='btn-primary'))),
                    css_class='row-fluid'),
               ),
            )
    )


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
 