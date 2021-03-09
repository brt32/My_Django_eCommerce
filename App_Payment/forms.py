from django import forms
from App_Payment.models import BillingAddress


class BillingForm(forms.ModelForm):
    class Meta:
        model = BillingAddress
        fields = '__all__'
