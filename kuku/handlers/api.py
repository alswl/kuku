# coding=utf-8

import os
import shutil

import tornado.ioloop
import tornado.web
import magic

from kuku import settings
from kuku.handlers import decorators
from .dir import is_security_path


def do_mkdir(path):
    abs_path = os.path.abspath(os.path.join(settings.UPLOAD_PATH, path))
    if os.path.isfile(abs_path):
        raise ValueError('name is already exist')
    if os.path.isdir(abs_path):
        raise ValueError('name is already exist')
    os.mkdir(abs_path)


def do_delete(path):
    abs_path = os.path.abspath(os.path.join(settings.UPLOAD_PATH, path))
    if not os.path.isfile(abs_path) and not os.path.isdir(abs_path):
        raise ValueError('name is not exist')
    if os.path.isfile(abs_path):
        os.remove(abs_path)
    elif os.path.isdir(abs_path):
        shutil.rmtree(abs_path)


class MkdirHandler(tornado.web.RequestHandler):

    @decorators.require_basic_auth
    def post(self):
        path_str = self.get_argument('path')
        path = path_str[1:]

        if not is_security_path(path):
            self.set_status(403)
            self.write('not allowed name')
            return

        try:
            do_mkdir(path)
        except ValueError, e:
            self.set_status(403)
            self.write(e.message)
            return

        self.finish()


class DeleteHandler(tornado.web.RequestHandler):

    @decorators.require_basic_auth
    def post(self):
        path_str = self.get_argument('path')
        path = path_str[1:]

        if not is_security_path(path):
            self.set_status(403)
            self.write('not allowed name')
            return

        try:
            do_delete(path)
        except ValueError, e:
            self.set_status(403)
            self.write(e.message)
            return

        self.finish()
