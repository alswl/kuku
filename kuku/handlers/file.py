# coding=utf-8

import os

import tornado.ioloop
import tornado.web


class FileHandler(tornado.web.RequestHandler):

    def get(self):
        self.write('file')

