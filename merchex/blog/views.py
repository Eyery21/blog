from django.shortcuts import render
from django.http import JsonResponse

from .models import Post
from .models import Project
from .models import Notes
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostSerializer
from .serializers import NotesSerializer
from .serializers import ProjectSerializer
# import spotipy
from django.conf import settings

# from spotipy.oauth2 import SpotifyOAuth

from .spotify import get_spotify_token, get_spotify_playlist


class BlogList(APIView):
    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

def vue_index(request):
    return render(request, "app.html")


def Blog_Profil(request):
    return render(request, 'posts/moi.html')


class BlogProject(APIView):
    def get(self, request, format=None):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

        
class BlogNotes(APIView):
    def get(self, request, format=None):
        notes = Notes.objects.all()
        serializer = NotesSerializer(notes, many=True)
        return Response(serializer.data)


def Blog_How(request):
    post = Post.objects.all()  # Récupérer tous les tutoriels
    return render(request, 'posts/explains.html', {'posts': post})


def Blog_Lab(request):
    return render(request, 'posts/labo.html')
