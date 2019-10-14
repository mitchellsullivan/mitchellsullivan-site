from django.views.generic import TemplateView
from django.shortcuts import render
from django.utils import timezone
from .models import Post

class HomePageView(TemplateView):
    model = Post
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.order_by('-post_date')[:1]
        context['year'] = timezone.now().year
        return context

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


