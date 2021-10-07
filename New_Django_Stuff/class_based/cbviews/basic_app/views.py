from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import  (TemplateView, View, ListView, DetailView,
                                   CreateView, UpdateView, DeleteView)
from . import models
# Create your views here

class IndexView(TemplateView):
    template_name = 'index.html'


class SchoolListView(ListView):
    model = models.School

class SchoolDetailView(DetailView):
    context_object_name = "school_details"
    model = models.School
    template_name = 'basic_app/school_details.html'

class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name','principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('basic_app:list')

























# class CBviews(View):
#     def get(self,request):
#         return HttpResponse("Hopefully it won't be as tough as this anymore")
#
# class IndexView(TemplateView):
#     template_name ='basic_app/index.html'
#
#     def get_context_data(self,**kwargs):
#         context =super().get_context_data(**kwargs)
#         context['inject_me'] = 'Basic Injection'
#         return context
