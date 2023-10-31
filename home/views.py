from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import *

#def HomeView(request):
    # return render(request, template_name='home/home.html')

class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['custom_date'] = 'Доп информ.'
        return context

class BlogView(ListView):
    model = Article
    # template_name = 'home/blog.html'