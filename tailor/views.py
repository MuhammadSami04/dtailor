from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.db.models import Count, Q

from .models import Customer, Measurement, Order, Payment
from .forms import CustomerForm, MeasurementForm, OrderForm, PaymentForm


def home(request):
    customers = Customer.objects.all()[:6]
    total_orders = Order.objects.count()
    active_orders = Order.objects.filter(status__in=['Pending', 'In Progress']).count()
    pending_payments = Payment.objects.none().count()
    
    context = {
        'customers': customers,
        'total_orders': total_orders,
        'active_orders': active_orders,
        'pending_payments': pending_payments,
    }
    return render(request, 'tailor/home.html', context)


# Customer views
class CustomerListView(generic.ListView):
    model = Customer
    template_name = 'tailor/customer_list.html'
    context_object_name = 'customers'


class CustomerCreateView(generic.CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'tailor/customer_form.html'
    success_url = reverse_lazy('customer-list')


class CustomerUpdateView(generic.UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'tailor/customer_form.html'
    success_url = reverse_lazy('customer-list')


class CustomerDeleteView(generic.DeleteView):
    model = Customer
    template_name = 'tailor/customer_confirm_delete.html'
    success_url = reverse_lazy('customer-list')


class CustomerDetailView(generic.DetailView):
    model = Customer
    template_name = 'tailor/customer_detail.html'


# Measurement views
class MeasurementListView(generic.ListView):
    model = Measurement
    template_name = 'tailor/measurement_list.html'
    context_object_name = 'measurements'


class MeasurementCreateView(generic.CreateView):
    model = Measurement
    form_class = MeasurementForm
    template_name = 'tailor/measurement_form.html'
    success_url = reverse_lazy('measurement-list')


class MeasurementUpdateView(generic.UpdateView):
    model = Measurement
    form_class = MeasurementForm
    template_name = 'tailor/measurement_form.html'
    success_url = reverse_lazy('measurement-list')


class MeasurementDeleteView(generic.DeleteView):
    model = Measurement
    template_name = 'tailor/measurement_confirm_delete.html'
    success_url = reverse_lazy('measurement-list')


class MeasurementDetailView(generic.DetailView):
    model = Measurement
    template_name = 'tailor/measurement_detail.html'


# Order views
class OrderListView(generic.ListView):
    model = Order
    template_name = 'tailor/order_list.html'
    context_object_name = 'orders'


class OrderCreateView(generic.CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'tailor/order_form.html'
    success_url = reverse_lazy('order-list')


class OrderUpdateView(generic.UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'tailor/order_form.html'
    success_url = reverse_lazy('order-list')


class OrderDeleteView(generic.DeleteView):
    model = Order
    template_name = 'tailor/order_confirm_delete.html'
    success_url = reverse_lazy('order-list')


class OrderDetailView(generic.DetailView):
    model = Order
    template_name = 'tailor/order_detail.html'


# Payment views
class PaymentListView(generic.ListView):
    model = Payment
    template_name = 'tailor/payment_list.html'
    context_object_name = 'payments'


class PaymentCreateView(generic.CreateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'tailor/payment_form.html'
    success_url = reverse_lazy('payment-list')


class PaymentUpdateView(generic.UpdateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'tailor/payment_form.html'
    success_url = reverse_lazy('payment-list')


class PaymentDeleteView(generic.DeleteView):
    model = Payment
    template_name = 'tailor/payment_confirm_delete.html'
    success_url = reverse_lazy('payment-list')


class PaymentDetailView(generic.DetailView):
    model = Payment
    template_name = 'tailor/payment_detail.html'
