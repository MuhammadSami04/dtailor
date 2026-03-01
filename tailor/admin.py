from django.contrib import admin
from .models import Customer, Measurement, Order, Payment

admin.site.register(Customer)
admin.site.register(Measurement)
admin.site.register(Order)
admin.site.register(Payment)