
from .client import LaunchKeyClient
from .models import LaunchKeyModel


class LaunchManager:

    def authorize(self, user):
        """
        call api authorize, return auth_request
        """
        lk, _ = LaunchKeyModel.objects.get_or_create(user=user)
        client = LaunchKeyClient()
        lk.auth_request = client.authorize(user.username)
        lk.save()

    def is_authorized(self, user):
        """
        return authorized state in db
        """
        try:
            lk = LaunchKeyModel.objects.get(user=user)
        except LaunchKeyModel.DoesNotExist:
            return False
        return lk.is_authorized()

    def poll_request(self, user):
        """
        call api poll_request
        """
        try:
            lk = LaunchKeyModel.objects.get(user=user)
        except LaunchKeyModel.DoesNotExist:
            return None
        client = LaunchKeyClient(lk.auth_request)
        status = client.poll_request()
        if 'auth' in status:
            lk.auth = status['auth']
            lk.save()
            lk.authorize()
        if 'user_hash' in status:
            lk.user_hash = status['user_hash']
            lk.save()
        return status

    def logout(self, user):
        """
        send logout via api, update database status
        """
        lk = LaunchKeyModel.objects.get(user=user)
        client = LaunchKeyClient(lk.auth_request)
        client.logout()
        lk.delete()

    def deorbit(self, deorbit, signature):
        client = LaunchKeyClient()
        client.deorbit(deorbit, signature)
