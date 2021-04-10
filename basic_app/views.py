from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

# Create your views here.


class HomePageViews(View):
    def get(self, _request):
        return HttpResponse('Class-based views are cool!')