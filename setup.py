from distutils.core import setup
"""
    tornado-route-simple
    -------------

    Tech Notes (or "What the *@# is really happening here?")
    --------------------------------------------------------

    Everytime @route('...') is called, we instantiate a new route object which
    saves off the passed in URI.  Then, since it's a decorator, the function is
    passed to the route.__call__ method as an argument.  We save a reference to
    that handler with our uri in our class level routes list then return that
    class to be instantiated as normal.

    Later, we can call the classmethod route.get_routes to return that list of
    tuples which can be handed directly to the tornado.web.Application
    instantiation.

    Example
    -------

    @route('/some/path')
    class SomeRequestHandler(RequestHandler):
        pass

    my_routes = route.get_routes()"""


setup(
    name='tornado-route-simple',
    version='0.2.0',
    packages=['simpleroute'],
    url='https://github.com/PushAMP/tornado-route-simple',
    license='MIT',
    author='PushAMP Ltd.',
    author_email='devcore@pushamp.com',
    description='Decorates RequestHandlers and builds up a list of routables handlers',
    long_description=__doc__,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
