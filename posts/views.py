from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)
from .models import Post

class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post
    context_object_name = 'post_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Use the same query as in the homepage
        context['post_list'] = Post.objects.order_by('-created_on')  # Fetch all posts
        print("PostListView Context:", context)  # Debugging output
        return context




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
