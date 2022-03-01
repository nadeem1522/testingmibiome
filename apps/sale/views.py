from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView


class SaleView(LoginRequiredMixin, TemplateView):
    template_name = 'sale/sale.html'