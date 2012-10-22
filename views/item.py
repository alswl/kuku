# coding=utf-8

import os

import config
from lib import get_file_path, get_dir_path, split_url
from models import Page
from views import render
from web.webapi import NotFound

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
            NotFound()
        page = Page.get_dirs_files(path)

        return render.item_index(page=page)

