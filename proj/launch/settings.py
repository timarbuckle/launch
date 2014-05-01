"""
Django settings for launch project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r6^2edgvlg3c0iwmitutn(u=_t0(c6ahk^al^&6(*4q$!u1i8d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'launch.urls'

WSGI_APPLICATION = 'launch.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

LAUNCHKEY_APP_KEY = '3186808161'
LAUNCHKEY_SECRET_KEY = '4if154ochz9th2a8mz3l0raakc4o6bf1'
LAUNCHKEY_PRIVATE_KEY = """
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAtGGAsSybah0ABkHTNoxplKNLLzXIlcnd/IqGF+pIWMpowkKY
IFPZWIeva6qP+iW9XSPfF6vtfuDOUpzFsmEaM16M/BuIs5yZK4VSmATBpiaociUB
/b2FjZpDV4oA/5M5em2H4o4uMjV8+5FR+i6OGPS5ASx3pWiRhVkFUpiO21KWLM0Y
4vxd486KYvSa9CCRc1xrG0DwmA1GhA1etGITw1cE454oWPb3CDFisGml370LARaa
+CeBUoVoVmP0N+/+UYkgp7rrDSiRDfoXnCknLn571S9XLazGZobXZPL/mVjefuDs
835nPNBiFZmYCtFpo1Cpc3G8W7nX0xUdCozvqwIDAQABAoIBAGOBehXC7sUd1Fqf
S13HHaNCZYJYoBuJba0X2ZstwdVBa4Lma7dBqh99UlcJkz1CPnE4DaSoUm5wo0DN
fP3HNUXrPckBg2rZ02E/ve1gilcW8kttgOix+Q/Bbq7G0YArfkS8UX64QmGuQhEg
/GEP95FqxvgPyLz1r3kpP5dt0zjHK+5+bCnM4pRaZBxzWrLLYdg9MyTXkJtEq6EV
ZpSqnmwtms2jzVCSnU+XFlYssye6t+umX2MkOHdxEZVfY82/grEZpLrheUbqsKMx
Hr6KC6X/fTowHIuhfTkYdaimONEjvHN1zm52wk26Mhl6xsOHHp7jrjKgESpySogx
QqU48GkCgYEA4g6do1iAZSh23yOsB/9+bstNGs9JeRPnwVvUeCSaBEPW25U+Id6M
sQaT7KeGXX0U7u/qNzSG/OQMcoQd/tFeGd4wwmR9MIhPkvESfiEX5LtqeRsbfsC7
+2U0aGAthY19gs2yKXEsIjNP09y7MXv1ALbRQAPdGlXexs7YZ559Ll0CgYEAzEYM
i4pDsGIkofyBlt7PH6ZU7KcCZZL3FWRgEz/dHJ0QTXs40zrvL1pJr6MOMs51fzvu
/z0IqR0UWlySoz7oKhS57LGP2mUYuZVrEO7NEWuV4cnLg8RI4cJoz7krEJYPa7Nu
v6BzImLh3wajC7pKKFEJ9yrWEe9JCOmV7j5tZacCgYAi2Sv1/XO1pHpGxeIETZ+5
BsA5LNFfx/DHPxfO+Z2AoNCjgytT31IDDEeLiPvOt7SdbQDHR+KzY5iDothY6v+9
ryIHJaSi8bCKr30xUnqzeSzdxI8FiEKya5Sbro/18azymDEp8FdkYlKhD3sQEtLf
LE+vtajFIY25SjPULXuQxQKBgB6zoIsQet/1wD/AbdG5JzRAkZ8H8upFTnGepnn+
LUNxr9OVY5ML1ostbMnDHg0wzqQS4/bku3p/bmGubDOw7r/0YYVbop1WeILcHD1t
RtEJdHt9EuN5CuMzjwE5eWmCxEqRq2GNwgA3EG+u1a6bjy3EEFVf0NDdQALg6LHo
HBUdAoGBAKu+GPrFkAidfdWR15cXxOWjKqeScc37Y19pm9wV2cpsAhhDF57aQ+OV
5XXaKctajO71tImQwifTUKd90DcQS+vTkpskHXr1imXg27jG4iocO7iVIpM10Nah
zjLQUJhr/F4psyxoWNoEqKO1IjeaH+9SqAcJEQeDtJvQsaf7ALQx
-----END RSA PRIVATE KEY-----
"""
