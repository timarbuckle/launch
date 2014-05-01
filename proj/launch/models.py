from django.db import models
from django.contrib.auth.models import User


class LaunchKeyModel(models.Model):
    user = models.ForeignKey(User)
    auth_request = models.CharField(max_length=60)
    auth = models.CharField(max_length=255)
    user_hash = models.CharField(max_length=60)
    device_id = models.CharField(max_length=20)
    app_pins = models.CharField(max_length=60)
