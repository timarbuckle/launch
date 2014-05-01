#!/usr/bin/env python

import launchkey

from django.conf import settings


class LaunchKeyClient:
    """
    Wrap launchkey api in django client
    """
    def __init__(self):
        self.api = launchkey.API(
            settings.LAUNCHKEY_APP_KEY,
            settings.LAUNCHKEY_SECRET_KEY,
            settings.LAUNCHKEY_PRIVATE_KEY
        )

    def authorize(self, username):
        response = self.api.authorize(username, True)
        self.auth_request = response.get('auth_request', None)
        return response

    def poll_request(self):
        if self.auth_request:
            response = self.api.poll_request(self.auth_request)
            self.auth = response.get('auth', None)
            self.user_hash = response.get('user_hash', None)
        else:
            response = None
        return response

    def is_authorized(self):
        self.authorized = self.api.is_authorized(self.auth_request, self.auth)
        return self.authorized.get('response') == 'true'

    def logout(self):
        self.api.logout(self.auth_request)

    def deorbit(self, deorbit, signature):
        return self.api.deorbit(deorbit, signature)
