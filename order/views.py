from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView

from catalog.models import Product
from order.models import Order
from order.services import send_order_email


class OrderCreateView(CreateView):
    model = Order
    fields = ('product', 'name', 'email', 'message',)

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk'), ])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = get_object_or_404(Product,
                                               pk=self.kwargs.get('pk'))
        return context

    def form_valid(self, form):
        obj = form.save()
        send_order_email(obj)
        return super().form_valid(form)
