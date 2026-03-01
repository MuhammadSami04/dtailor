from django import forms
from .models import Customer, Measurement, Order, Payment


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'address', 'gender']


class MeasurementForm(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = ['customer', 'chest', 'waist', 'shoulder', 'arm_length', 'shalwar_length', 'collar']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'dress_type', 'fabric_provided', 'total_price', 'advance_payment', 'delivery_date', 'status']


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['order', 'amount_paid']
