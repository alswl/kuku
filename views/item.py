# coding=utf-8

import os

import web
from web import webapi

import config
from lib import get_file_path, get_dir_path, split_url
from models import Page
from views import render

class Detail:        
    def GET(self, path):
        try:
            path = get_file_path(*split_url(path))
        except ValueError:
            NotFound()
        item = open(path, 'r')
        content = item.read() # TODO 直接返回优化
        item.close()
        return content

class Index:        
    def GET(self, path=''):
        path = os.path.join(config.UPLOAD_DIR, path)
        if os.path.isdir(path):
            webapi.NotFound()
        page = Page.get_dirs_files(path)

        return render.item_index(page=page)

class Upload:
    def POST(self):
        allowed_extension = [".*"]
        size_limit = 3 * 1024 * 1024 # 3 * 1024 * 1024 bytes
        name = web.input(qqfile=None).qqfile
        path = web.input().path
        data = webapi.data()

        # FIXME 站点攻击，路径问题
        file = open(os.path.join(config.UPLOAD_DIR, path, name), "wb+")
        file.write(data)
        file.close()

        return '{success:true}'
