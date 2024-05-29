from django.db import models
from django.utils import timezone
# from rest_framework import viewsets


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    class Language(models.TextChoices):
        PHP = 'PHP', 'PHP'
        JS = 'JS', 'JavaScript'
        PYTHON = 'PYTHON', 'Python'
        HTML = 'HTML', 'HTML'
        CSS = 'CSS', 'CSS'
        JAVA = 'JAVA', 'java'

    title = models.CharField(max_length=100)
    content = models.TextField()
    images = models.ImageField(blank=True, null=True, upload_to='blog/images')
    created_at = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    language = models.CharField(choices=Language.choices, max_length=10)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='posts', blank=True, null=True)
    

    def __str__(self):
        return self.title


class Project(models.Model):
    class Technology(models.TextChoices):
        HTML_CSS = 'HTML/CSS', 'HTML/CSS'
        PHP = 'PHP', 'PHP'
        JS = 'JS', 'JavaScript'
        PYTHON = 'PYTHON', 'Python'
        VUE = 'VUE', 'Vue.js'
        NODE = 'NODE', 'Node.js'
        SYMFONY = 'SYMFONY', 'Symfony'

    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.CharField(max_length=50, choices=Technology.choices)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='projects', blank=True, null=True)
    date_completed = models.DateField(blank=True, null=True)
    project_link = models.URLField(blank=True, null=True)
    image = models.ImageField(
        upload_to='project_images/', blank=True, null=True)

    def __str__(self):
        return self.title


# class PostViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Post.objects.all()
class Notes(models.Model):
    title = models.TextField()
    content = models.TextField()
    images = models.ImageField(blank=True, null=True)
    public = models.BooleanField(default=False)
    private = models.BooleanField(default=False)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='notes', blank=True, null=True)

    def __str__(self):
        return self.title
