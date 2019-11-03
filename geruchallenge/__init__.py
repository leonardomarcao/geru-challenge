from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    session_factory = SignedCookieSessionFactory('itsaseekreet')
    config = Configurator(settings=settings)
    config.set_session_factory(session_factory)
    config.include('pyramid_jinja2')
    config.include('.models')
    config.include('.routes')
    config.include("cornice")
    config.scan("geruchallenge.views")
    return config.make_wsgi_app()
