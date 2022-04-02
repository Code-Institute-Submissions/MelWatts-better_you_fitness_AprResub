from django.contrib import admin
from .models import Stories, Comment

# Register your models here.


class StoriesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'image_before',
        'image_after',
    )

    ordering = ('name',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'created_on', 'story',)
    list_filter = ('created_on',)
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


admin.site.register(Stories, StoriesAdmin)
admin.site.register(Comment, CommentAdmin)
