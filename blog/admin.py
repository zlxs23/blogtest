from django.contrib import admin

# Register your models here.
from blog.models import *
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','created',)
    list_editable = ('title',)
    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )
class CommentAdmin(admin.ModelAdmin):
    list_display = ('article','date_publish',)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment,CommentAdmin)

