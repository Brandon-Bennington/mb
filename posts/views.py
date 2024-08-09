from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)
from .models import Post

class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post
    context_object_name = 'posts'

class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)  # Debugging output
        return context


class PostCreateView(CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "subtitle", "body"]
