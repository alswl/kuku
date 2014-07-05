# coding=utf-8

import os
from collections import OrderedDict

import tornado.ioloop
import tornado.web
import magic

from kuku import settings
from kuku.handlers import decorators


def is_in_upload(path):
    abs_path = os.path.abspath(os.path.join(settings.UPLOAD_PATH, path))
    return settings.UPLOAD_PATH in abs_path


def is_security_path(path):
    return is_in_upload(path)


class DirHandler(tornado.web.RequestHandler):

    @decorators.require_basic_auth
    def get(self, path):
        if not is_security_path(path):
            raise tornado.web.HTTPError(404)

        abs_path = os.path.abspath(os.path.join(settings.UPLOAD_PATH, path))
        dirs = OrderedDict()
        files = OrderedDict()
        l = os.listdir(abs_path)
        for f in l:
            if os.path.isdir(os.path.join(abs_path, f)):
                dirs[f] = {
                }
            else:
                files[f] = {
                    'mime': magic.from_file(os.path.join(abs_path, f), mime=True),
                }

        parent_dir = os.path.dirname(path)
        if not is_security_path(parent_dir):
            parent_dir = ''

        self.render('dir.html', current_dir=path, dirs=dirs, files=files, parent_dir=parent_dir)
