from django.contrib import admin

# Register your models here.
from contact.forms import ContactForm
from contact.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ["email", "first_name", "last_name", "created_at", "reply_status", "updated_at"]
    form = ContactForm


admin.site.register(Contact, ContactAdmin)
