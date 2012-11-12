# coding=utf-8

import os
import logging

import web
from web import webapi

import config
import lib
from models import Page, Item
from views import Base, render, JsonResult
from views import check_path, require_post_params, require_login

logger = logging.getLogger(__name__)

class Detail(Base):
    @check_path(key_indexs=[1])
    def GET(self, path):
        web.header('Content-Type', mimetypes.guess_type(path)[0]) # TODO
        try:
            item = Item(path)
        except lib.NotFoundError:
            return webapi.NotFound()
        logger.info('Need nginx cache file, path: %s' %path)

        return item.get_content()

class Index(Base):
    @require_login
    @check_path(key_indexs=[1])
    def GET(self, path):
        try:
            page = Page.get(path)
        except lib.NotFoundError:
            return webapi.NotFound()

        return render.item_index(page=page)
