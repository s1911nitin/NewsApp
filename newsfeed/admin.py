from atexit import register
from django.contrib import admin
from .models import News

# Register your models here.

@admin.register(News)
class NewsAdminClass(admin.ModelAdmin):
    list_display = ["id","headline_number","title","description","news_image"]