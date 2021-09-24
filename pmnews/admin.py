from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin

# Register your models here.
from .models import Post
from django_summernote.utils import get_attachment_model


class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)
    # exclude = ['slug']
    list_display = ('title', 'slug', 'status', 'created_on',)
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}



admin.site.register(Post, PostAdmin)
# admin.site.unregister(get_attachment_model())
