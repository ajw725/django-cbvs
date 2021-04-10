from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import School


class IndexView(TemplateView):
    template_name = 'index.html'


class SchoolListView(ListView):
    model = School
    context_object_name = 'schools'


class SchoolDetailView(DetailView):
    model = School
    template_name = 'schools/school_detail.html'


class SchoolCreateView(CreateView):
    model = School
    fields = ('name', 'principal', 'location')


class SchoolUpdateView(UpdateView):
    model = School
    fields = ('name', 'principal')


class SchoolDeleteView(DeleteView):
    model = School
    success_url = reverse_lazy('schools:list')
