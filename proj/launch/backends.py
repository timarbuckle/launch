from django.contrib.auth.models import User

from .manager import LaunchManager


class LaunchKeyBackend:

    def authenticate(self, username, password='launchkey'):
        user, _ = User.objects.get_or_create(username=username)
        LaunchManager().authorize(user)
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
