from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # customer urls
    path('customers/', views.CustomerListView.as_view(), name='customer-list'),
    path('customers/add/', views.CustomerCreateView.as_view(), name='customer-add'),
    path('customers/<int:pk>/edit/', views.CustomerUpdateView.as_view(), name='customer-edit'),
    path('customers/<int:pk>/delete/', views.CustomerDeleteView.as_view(), name='customer-delete'),
    path('customers/<int:pk>/', views.CustomerDetailView.as_view(), name='customer-detail'),

    # measurement urls
    path('measurements/', views.MeasurementListView.as_view(), name='measurement-list'),
    path('measurements/add/', views.MeasurementCreateView.as_view(), name='measurement-add'),
    path('measurements/<int:pk>/edit/', views.MeasurementUpdateView.as_view(), name='measurement-edit'),
    path('measurements/<int:pk>/delete/', views.MeasurementDeleteView.as_view(), name='measurement-delete'),
    path('measurements/<int:pk>/', views.MeasurementDetailView.as_view(), name='measurement-detail'),

    # order urls
    path('orders/', views.OrderListView.as_view(), name='order-list'),
    path('orders/add/', views.OrderCreateView.as_view(), name='order-add'),
    path('orders/<int:pk>/edit/', views.OrderUpdateView.as_view(), name='order-edit'),
    path('orders/<int:pk>/delete/', views.OrderDeleteView.as_view(), name='order-delete'),
    path('orders/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),

    # payment urls
    path('payments/', views.PaymentListView.as_view(), name='payment-list'),
    path('payments/add/', views.PaymentCreateView.as_view(), name='payment-add'),
    path('payments/<int:pk>/edit/', views.PaymentUpdateView.as_view(), name='payment-edit'),
    path('payments/<int:pk>/delete/', views.PaymentDeleteView.as_view(), name='payment-delete'),
    path('payments/<int:pk>/', views.PaymentDetailView.as_view(), name='payment-detail'),
]
