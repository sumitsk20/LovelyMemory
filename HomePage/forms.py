from django import forms

from HomePage.models import CustomerOrder


class Customer(forms.ModelForm):
    customer_name = forms.CharField(label='Name', max_length=100)
    customer_location = forms.URLField(label='Location URL', max_length=500)
    customer_request = forms.CharField(max_length=1000)
    customer_deliver = forms.DateTimeInput()

    class Meta:
        model = CustomerOrder
        fields = ['customer_name', 'customer_location']
