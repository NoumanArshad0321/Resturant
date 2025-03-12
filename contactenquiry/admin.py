from django.contrib import admin
from contactenquiry.models import contactEnquiry

@admin.register(contactEnquiry)
class AdminContact(admin.ModelAdmin):
    list_display=[
        'name',
        'email',
        'phone',
        'websiteLink',
        'message',
        'id',
    ]

# Register your models here.
