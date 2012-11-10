# coding=utf-8

import os
import json
import mimetypes

import web
from web.contrib.template import render_mako

import config
import lib

mimetypes.init()

class Base(object):
    def __init__(self):
        web.header('Content-Type', 'text/html')

class MyRenderMako(render_mako):
    def __getattr__(self, name):
        path = name + ".html"
        if not os.path.isfile(path):
            path = name.replace('_', '/') + ".html"
        t = self._lookup.get_template(path)
        return t.render

render = MyRenderMako(
    directories=[config.TEMPLATES_DIR],
    input_encoding='utf-8',
    output_encoding='utf-8',
) # TODO +web.contrib.template.cache

class JsonResult(object):

    @classmethod
    def json(cls, success, data=None, message=None):
        result = { 'success': success, }
        if not data is None:
            result['data'] = data
        if not message is None:
            result['message'] = data
        return json.dumps(result)

    @classmethod
    def json_true(cls, data=None, message=None):
        return cls.json(True, data, message)

    @classmethod
    def json_false(cls, data=None, message=None):
        return cls.json(False, data, message)

    @classmethod
    def json_illegal(cls, data=None, message=None):
        return cls.json(False, message='illegal parameters')

def check_path(key_indexs=[], key_words={}):
    """decorator: check path"""
    def wrapper(func):
        def __wrapper(*args, **kwargs):
            need_checks = []
            for i in key_indexs:
                need_checks.append(args[i])
            for path in need_checks:
                if not lib.secure_check_path(path):
                    return web.NotFound()
            return func(*args, **kwargs)
        return __wrapper
    return wrapper
