from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name="bloghome"),
    path('blogpost/<int:id>', views.blogpost, name="blogPost"),
]