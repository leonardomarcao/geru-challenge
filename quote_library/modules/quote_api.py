from quote_library.config.settings import (
    API_URL
)
import requests
import json
import random


class _QuoteAPI(object):

    @classmethod
    def __api_url(cls):
        return API_URL

    @staticmethod
    def request_quote():
        return requests.get(_QuoteAPI.__api_url())


class Quote(object):

    @staticmethod
    def get_quotes(**kwargs):
        try:
            req = _QuoteAPI.request_quote()
            if req.status_code == 200:
                if not kwargs:
                    return [quote for quote in json.loads(req.text)['quotes']]
                elif 'quote_number' in kwargs:
                    quote_number = int(kwargs['quote_number'])
                    try:
                        return json.loads(req.text)['quotes'][quote_number]
                    except IndexError as e:
                        print('Ops! A quote which one are you trying to get does not exist.')
                elif 'random' in kwargs and kwargs['random']:
                    return random.choice(json.loads(req.text)['quotes'])
        except requests.exceptions.RequestException as e:
            print(e)
