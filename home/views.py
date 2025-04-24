from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from blog.models import Post


class HomePageView(TemplateView):
    template_name = "home\home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_posts'] = Post.objects.all().order_by('-post_date')[:6]
        return context