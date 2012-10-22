# coding=utf-8

import os

import config

class Page(object):

    def __init__(self, path):
        self.path = path
        #self.relative_path
        self.dirs = []
        self.files = []
        self.breadcrumbs = []
        self.set_breadcrumbs()

    def set_breadcrumbs(self):
        self.relative_path = os.path.relpath(self.path, config.UPLOAD_DIR)
        l = self.relative_path.split('/')
        parent = '/'
        self.breadcrumbs.append(('HOME', parent))
        if l[0] == '.':
            l.pop(0)
        for i in l:
            self.breadcrumbs.append((i, parent + i + '/'))
            parent += i + '/'

    @staticmethod
    def get_dirs_files(path):
        page = Page(path)
        l = os.listdir(page.path)
        for f in l:
            if os.path.isdir(os.path.join(path, f)):
                page.dirs.append(f)
            else:
                page.files.append(f)
        return page
