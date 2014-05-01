
from .client import LaunchKeyClient
from .models import LaunchKeyModel


class LaunchManager:

    def authorize(self, user):
        lk, _ = LaunchKeyModel.objects.get_or_create(user=user)
        client = LaunchKeyClient()
        lk.auth_request = client.authorize(user.username)
        lk.save()
