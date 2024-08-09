from django.urls import path
from posts import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='list'),  # For listing posts
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),  # For detailed view of a single post
]
