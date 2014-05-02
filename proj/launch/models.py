from django.db import models
from django.contrib.auth.models import User


class LaunchKeyModel(models.Model):
    user = models.ForeignKey(User)
    auth_request = models.CharField(max_length=60, unique=True)
    auth = models.CharField(max_length=255)
    user_hash = models.CharField(max_length=60)
    device_id = models.CharField(max_length=20)
    app_pins = models.CharField(max_length=60)
    authorized = models.BooleanField(default=False)

    def is_authorized(self):
        return self.authorized

    def authorize(self):
        self.authorized = True
        self.save()

    def deauthorize(self):
        self.authorized = False
        self.save()

    def __unicode__(self):
        return '%s %s' % (self.user, self.auth_request)
