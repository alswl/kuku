# coding=utf-8

import os

import web
from web import webapi

import config
import lib
import views
from views import Base, render, JsonResult
from views import check_path, require_post_params
from kuku import session

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
    @require_post_params(['path', 'name'])
    def POST(self):
        input = web.input()
        relative_path = input.path
        name = input.name
        if not lib.secure_check_path(relative_path):
            return web.BadRequest()

        path = os.path.join(config.UPLOAD_DIR, relative_path, name)
        if os.path.isfile(path):
            return web.BadRequest()
        if os.path.isdir(path):
            return web.BadRequest()
        os.mkdir(path)
        return JsonResult.json(True)

class Login(Base):
    def GET(self):
        # TODO post login messages
        if views.is_login():
            return web.seeother('/')
        return render.admin_login()

    @require_post_params(['username', 'password'])
    def POST(self):
        input = web.input()
        if input.username == config.ADMIN and input.password == config.PASSWORD:
            views.login()
        return web.seeother('/')

class Logout(Base):
    def GET(self):
        input = web.input(next=None)
        next = input.next
        views.logout()

        if next:
            return web.seeother(next)
        return web.seeother('/')
