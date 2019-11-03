from pyramid.response import Response
from pyramid.view import view_config
from sqlalchemy.exc import DBAPIError
from ..models import Session
from quote_library.modules.quote_api import Quote
from datetime import datetime


@view_config(route_name='home', renderer='../templates/home.jinja2')
def home(request):
    save_session(request)
    return {'welcome_message': 'Bem vindo, Desafio Web 1.0'}


@view_config(route_name='quotes', renderer='../templates/quotes.jinja2')
def quote(request):
    save_session(request)
    return {'quotes': Quote.get_quotes()}


def save_session(request):
    try:
        session = Session(date_accessed=datetime.utcfromtimestamp(request.session.accessed),
                          page_accessed=request.application_url)
        request.dbsession.add(session)
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)


db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_guruchallenge_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""

