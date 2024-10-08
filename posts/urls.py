from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),  # Change 'detail' to 'post_detail'
    path('new/', PostCreateView.as_view(), name='new'),
]
