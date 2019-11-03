from quote_library.config.settings import (
    API_URL
)
import requests
import json


class QuoteAPI(object):

    def __init__(self):
        self.api_url = API_URL

    @property
    def api_url(self):
        return self._api_url

    @api_url.setter
    def api_url(self, api_url: str):
        self._api_url = api_url


class Quote(object):

    def __init__(self):
        self.quote_api = QuoteAPI()
        self.quote = None

    def get_quotes(self, **kwargs):
        if not kwargs:
            list_quotes = []
            req = requests.get(self.quote_api.api_url)
            if req.status_code == 200:
                self.quote = [quote for quote in json.loads(req.text)['quotes']]
        else:
            try:
                quote_number = kwargs['quote_number']
                return json.loads(requests.get(self.quote_api.api_url, params=dict(quote_number)).text)
            except ValueError as e:
                print('You maybe pass argument called quote_number')

    @property
    def quote(self):
        return self._quote

    @quote.setter
    def quote(self, v):
        self._quote = v
