
import logging

from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

#from .client import LaunchKeyClient
from .manager import LaunchManager
from .models import LaunchKeyModel


logger = logging.getLogger()


class CsrfDisableView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(CsrfDisableView, self).dispatch(*args, **kwargs)


class HomeView(CsrfDisableView):

    def _response(self, request):
        if request.user.is_authenticated():
            mgr = LaunchManager()
            is_auth = mgr.is_authorized(request.user)
            if is_auth:
                prstatus = {'message': 'Authorized'}
            else:
                prstatus = mgr.poll_request(request.user)
            logger.warn('poll request status: %s' % prstatus)
            lk = LaunchKeyModel.objects.get(user=request.user)
            c = RequestContext(request, {
                'username': request.user.username,
                'auth_request': lk.auth_request,
                'auth': lk.auth,
                'user_hash': lk.user_hash,
                'is_authorized': is_auth,
                'device_id': lk.device_id,
                'app_pins': lk.app_pins,
                'authorized': lk.is_authorized(),
                'poll_request_status': prstatus.get('message', 'Good')
            })
            return render(request, 'home.html', c)
        else:
            return render(request, 'home.html')

    def get(self, request, *args, **kwargs):
        return self._response(request)


class LoginView(CsrfDisableView):

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username', None)
        if username:
            user = authenticate(username=username)
            if user is not None:
                login(request, user)
        return HttpResponseRedirect(reverse('home'))


class LogoutView(CsrfDisableView):

    def post(self, request, *args, **kwargs):
        mgr = LaunchManager()
        mgr.logout(request.user)
        logout(request)
        return HttpResponseRedirect(reverse('home'))


class AuthView(CsrfDisableView):

    def _auth_request(self, request, auth_request, *args, **kwargs):
        try:
            lk = LaunchKeyModel.objects.get(auth_request=auth_request)
        except LaunchKeyModel.DoesNotExist:
            lk = None
        ## check is_authorized, store auth response
        lk.is_authorized = True
        lk.auth = request.GET.get('auth')
        lk.user_hash = request.GET.get('user_hash')
        lk.save()

    def _deorbit_request(self, request, deorbit, *args, **kwargs):
        signature = request.GET.get('signature', None)
        #user_hash = deorbit.get('user_hash', None)
        #launchkey_time = deorbit.get('launchkey_time', None)
        mgr = LaunchManager()
        mgr.deorbit(deorbit, signature)

    def post(self, request, *args, **kwargs):
        auth_request = request.GET.get('auth_request', None)
        deorbit = request.GET.get('deorbit', None)

        if auth_request:
            self._auth_request(request, auth_request, *args, **kwargs)
        elif deorbit:
            self._deorbit_request(request, deorbit, *args, **kwargs)
        else:
            logger.warn('Unexpected auth request.\n%s' % request.GET)
        return HttpResponse()
