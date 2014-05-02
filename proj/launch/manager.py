
from django.contrib.sessions.models import Session

from .client import LaunchKeyClient
from .models import LaunchKeyModel


class LaunchManager:

    def _get_lk(self, user):
        try:
            lk = LaunchKeyModel.objects.get(user=user)
        except LaunchKeyModel.DoesNotExist:
            lk = None
        return lk

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
        lk = self._get_lk(user)
        return lk.is_authorized()

    def poll_request(self, user):
        """
        call api poll_request
        """
        lk = self._get_lk(user)
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
        lk = self._get_lk(user)
        client = LaunchKeyClient(lk.auth_request)
        client.logout()
        lk.delete()

    def deorbit(self, deorbit, signature):
        client = LaunchKeyClient()
        user_hash = client.deorbit(deorbit, signature)
        try:
            lk = LaunchKeyModel.objects.get(user_hash=user_hash)
        except LaunchKeyModel.DoesNotExist:
            lk = None
        if lk:
            # clear session for this user
            [s.delete() for s in Session.objects.all()
             if s.get_decoded().get('_auth_user_id') == lk.user.id]
            client = LaunchKeyClient(lk.auth_request)
            client.logout()
            lk.delete()
