from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


class QuantiFGA(TemplateView):
    template_name = 'polls/index.html'

