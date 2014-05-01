
import logging

from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import View

from .models import LaunchKeyModel


logger = logging.getLogger()


"""
[01/May/2014 18:29:47] "POST /launch/auth?auth_request=occ1h35onzjr24e0dpwz5hqbbef7wqj3&user_hash=oXwQPwtqmtAQodXwMpj3c0oNTMDMR4feMWE9j2a94SU&auth=Y0RbKB1T8GomYaYisiXJLQQXpgYHdRPH5TCYP8nifOssf0ghp8sO2iM4tQ9uxdFb%0D%0AOJDmP1s7nHXvRrSYgDnOw%5C%2FgKkG0eLsmfX%2BF%5C%2Fj%5C%2F35THgp5YyKvGJ8aCGCH20yOLl%2B%0D%0AczhBGh9rhO7sxpESFNJPgkCxV%2BQrKo%2BH92ZAF5zNXkS1CD5fGvmvhf9DMWQTktMi%0D%0AgrVzXhmGOnYong%2BRyLp04wBbhN9fUo5FMGZlzT5DRD2slyTnSHa2ns76D9FtjKPm%0D%0Ad9IhyqSo7NBbXWhv1fWpBSgDzL1eG5KM5MiJSC0jpUszaIVt0AxXXiKOrBGrIN8t%0D%0A%2B4G37eGCvdyXsoj%2BJHQ8UQ%3D%3D HTTP/1.0" 403 2282


[01/May/2014 18:33:01] "POST /launch/auth?deorbit=%7B%22launchkey_time%22%3A+%222014-05-01+18%3A33%3A00%22%2C+%22user_hash%22%3A+%22oXwQPwtqmtAQodXwMpj3c0oNTMDMR4feMWE9j2a94SU%22%7D&signature=Bz21ZVgPCRAPZfPFs26qBgelsOPPeX4AagVBKXIYJwJaLR2zpH9WT9dbLaGF3tLVD0E6a1GcPiib7Z9oZwZsRVaPVoIdYYId1Anpz6Weuo1dKw98oIXn%2F7uel5tmR7a2f3qh10dGgWXKB%2F4BVvSj4rU01zXwJUCPbABQs8cG4IuhKWFDPca7ysq4cdaoDm%2FaxOYdAN49puJD9t6F4kyY384PLo%2Bde5XwTgh%2BcHp%2B8jngORnwNpEIoUtLxQW3hcHTelmZctidqNDvAup4lEjDddklV5S6tgnIKHd%2FPmIjN%2BCrHZRGZDZpHNdqoN4bUsTOFbbp367xgc0zQEcbLIda%2Bw%3D%3D HTTP/1.0" 403 2282
"""


class HomeView(View):

    def _response(self, request):
        if request.user.is_authenticated():
            lk = LaunchKeyModel.objects.get(user=request.user)
            c = RequestContext(request, {'data':
                {
                    'username': request.user.username,
                    'auth_request': lk.auth_request,
                    'auth': lk.auth,
                    'user_hash': lk.user_hash,
                    'device_id': lk.device_id,
                    'app_pins': lk.app_pins
                }
            })
            return render(request, 'home.html', c)
        else:
            return render(request, 'home.html')

    def get(self, request, *args, **kwargs):
        return self._response(request)


class LoginView(View):

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username', None)
        if username:
            user = authenticate(username=username)
            if user is not None:
                login(request, user)
        return HttpResponseRedirect(reverse('home'))


class LogoutView(View):

    def post(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('home'))


class AuthView(View):

    def _auth_request(self, request, *args, **kwargs):
        logger.info('auth_request')
        logger.info(request.POST)
        return HttpResponseRedirect(reverse('home'))

    def _deorbit_request(self, request, *args, **kwargs):
        logger.info('deorbit')
        logger.info(request.POST)
        return HttpResponseRedirect(reverse('home'))

    def post(self, request, *args, **kwargs):
        import pdb; pdb.set_trace()
        auth_request = request.GET.get('auth_request', None)
        deorbit = request.GET.get('deorbit', None)

        if auth_request:
            return self._auth_request(request, *args, **kwargs)
        elif deorbit:
            return self._deorbit_request(request, *args, **kwargs)

        logger.warn('Unexpected auth request.\n%s' % request.GET)
        return HttpResponseRedirect(reverse('home'))
