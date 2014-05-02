#!/usr/bin/env python

#import json
import launchkey
#from pprint import pprint

from django.conf import settings


PRIVATE_KEY = open(settings.LAUNCHKEY_PRIVATE_KEY, 'r').read()


class LaunchKeyClient:
    """
    Wrap launchkey api in django client
    """
    def __init__(self, auth_request=None, auth=None):
        self.api = launchkey.API(
            settings.LAUNCHKEY_APP_KEY,
            settings.LAUNCHKEY_SECRET_KEY,
            PRIVATE_KEY
        )
        self.auth_request = auth_request
        self.auth = auth

    def authorize(self, username):
        response = self.api.authorize(username, True)
        if isinstance(response, dict):
            self.auth_request = response.get('auth_request', None)
        else:
            self.auth_request = response
        return self.auth_request

    def poll_request(self):
        if self.auth_request:
            response = self.api.poll_request(self.auth_request)
            self.auth = response.get('auth', None)
            self.user_hash = response.get('user_hash', None)
        else:
            response = None
        return response

    def is_authorized(self):
        if not self.auth_request and self.auth:
            return None
        response = self.api.is_authorized(self.auth_request, self.auth)
        return response

    def logout(self):
        if not self.auth_request:
            return None
        response = self.api.logout(self.auth_request)
        return response

    def deorbit(self, deorbit, signature):
        response = self.api.deorbit(deorbit, signature)
        return response
