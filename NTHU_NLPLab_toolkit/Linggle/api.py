# -*- coding: utf-8 -*-
from collections import namedtuple
import requests
import urllib
import re

from .config import *

class LinggleAPI(dict):
    # ver: Version can be `www`, `coca`, `cna`, `udn`, `zh`
    def __init__(self, ver='www'):
        self.ngram_api = NGRAM_API_URI.format(ver)
        self.example_api = EXP_API_URI.format(ver)

    def __getitem__(self, query):
        return self.query(query)

    def query(self, query):
        """This function query Linggle by query argument

        Parameters
        ----------
        query : str
            The query to query Linggle

        Returns
        -------
        NgramResult : tuple
            query, ngrams, total



        Example
        -------
        >>> api = LinggleAPI()
        >>> api.query('discuss ?about the issue')
        NgramResult(query='discuss ?about the issue', ngrams=[['discuss the issue', 147489], ['discuss about the issue', 98]], total=147587)

        """
        query = query.replace('/', '@')
        query = urllib.parse.quote(query, safe='')
        req = requests.get(self.ngram_api + query)
        if req.status_code == 200:
            return NgramResult(**req.json())

    def get_example(self, ngram_str):
        req = requests.post(self.example_api, json={'ngram': ngram_str})
        if req.status_code == 200:
            result = req.json()
            return result.get("examples", [])

if __name__ == "__main__":
    import doctest
    doctest.testmod()