# coding=utf-8

import os

import tornado.ioloop
import tornado.web

import settings


def is_in_upload(path):
    abs_path = os.path.abspath(os.path.join(settings.UPLOAD_PATH, path))
    return settings.UPLOAD_PATH in abs_path


def is_security_path(path):
    return is_in_upload(path)


class DirHandler(tornado.web.RequestHandler):

    def get(self, path):
        if not is_security_path(path):
            raise tornado.web.HTTPError(404)

        abs_path = os.path.abspath(os.path.join(settings.UPLOAD_PATH, path))
        dirs = []
        files = []
        l = os.listdir(abs_path)
        for f in l:
            if os.path.isdir(os.path.join(abs_path, f)):
                dirs.append(f)
            else:
                files.append(f)
        parent_dir = os.path.dirname(path)
        if not is_security_path(parent_dir):
            parent_dir = None

        self.render('dir.html', dirs=dirs, files=files, parent_dir=parent_dir)

