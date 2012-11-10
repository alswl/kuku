# coding=utf-8

import web

import config
import views

re_safe_name = ur'[ \w\u2e80-\u9fff\-_\.,\[\]]'
re_safe_name2 = ur'[ \w\u2e80-\u9fff\-_\.,\[\]/]'

urls = (
    r'/_admin/login', 'views.admin.Login',
    r'/_admin/logout', 'views.admin.Logout',
    r'/_admin/upload', 'views.admin.Upload',
    r'/_admin/mkdir', 'views.admin.Mkdir',
    r'/((?:%(name)s+/)*)' %{'name': re_safe_name}, 'views.item.Index',
    r'/(%(name)s+[^/])' %{'name': re_safe_name2}, 'views.item.Detail',
)
app = web.application(urls, globals())

if web.config.get('_session') is None:
    session = web.session.Session(app, web.session.DiskStore('sessions'), {})
    web.config._session = session
else:
    session = web.config._session

if __name__ == "__main__":
    web.config.debug = config.DEBUG
    app.run()
