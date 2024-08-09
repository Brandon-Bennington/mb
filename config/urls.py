from django.contrib import admin
from django.urls import include, path
from pages.views import HomePageView, AboutPageView  # Import from pages.views
from posts import views  # Import post views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomePageView.as_view(), name="home"),  # Home page
    path("about/", AboutPageView.as_view(), name="about"),  # About page
    path("posts/", include("posts.urls")),  # Include posts app URLs
]
