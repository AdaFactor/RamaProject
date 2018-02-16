from django.forms import ModelForm, DateInput
from MemberApp.models import Member, Address
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, Field, Div
from crispy_forms.bootstrap import PrependedText, PrependedAppendedText, FormActions, StrictButton, InlineField


class DateInput(DateInput):
    input_type = 'date'


class RegistrationForm(ModelForm):
    class Meta:
        model = Member
        fields = [
        'prefix',
        'first_name',
        'last_name',
        'gender',
        'citizen_id',
        'date_birth',
        'address',
        'phone_no',
        'email',
        'reference_person',
        # 'relationship',
        'paid',
        'paid_date',
        ]
        widgets = {
            'date_birth': DateInput(),
            'paid_date': DateInput()
        }

    def __init__(self, request, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = ''
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            Div(
                Fieldset(
                    'New Member Registration',
                    Field(
                        'prefix',
                        'first_name',
                        'last_name',
                        'gender',
                        'citizen_id',
                        'date_birth',
                        'address',
                        'phone_no',
                        'email',
                        'reference_person',
                        # 'relationship',
                        'paid',
                        'paid_date',
                    ),
                    Submit('submit', 'Submit', css_class='btn btn-success btn-block')
                ),
            ),
        )
