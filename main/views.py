from django.shortcuts import render
from django.views.generic import ListView

from .models import Trainig
# Create your views here.

class MainPage(ListView):
    paginate_by = 1
    model = Trainig
    template_name = 'index.html'
    context_object_name = 'trainig'

