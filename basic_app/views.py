from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import School


class IndexView(TemplateView):
    template_name = 'index.html'


class SchoolListView(ListView):
    model = School
    context_object_name = 'schools'


class SchoolDetailView(DetailView):
    model = School
    template_name = 'basic_app/school_detail.html'
