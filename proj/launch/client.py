#!/usr/bin/env python

import json
import launchkey
from pprint import pprint

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
            data = json.loads(response)
            self.auth_request = data.get('auth_request', None)
        else:
            self.auth_request = response
        return self.auth_request

    def poll_request(self):
        if self.auth_request:
            response = self.api.poll_request(self.auth_request)
            data = json.loads(response)
            pprint(data)
            self.auth = data.get('auth', None)
            self.user_hash = data.get('user_hash', None)
        else:
            data = None
        return data

    def is_authorized(self):
        if not self.auth_request and self.auth:
            return None
        response = self.api.is_authorized(self.auth_request, self.auth)
        self.authorized = json.loads(response)
        pprint(self.authorized)
        #return self.authorized.get('response') == 'true'
        return self.authorized

    def logout(self):
        if not self.auth_request:
            return None
        response = self.api.logout(self.auth_request)
        data = json.loads(response)
        pprint(data)
        return data

    def deorbit(self, deorbit, signature):
        response = self.api.deorbit(deorbit, signature)
        data = json.loads(response)
        pprint(data)
        return data
