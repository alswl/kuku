# coding=utf-8

import os

import web
from web import webapi

import config
import lib
from views import Base, render, JsonResult

class Index(Base):
    def GET(self):
        return render.foundation()

class Upload(Base):
    def POST(self):
        name = web.input(qqfile=None).qqfile
        path = web.input(path=None).path # TODO 做统一校验
        data = webapi.data()
        if name is None or path is None or data is None:
            return JsonResult.json(False, message='Parameter error')
        if not lib.secure_check_path(path):
            return JsonResult.json(False)
        _, extension = os.path.splitext(name)
        if len(extension) > 1 and \
           not extension[1:] in config.ALLOWD_EXTENSIONS:
            return JsonResult.json(False, message='Not allowed extension')
        if len(data) > config.MAX_FILE_SIZE:
            return JsonResult.json(False, message='File too large')

        name = lib.secure_name(name)
        file = open(os.path.join(config.UPLOAD_DIR, path, name), "wb+")
        file.write(data)
        file.close()
        return JsonResult.json(True)

class Mkdir(Base):
    def POST(self):
        input = web.input(path=None, name=None)
        relative_path = input.path
        name = input.name
        if not relative_path or not name:
            return JsonResult.json_illegal(False) # TODO security

        os.mkdir(os.path.join(config.UPLOAD_DIR, relative_path, name))
        return JsonResult.json(True)
