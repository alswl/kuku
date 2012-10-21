# coding=utf-8

from lib import get_dir_path, split_url

class Detail:        
    def GET(self, path=''):
        path = get_dir_path(*split_url(path))
        return path

