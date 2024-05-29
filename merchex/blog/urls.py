# Dans urls.py de votre application
from django.conf import settings
from django.urls import path, include
from . import views
from .views import BlogList
from .views import BlogNotes
from .views import BlogProject

# from .views import BlogList
# from .views import VueAppView
from django.views.generic import TemplateView

app_name = "blog"

urlpatterns = [
    path('post/', BlogList.as_view(), name='post_list'),
    path('moi', views.Blog_Profil, name='blog_profil'),
    path('projets/', BlogProject.as_view(), name='blog_projects'),
    path('notes/', BlogNotes.as_view(), name='blog_Notes'),
    path('comment_ont_fait', views.Blog_How, name='blog_How'),
    path('labo', views.Blog_Lab, name='blog_Labo'),
    # path('spotify', views.Spotify_Playlist, name='spotify')
    # path('', VueAppView.as_view(), name='app'),


]
