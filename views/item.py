# coding=utf-8

import os

import web
from web import webapi

import config
import lib
from models import Page
from views import render

class Detail:        
    def GET(self, dir, name):
        try:
            path = lib.get_file_path(dir, name)
        except ValueError:
            return webapi.NotFound()
        item = open(path, 'r')
        content = item.read() # TODO 直接返回优化
        item.close()
        return content

class Index:        
    def GET(self, path):
        path = os.path.join(config.UPLOAD_DIR, path)
        if not os.path.isdir(path):
            return webapi.NotFound()
        page = Page(path)

        return render.item_index(page=page)

class Upload:
    def POST(self):
        allowed_extension = [".*"]
        size_limit = 3 * 1024 * 1024 # 3 * 1024 * 1024 bytes
        name = web.input(qqfile=None).qqfile
        path = web.input().path
        data = webapi.data()

        if not lib.secure_check_path(path):
            return '{success: false}'
        name = lib.secure_name(name)
        file = open(os.path.join(config.UPLOAD_DIR, path, name), "wb+")
        file.write(data)
        file.close()

        return '{success:true}'
