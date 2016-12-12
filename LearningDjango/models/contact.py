from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Contact(models.Model):
    email = models.EmailField()
    first_name = models.CharField()
    last_name = models.CharField()
    phone_number = models.CharField()
    message = models.TextField()
    reply_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.email
