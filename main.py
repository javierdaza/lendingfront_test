import os

import tornado.httpserver
import tornado.ioloop
import tornado.web

from controller import MainHandler, MyFormHandler

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "debug": False,
}

urls = [
        (r"/home", MainHandler),
        (r"/", MyFormHandler),
        (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': dict(path=settings['static_path'])}),
    ]


def make_app():
    return tornado.web.Application(urls, **settings)

if __name__ == "__main__":
    app = make_app()
    server = tornado.httpserver.HTTPServer(app)
    port = int(os.environ.get("PORT", 5000))
    server.listen(port)
    tornado.ioloop.IOLoop.instance().start()
