# coding=utf-8

from web.contrib.template import render_mako

import config

render = render_mako(
    directories=[config.TEMPLATES_DIR],
    input_encoding='utf-8',
    output_encoding='utf-8',
)

