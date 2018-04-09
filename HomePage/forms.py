from django import forms

from HomePage.models import CustomerOrderModel


class Customer(forms.ModelForm):
    class Meta:
        model = CustomerOrderModel
        fields = ['customer_name', 'customer_location', 'customer_note', 'customer_deliver_date',
                  'customer_deliver_time', 'customer_phone_number']

    TEXTINPUT = {
        'class': 'form-control',
        'id': 'customer_name',
        'type': 'text',
        'placeholder': '',
        'value': '',
        'required': 'True',
    }
    TEXTAEATINPUT = {
        'class': 'form-control',
        'id': 'customer_note',
        'type': 'text',
        'placeholder': 'Your Note',
        'value': '',

    }
    NUMBERINPUT = {
        'class': 'form-control',
        'type': 'tel',
        'id': 'phone_number',
        'placeholder': '0551234567',
        'value': '',
        'required': 'required',
    }
    URLINPUT = {
        'class': 'form-control',
        'type': 'url',
        'id': 'address',
        'placeholder': 'https://goo.gl/maps/BLXKb9PXVJ72',
        'value': '',
        'required': 'required',

    }

    DATEPICKER = {
        'class': 'form-control',
        'type': 'date',
        'id': 'date',
        'required': 'true',

    }
    TIMEPICKER = {
        'class': 'form-control',
        'type': 'time',
        'id': 'time',
        'required': 'required',
    }

    EMAILINPUT = {
        'class': 'form-control',
        'id': 'email',
        'type': 'email',
        'placeholder': 'you@example.com',
        'value': '',

    }

    customer_name = forms.CharField(widget=forms.TextInput(attrs=TEXTINPUT))
    # customer_email = forms.EmailField(widget=forms.EmailInput(attrs=EMAILINPUT))
    customer_location = forms.URLField(widget=forms.TextInput(attrs=URLINPUT))
    customer_note = forms.CharField(widget=forms.Textarea(attrs=TEXTAEATINPUT))
    customer_deliver_date = forms.DateField(widget=forms.DateInput(attrs=DATEPICKER))
    customer_deliver_time = forms.TimeField(widget=forms.TimeInput(attrs=TIMEPICKER))
    customer_phone_number = forms.DecimalField(widget=forms.NumberInput(attrs=NUMBERINPUT))

    def clean_data(self):
        customer_name = self.cleaned_data.get('customer_name')
        customer_location = self.cleaned_data.get('customer_location')
        customer_note = self.cleaned_data.get('customer_note')
        customer_deliver_date = self.cleaned_data.get('customer_deliver_date')
        customer_deliver_time = self.cleaned_data.get('customer_deliver_time')
        customer_phone_number = self.cleaned_data.get('customer_phone_number')
        return customer_name, customer_location, customer_note, customer_deliver_date, customer_deliver_time, customer_phone_number
