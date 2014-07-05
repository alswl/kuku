# coding=utf-8

import base64

from kuku import settings


def require_basic_auth(func):

    def wrap(handler, *args, **kwargs):
        auth_header = handler.request.headers.get('Authorization')
        if auth_header is None or not auth_header.startswith('Basic '):
            handler.set_status(401)
            handler.set_header('WWW-Authenticate', 'Basic realm=Restricted')
            handler._transforms = []
            handler.finish()
            return
        auth_decoded = base64.decodestring(auth_header[6:])
        username, password = auth_decoded.split(':', 2)
        if (username, password) not in settings.ACCOUNTS:
            handler.set_status(403)
            handler.write('403')
            return
        return func(handler, *args, **kwargs)

    return wrap

