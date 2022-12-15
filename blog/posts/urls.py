from django.contrib import admin
from django.urls import path
from posts import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(
        route='blog',
        view=views.PostsFeedView.as_view(),
        name='Blog'
    ),
    path(
        route='posts/<pk>/',
        view=views.PostDetailView.as_view(),
        name='details'
    ),
    path(
        route='posteo/',
        view=views.CreatePostView.as_view(),
        name='posteo'
    ),

    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)