from django.views.generic import TemplateView
from posts.models import Post

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_posts'] = Post.objects.order_by('-created_on')[:3]
        return context

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'
