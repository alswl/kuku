# coding=utf-8

import os

import web
from web import webapi

import config
import lib
from views import render, JsonResult

class Index:
    def GET(self):
        return render.foundation()

class Upload:
    def POST(self):
        allowed_extension = [".*"]
        size_limit = 3 * 1024 * 1024 # 3 * 1024 * 1024 bytes
        name = web.input(qqfile=None).qqfile
        path = web.input(path=None).path
        data = webapi.data()
        if name is None or path is None or data is None:
            return JsonResult.json(False, message="Parameter error")
        if not lib.secure_check_path(path):
            return JsonResult.json(False)

        name = lib.secure_name(name)
        file = open(os.path.join(config.UPLOAD_DIR, path, name), "wb+")
        file.write(data)
        file.close()

        return JsonResult.json(True)

class Mkdir:
    def POST(self):
        return JsonResult.json(False, message="need implement") ## change json to decorator
