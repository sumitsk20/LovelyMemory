from django import forms

from HomePage.models import CustomerOrder


class Customer(forms.ModelForm):
    customer_name = forms.CharField(label='Name', max_length=100)
    customer_location = forms.CharField(label='Location URL', max_length=500)

    class Meta:
        model = CustomerOrder
        fields = ['customer_name', 'customer_location']
