from django.urls import path
from .views import (
    postView,
    about,
    blog_post
)

urlpatterns = [
    path('', postView),
    path('about/',about),
    path('blog/',blog_post),
]
