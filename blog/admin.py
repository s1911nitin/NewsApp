from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)
class PostAdminClass(admin.ModelAdmin):
    list_display = ["id","title","desc","post_image","user"]

