from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Post , Comment


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ['title','draft','author']
    list_filter = ['draft','author']
    search_fields = ['title','content']


class CommentAdmin(admin.ModelAdmin):
    list_display =['user','post','created_at']
    list_filter =['user']
    


admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
