from django.urls import path

from apps.views import CustomerView, CustomerAddView, CustomerDeleteView, CustomerUpdateView

urlpatterns = [
    path('', CustomerView.as_view(), name='index_page'),
    path('add/', CustomerAddView.as_view(), name='add_page'),
    path('delete/<int:pk>/', CustomerDeleteView.as_view(), name='customer_delete'),
    path('update/<int:pk>/', CustomerUpdateView.as_view(), name='customer_update')
]