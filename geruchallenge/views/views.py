from pyramid.response import Response
from pyramid.view import view_config
from sqlalchemy.exc import DBAPIError
from ..models import Session
from quote_library.modules.quote_api import Quote
from datetime import datetime
import pyramid.httpexceptions as exc
from cornice import Service
from cornice.resource import resource


@view_config(route_name='home', renderer='../templates/home.jinja2')
def home(request):
    save_session(request)
    return {'welcome_message': 'Bem vindo, Desafio Web 1.0'}


@view_config(route_name='quotes', renderer='../templates/quotes.jinja2')
def quote(request):
    save_session(request)
    return {'quotes': Quote.get_quotes()}


@view_config(route_name='quotes1', renderer='../templates/quote.jinja2')
def quote1(request):
    save_session(request)
    try:
        quote_number = int(request.matchdict['quote_number'])
        return {'quotes': Quote.get_quotes(quote_number=quote_number)}
    except ValueError as e:
        raise exc.exception_response(404)


def save_session(request):
    try:
        session = Session(date_accessed=datetime.utcfromtimestamp(request.session.accessed),
                          page_accessed=request.application_url + request.path_info)
        request.dbsession.add(session)
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)


@resource(collection_path='/endpoint', path='/endpoint/{id}')
class QuoteEndpoint(object):

    def __init__(self, request):
        self.request = request

    def collection_get(self):

        return {
            'sessions': [
                {'id': session.id,
                 'page_accessed': session.page_accessed,
                 'date_accessed': session.date_accessed}

                for session in self.request.dbsession.query(Session)

            ]
        }

    def get(self):
        try:
            return self.request.dbsession.query(Session).get(
                int(self.request.matchdict['id'])).to_json()
        except:
            return {}


db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_geruchallenge_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""
