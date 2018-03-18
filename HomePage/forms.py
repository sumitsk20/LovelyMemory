from django import forms

from HomePage.models import CustomerOrderModel


class Customer(forms.ModelForm):
    class Meta:
        model = CustomerOrderModel
        fields = ['customer_name', 'customer_location', 'customer_note', 'customer_deliver_date',
                  'customer_deliver_time', 'customer_phone_number']

    TEXTINPUT = {
        'class': 'form-control',
        'type': 'text'
    }
    NUMBERINPUT = {
        'class': 'form-control',
        'type': 'tel'
    }
    URLINPUT = {
        'class': 'form-control',
        'type': 'url'
    }
    DATEPICKER = {
        'class': 'form-control',
        'type': 'date',
        'id': 'datetimepicker4'
    }
    TIMEPICKER = {
        'class': 'form-control',
        'type': 'time',
    }
    customer_name = forms.CharField(widget=forms.TextInput(attrs=TEXTINPUT))
    customer_location = forms.URLField(widget=forms.TextInput(attrs=URLINPUT))
    customer_note = forms.CharField(widget=forms.Textarea(attrs=TEXTINPUT))
    customer_deliver_date = forms.DateField(widget=forms.DateTimeInput(attrs=DATEPICKER))
    customer_deliver_time = forms.TimeField(widget=forms.DateTimeInput(attrs=TIMEPICKER))
    customer_phone_number = forms.DecimalField(widget=forms.NumberInput(attrs=NUMBERINPUT))

    def clean_data(self):
        customer_name = self.cleaned_data.get('customer_name')
        customer_location = self.cleaned_data.get('customer_location')
        customer_note = self.cleaned_data.get('customer_note')
        customer_deliver_date = self.cleaned_data.get('customer_deliver_date')
        customer_deliver_time = self.cleaned_data.get('customer_deliver_time')
        customer_phone_number = self.cleaned_data.get('customer_phone_number')
        return customer_name, customer_location, customer_note, customer_deliver_date, customer_deliver_time, customer_phone_number
