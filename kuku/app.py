# coding=utf-8

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(__file__, os.path.pardir, os.path.pardir)))

import tornado.ioloop
import tornado.web

from kuku.handlers import dir, api
from kuku import settings


re_safe_name_with_slash = ur'[ \w\u2e80-\u9fff\-_\.,%/]'


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


route = [
    #(r'/_admin/login', MainHandler),  # TODO
    #(r'/_admin/logout', MainHandler),  # TODO
    (r'/_api/upload', MainHandler),  # TODO
    (r'/_api/mkdir', api.MkdirHandler),
    (r'/_api/delete', api.DeleteHandler),
    (r'/()', dir.DirHandler),
    (r'/(%s+)/' % re_safe_name_with_slash, dir.DirHandler),
    (r'/(%s+)' % re_safe_name_with_slash, tornado.web.StaticFileHandler, {'path': settings.UPLOAD_PATH}),
]

application = tornado.web.Application(route, template_path=settings.TEMPLATE_PATH, debug=settings.DEBUG)


if __name__ == "__main__":
    print """Kuku Start Work!
 _   __      _   __
| | / /     | | / /
| |/ / _   _| |/ / _   _
|    \| | | |    \| | | |
| |\  \ |_| | |\  \ |_| |
\_| \_/\__,_\_| \_/\__,_|
    """
    application.listen(settings.PORT, settings.ADDRESS)
    tornado.ioloop.IOLoop.instance().start()