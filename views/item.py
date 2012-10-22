# coding=utf-8

import os

from lib import get_file_path, get_dir_path, split_url
from views import render

class Detail:        
    def GET(self, path):
        path = get_file_path(*split_url(path))
        item = open(path, 'r')
        content = item.read() # TODO 直接返回优化
        item.close()
        return content

class Index:        
    def GET(self, path=''):
        path = get_dir_path(*split_url(path))
        return render.item_index()

