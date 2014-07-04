# coding=utf-8

import tornado.ioloop
import tornado.web

from handlers import dir, file
import settings


re_safe_name_with_slash = ur'[ \w\u2e80-\u9fff\-_\.,/]'


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


application = tornado.web.Application([
    (r'/_admin/', MainHandler),
    (r'/_admin/login', MainHandler),
    (r'/_admin/logout', MainHandler),
    (r'/_admin/upload', MainHandler),
    (r'/_admin/mkdir', MainHandler),
    (r'/_admin/delete', MainHandler),
    (r'/()', dir.DirHandler),
    (r'/(%s+/)' % re_safe_name_with_slash, dir.DirHandler),
    (r'/(%s+)' % re_safe_name_with_slash, tornado.web.StaticFileHandler, {'path': settings.UPLOAD_PATH}),
])


if __name__ == "__main__":
    print """Kuku Start Work!
 _   __      _   __
| | / /     | | / /
| |/ / _   _| |/ / _   _
|    \| | | |    \| | | |
| |\  \ |_| | |\  \ |_| |
\_| \_/\__,_\_| \_/\__,_|
    """
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()