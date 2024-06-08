from django.contrib import admin

from blog.models import Post
from blog.models import Project
from blog.models import Notes
# Register your models here.


class TutoAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'description',
        'language',
        'frameworkfront',
        'frameworkback',
        'new',
        'date_completed',
        'project_link',
        'image',

    )


class NotesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'content',
        'images',
        'public',
        'private'

    )

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'content',
        'images',
        'created_at',
        'like',
        'dislike',
        'language',
        'category'
    )


admin.site.register(Post, PostAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Notes, NotesAdmin)
