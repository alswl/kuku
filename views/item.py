# coding=utf-8

from lib import get_file_path, split_url

class Detail:        
    def GET(self, path):
        path = get_file_path(*split_url(path))
        item = open(path, 'r')
        content = item.read() # TODO 直接返回优化
        item.close()
        return content
