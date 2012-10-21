# coding=utf-8

import web

import config
import views

urls = (
    r'^/admin/$', 'views.admin.Index',
    r'^/(\S+)/$', 'views.page.Detail',
    r'^/(\S+)$', 'views.item.Detail',
    r'^/$', 'views.page.Detail',
)
app = web.application(urls, globals())

if __name__ == "__main__":
    web.config.debug = config.DEBUG
    app.run()
