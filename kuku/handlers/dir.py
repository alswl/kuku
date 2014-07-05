# coding=utf-8

import os

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
        dirs = []
        files = []
        file_types = {}
        l = os.listdir(abs_path)
        for f in l:
            if os.path.isdir(os.path.join(abs_path, f)):
                dirs.append(f)
            else:
                files.append(f)

        file_types = dict([(x, magic.from_file(os.path.join(abs_path, x), mime=True)) for x in files])

        parent_dir = os.path.dirname(path)
        if not is_security_path(parent_dir):
            parent_dir = None

        self.render('dir.html', dirs=dirs, files=files, file_types=file_types, parent_dir=parent_dir)
