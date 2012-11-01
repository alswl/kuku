# coding=utf-8

import web

import config
import views

re_safe_name = ur'[ \w\u2e80-\u9fff\-_\.,\[\]]'

urls = (
    r'/_admin/login', 'views.admin.Login',
    r'/_admin/upload', 'views.admin.Upload',
    r'/_admin/mkdir', 'views.admin.Mkdir',
    r'/((?:%(name)s+/)*)' %{'name': re_safe_name}, 'views.item.Index',
    r'/((?:%(name)s+/)*)(%(name)s+)' %{'name': re_safe_name}, 'views.item.Detail',
)
app = web.application(urls, globals())

if __name__ == "__main__":
    web.config.debug = config.DEBUG
    app.run()
