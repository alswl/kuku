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

        self.set_dirs_files()
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

    def set_dirs_files(self):
        l = os.listdir(self.path)
        for f in l:
            if os.path.isdir(os.path.join(self.path, f)):
                self.dirs.append(f)
            else:
                self.files.append(f)
        return self
