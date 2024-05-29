from django.contrib import admin

from blog.models import Post
from blog.models import Project
from blog.models import Notes
# Register your models here.


class TutoAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'technologies',
        'category',
        'date_completed',
        'project_link',
        'image',

         )
         

class NotesAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'content',
        'images',
        'public',
        'private'

    )
admin.site.register(Post, TutoAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Notes, NotesAdmin)
