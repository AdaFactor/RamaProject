from django.forms import ModelForm
from MemberApp.models import Member, Address

class RegistrationForm(ModelForm):
    class Meta:
        model = Member
        exclude = [
            'relationship',
            'paid',
            'paid_date',
        ]


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = '__all__'
