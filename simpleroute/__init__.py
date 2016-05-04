# coding=utf-8
__author__ = "Dmitry Zhiltsov"
__copyright__ = "Copyright 2016, PushAMP Ltd."
__license__ = "BSD"
__email__ = "devcore@pushamp.com"

import pkgutil
import sys


class Route(object):
    _routes = []

    def __init__(self, uri):
        self._uri = uri

    def __call__(self, _handler):
        self._routes.append((self._uri, _handler))
        return _handler

    @classmethod
    def get_routes(self):
        return self._routes


class RouteLoader(object):
    @staticmethod
    def load(package_name):
        loader = RouteLoader()
        return loader.init_routes(package_name)

    def init_routes(self, package_name):
        package = __import__(package_name)
        controllers_module = sys.modules[package_name]
        prefix = controllers_module.__name__ + "."
        for importer, modname, ispkg in pkgutil.iter_modules(controllers_module.__path__, prefix):
            module = __import__(modname)
        url_routes = route.get_routes()
        return url_routes


def make_routes(dirs):
    result = []
    for dir in dirs:
        item = RouteLoader.load(dir)
        result = result+item
    return result


make_route = lambda dir: RouteLoader.load(dir)

route = Route
