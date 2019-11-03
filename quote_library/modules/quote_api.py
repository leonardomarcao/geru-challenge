from quote_library.config.settings import (
    API_URL
)
import requests
import json


class _QuoteAPI(object):

    @classmethod
    def api_url(cls):
        return API_URL


class Quote(_QuoteAPI):

    @staticmethod
    def get_quotes(**kwargs):
        try:
            req = requests.get(_QuoteAPI.api_url())
            if req.status_code == 200:
                if not kwargs:
                    return [quote for quote in json.loads(req.text)['quotes']]
                else:
                    try:
                        quote_number = int(kwargs['quote_number'])
                        try:
                            return str(json.loads(req.text)['quotes'][quote_number])
                        except IndexError as e:
                            print('Ops! A quote which one are you trying to get does not exist.')
                    except KeyError as e:
                        print('Ops! You maybe pass argument called quote_number.')
        except requests.exceptions.RequestException as e:
            print(e)