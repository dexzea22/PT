from django.contrib import admin
from .models import ContactMessage

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('name', 'email', 'subject', 'message', 'timestamp')
    ordering = ('-timestamp',)

admin.site.register(ContactMessage, ContactMessageAdmin)
