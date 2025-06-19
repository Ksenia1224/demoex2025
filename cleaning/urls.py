from django.urls import path

from cleaning.views import OrderListView, OrderCreateView, OrderUpdateView, OrderDeleteView

app_name = 'cleaning'

urlpatterns = [
    path('list/', OrderListView.as_view(template_name='cleaning/order_list.html'), name='order_list'),
    path('create/', OrderCreateView.as_view(template_name='cleaning/order_form.html'), name='order_create'),
    path('update/<int:pk>/', OrderUpdateView.as_view(template_name='cleaning/order_form.html'), name='order_update'),
    path('delete/<int:pk>/', OrderDeleteView.as_view(template_name='cleaning/order_confirm_delete.html'), name='order_delete'),
]