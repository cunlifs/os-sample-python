import pprint


def handler(environ, start_fn):
    start_fn('200 OK', [('Content-Type', 'text/plain')])
    return ["Hello World!\n"]


def log_environ(handler):
    def _inner(environ, start_fn):
        pprint.pprint(environ)
        return handler(environ, start_fn)
    return _inner


app = log_environ(handler)
