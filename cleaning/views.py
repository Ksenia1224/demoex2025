from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from cleaning.models import Order


class OrderListView(ListView):
    model = Order


class OrderCreateView(CreateView):
    model = Order
    fields = ['title', 'address', 'phone', 'date', 'service', 'payment']
    success_url = reverse_lazy('cleaning:order_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class OrderUpdateView(UpdateView):
    model = Order
    fields = ['title', 'address', 'phone', 'date', 'service', 'payment']
    success_url = reverse_lazy('cleaning:order_list')


class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy('cleaning:order_list')

