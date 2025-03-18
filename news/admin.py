from django.contrib import admin
from news.models import News

@admin.register(News)
class AdminNews(admin.ModelAdmin):
    list_display=[
        'news_title',
        'news_describe',
        'id',
        'news_image',
    ]
    search_fields=['id','news_title']
    ordering=['id']
    list_filter=['news_title']
 
