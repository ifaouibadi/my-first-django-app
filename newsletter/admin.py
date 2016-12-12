from django.contrib import admin

# Register your models here.
from newsletter.models import SignUp


class SignUpAdmin(admin.ModelAdmin):
    list_display = ["email", "full_name", "created_at", "updated_at"]

    class Meta:
        model = SignUp


admin.site.register(SignUp, SignUpAdmin)
