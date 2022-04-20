from django.db import models
from django.contrib.auth.models import User
import uuid

class profile(models.Model):
    email = models.EmailField(max_length=100)
    token = models.CharField(default='', max_length=1000)
    is_verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.email

    def save(self, *args, **kwargs):
        self.token = str(uuid.uuid4())
        super(profile, self).save(*args, **kwargs)

