# coding=utf-8

import os
import mimetypes

import web
from web import webapi

import config
import lib
from models import Page
from views import Base, render

mimetypes.init()

class Detail(Base):
    def GET(self, dir, name):
        try:
            path = lib.get_file_path(dir, name)
            web.header('Content-Type', mimetypes.guess_type(path)[0])
        except ValueError:
            return webapi.NotFound()
        item = open(path, 'r')
        content = item.read() # TODO 直接返回优化，应该使用 nginx
        item.close()
        return content

class Index(Base):
    def GET(self, path):
        path = os.path.join(config.UPLOAD_DIR, path)
        if not os.path.isdir(path):
            return webapi.NotFound()
        page = Page(path)

        return render.item_index(page=page)
