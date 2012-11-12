# coding=utf-8

import os
import shutil

import config
import lib

class Page(object):

    BASE_PATH = config.UPLOAD_DIR

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

    @classmethod
    def get(cls, relative_path):
        path = os.path.join(cls.BASE_PATH, relative_path)
        if not os.path.isdir(path):
            raise lib.NotFoundError
        return Page(path)

class Item(object):

    BASE_PATH = config.UPLOAD_DIR

    def __init__(self, relative_path):
        self.path = os.path.join(self.BASE_PATH, relative_path)
        if not os.path.isfile(self.path):
            raise lib.NotFoundError
        self.relative_path = relative_path

    @classmethod
    def get(cls, relative_path):
        item = Item(relative_path)
        item.relative_path = relative_path

    def get_content(self):
        if hasattr(self, 'content'):
            return self.content
        f = open(self.path, 'r')
        self.content = f.read()
        f.close()
        return self.content

    @classmethod
    def upload(cls, dir_path, name, data):
        _, extension = os.path.splitext(name)
        if len(extension) <= 1:
            raise lib.IllegalValueError()
        if not extension[1:] in config.ALLOWD_EXTENSIONS:
            raise lib.IllegalValueError()
        if len(data) > config.MAX_FILE_SIZE:
            raise lib.IllegalValueError()

        name = lib.secure_name(name)
        file = open(os.path.join(config.UPLOAD_DIR, dir_path, name), "wb+")
        file.write(data)
        file.close()
    @classmethod

    def delete(cls, dir_path, name):
        path = os.path.join(config.UPLOAD_DIR, dir_path, name)
        if os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)
        else:
            raise lib.IllegalValueError()
