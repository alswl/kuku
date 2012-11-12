# coding=utf-8

import os

import web
from web import webapi

import config
import lib
from models import Item
import views
from views import Base, render, JsonResult
from views import check_path, require_post_params, require_login

class Index(Base):
    def GET(self):
        return render.foundation()

class Mkdir(Base):
    @require_login
    @require_post_params('path', 'name')
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

    @require_post_params('username', 'password')
    def POST(self):
        input = web.input()
        if input.username == config.ADMIN and input.password == config.PASSWORD:
            views.login()
        return web.seeother('/')

class Logout(Base):
    @require_login
    def GET(self):
        input = web.input(next=None)
        next = input.next
        views.logout()

        if next:
            return web.seeother(next)
        return web.seeother('/')

class Upload(Base):
    @require_login
    @check_path(post_params=['path'])
    @require_post_params('qqfile', 'path')
    def POST(self):
        name = web.input().qqfile
        path = web.input().path
        data = webapi.data()
        if data is None:
            return web.BadRequest()
        try:
            Item.upload(path, name, data)
        except lib.IllegalValueError:
            return JsonResult.json(False)

        return JsonResult.json(True)

