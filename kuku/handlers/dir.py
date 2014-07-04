# coding=utf-8

import os

import tornado.ioloop
import tornado.web

import settings


class DirHandler(tornado.web.RequestHandler):

    def get(self, path):
        abs_path = os.path.abspath(os.path.join(settings.UPLOAD_PATH, path))
        if settings.UPLOAD_PATH not in abs_path:
            raise tornado.web.HTTPError(404)

        dirs = []
        files = []
        l = os.listdir(abs_path)
        for f in l:
            if os.path.isdir(os.path.join(abs_path, f)):
                dirs.append(f)
            else:
                files.append(f)

        self.write(','.join(dirs) + '; ' + ','.join(files))

