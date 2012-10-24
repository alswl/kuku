# coding=utf-8

import os
try:
    import simplejson as json
except ImportError:
    import json

from web.contrib.template import render_mako

import config

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
)

class JsonResult(object):
    def __init__(self, success, data, message):
        self.success = success
        self.data = data
        self.message = message

    def to_json(self):
        return json.dumps({
            'success': self.success,
            'data': self.data,
            'message': self.message,
        })

    @staticmethod
    def json(success, data=None, message=None):
        return JsonResult(success, data, message).to_json()
