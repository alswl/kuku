# coding=utf-8

import os

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
