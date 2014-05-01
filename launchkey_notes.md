# LaunchKey Notes

These are some of the things I noticed while developing my app.

## iOS App

The iOS app shows "Swipe right for tutorial" but the user actually must
swipe left.

## Python SDK

On Github, the installation instructions via pip show

    $ pip launchkey-python

The command should be

    $ pip install launchkey-python

Same problem on https://launchkey.com/docs/sdk/python/

## PIP Install on OSX

Running the above pip install command on my mac
resulted in the following error:

```
running build_configure

warning: GMP or MPIR library not found; Not building Crypto.PublicKey._fastmath.

building 'Crypto.Hash._MD2' extension

cc -fno-strict-aliasing -fno-common -dynamic -arch x86_64 -arch i386 -pipe -fno-common -fno-strict-aliasing -fwrapv -mno-fused-madd -DENABLE_DTRACE -DMACOSX -Wall -Wstrict-prototypes -Wshorten-64-to-32 -fwrapv -Wall -Wstrict-prototypes -DENABLE_DTRACE -arch x86_64 -arch i386 -pipe -std=c99 -O3 -fomit-frame-pointer -Isrc/ -I/System/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7 -c src/MD2.c -o build/temp.macosx-10.9-intel-2.7/src/MD2.o

clang: error: unknown argument: '-mno-fused-madd' [-Wunused-command-line-argument-hard-error-in-future]

clang: note: this will be a hard error (cannot be downgraded to a warning) in the future

error: command 'cc' failed with exit status 1

----------------------------------------
Command /Users/tim/projects/launchkey/env/bin/python -c "import setuptools;__file__='/Users/tim/projects/launchkey/env/build/pycrypto/setup.py';exec(compile(open(__file__).read().replace('\r\n', '\n'), __file__, 'exec'))" install --record /var/folders/gj/565xs7nx7hjfwl3v91168zf00000gn/T/pip-PPGqWw-record/install-record.txt --single-version-externally-managed --install-headers /Users/tim/projects/launchkey/env/include/site/python2.7 failed with error code 1 in /Users/tim/projects/launchkey/env/build/pycrypto
Storing complete log in /Users/tim/.pip/pip.log
```

Fortunately, running this on Ubuntu Linux was successful.


## Convert RSA key to PEM

The following command command can be used to convert the RSA Private Key to
a PEM file for use by the python API.

    openssl rsa -in LaunchKey.key -outform PEM -out launchkey.pem

## Callbacks

It would be helpful to document the URL parameters and POST data associated
with callbacks and the expected response from the web app.
