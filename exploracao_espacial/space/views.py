from django.shortcuts import render
from django.views.generic import base
# Create your views here.

class HomeView(base.TemplateView):
    template_name = "home.html"

class PhilaeView(base.TemplateView):
    template_name = "philae.html"
