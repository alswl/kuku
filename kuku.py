# coding=utf-8

import web

import config
import views

urls = (
    r'^/admin/$', 'views.admin.Index',
    r'^/(\S+)/$', 'views.item.Index',
    r'^/(\S+)$', 'views.item.Detail',
    r'^/$', 'views.item.Index',
)
app = web.application(urls, globals())

if __name__ == "__main__":
    web.config.debug = config.DEBUG
    app.run()
