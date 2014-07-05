# coding=utf-8

import tornado.ioloop
import tornado.web

from handlers import dir
import settings


re_safe_name_with_slash = ur'[ \w\u2e80-\u9fff\-_\.,/]'


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


route = [
    (r'/_admin/login', MainHandler),  # TODO
    (r'/_admin/logout', MainHandler),  # TODO
    (r'/_api/upload', MainHandler),  # TODO
    (r'/_api/mkdir', MainHandler),  # TODO
    (r'/_api/delete', MainHandler),  # TODO
    (r'/()', dir.DirHandler),
    (r'/(%s+)/' % re_safe_name_with_slash, dir.DirHandler),
    (r'/(%s+)' % re_safe_name_with_slash, tornado.web.StaticFileHandler, {'path': settings.UPLOAD_PATH}),
]

application = tornado.web.Application(route, template_path=settings.TEMPLATE_PATH)


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