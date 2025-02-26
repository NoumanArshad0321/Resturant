from django.contrib import admin
from .models import Service

@admin.register(Service)
class AdminServices(admin.ModelAdmin):
    list_display = [
        "id",
        "service_name",
        "service_title",
        "service_des"
    ]
    search_fields=['id','service_name']
    ordering=['id']
    list_filter=['service_title']