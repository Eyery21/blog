# Dans urls.py de votre application
from django.conf import settings
from django.urls import path, include
from . import views
from .views import BlogPost, BlogNotes, BlogProject


from django.conf.urls.static import static

from django.conf import settings

# from .views import BlogList
# from .views import VueAppView
from django.views.generic import TemplateView

app_name = "blog"

urlpatterns = [
    path('post/', BlogPost.as_view(), name='post_list'),
    path('moi', views.Blog_Profil, name='blog_profil'),
    path('projets/', BlogProject.as_view(), name='blog_projects'),
    path('notes/', BlogNotes.as_view(), name='blog_Notes'),
    path('comment_ont_fait', views.Blog_How, name='blog_How'),
    path('labo', views.Blog_Lab, name='blog_Labo'),
    # path('', BlogIndex.as_view(), name='index'),

    # path('spotify', views.Spotify_Playlist, name='spotify')
    # path('', VueAppView.as_view(), name='app'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))] + urlpatterns
