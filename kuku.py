# coding=utf-8

import web

import config
import views

re_safe_name = r'[ \w\-\.\u2e80-\u9fff]' # FIXME 中文有问题

urls = (
    r'/_admin/login', 'views.admin.Login',
    r'/_upload', 'views.item.Upload',
    r'/((?:%(name)s+/)*)' %{'name': re_safe_name}, 'views.item.Index',
    r'/((?:%(name)s+/)*)(%(name)s+)' %{'name': re_safe_name}, 'views.item.Detail',
)
app = web.application(urls, globals())

if __name__ == "__main__":
    web.config.debug = config.DEBUG
    app.run()
