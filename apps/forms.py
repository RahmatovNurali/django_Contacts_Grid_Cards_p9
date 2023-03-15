from django.forms import ModelForm, CharField, EmailField

from apps.models import Customer


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'phone_number', 'email', 'address', 'jobs', 'image')