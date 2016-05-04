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

Installation
------------
Install the extension with one of the following commands:

	pip install tornado-route-simple

or download the source code from here and run command:

	python setup.py build
	python setup.py install


Sample usage
-------------
In your app.py

    import tornado.ioloop
    import tornado.web

    from simpleroute import make_routes


    app_settings = dict(
        debug=True,
    )


    apihandlers = make_routes(['handlers'])
    application = tornado.web.Application(apihandlers, **app_settings)
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


In your handlers package
    
    from simpleroute import route
    import tornado.web

    @route(r"^/index/simple$")
    class SimpleHandler(tornado.web.RequestHandler):
        def get(self):
            self.write('Hello!')