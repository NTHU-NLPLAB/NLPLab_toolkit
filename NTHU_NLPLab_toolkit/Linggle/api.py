# -*- coding: utf-8 -*-
import requests
import urllib

from .config import NGRAM_API_URI, EXP_API_URI, NgramResult


class LinggleAPI(dict):
    # ver: Version can be `www`, `coca`, `cna`, `udn`, `zh`
    """This is `Linggle <https://linggle.com/>`_ api class.
    you can use ver parameter to select different API version.


    Parameters
    ----------
    ver : {'www', 'coca', 'cna', 'udn', 'zh'}
        version of different linggle API
            * www
            * coca - Corpus of Contemporary American English
            * cna - 中央社
            * udn - 聯合新聞網
            * zh

    """

    def __init__(self, ver="www"):
        self.ngram_api = NGRAM_API_URI.format(ver)
        self.example_api = EXP_API_URI.format(ver)

    def __getitem__(self, query):
        return self.query(query)

    def query(self, query):
        """This function query Linggle by query argument

        Parameters
        ----------
        query : str
            The query string to query Linggle
            you can check `Linggle <https://linggle.com/>`_ for more details.

        Returns
        -------
        NgramResult : tuple
            query, ngrams, total



        Example
        -------
        >>> api = LinggleAPI()
        >>> api.query('discuss ?about the issue')
        NgramResult(query='discuss ?about the issue', \
ngrams=[['discuss the issue', 147489], ['discuss about the issue', 98]], total=147587)

        """
        query = query.replace("/", "@")
        query = urllib.parse.quote(query, safe="")
        req = requests.get(self.ngram_api + query)
        if req.status_code == 200:
            return NgramResult(**req.json())

    def get_example(self, ngram_str):
        """This function query Linggle by query argument

        Parameters
        ----------
        ngram_str : str
            The query string to query Linggle

        Returns
        -------
        results : list of str


        Example
        -------
        >>> from pprint import pprint
        >>> api = LinggleAPI()
        >>> pprint(api.get_example('get a'))
        ['An aid organization helps the family get an apartment in Long Beach , '
         'California , and helps Riku get a job .',
         'Every evening every citizen could get a copy of every piece of paper '
         'generated that day in every government office .',
         'Rookie Bernard Williams figures to start at LT and RT Antone Davis might get '
         'a look at G. Key concern : QB Randall Cunningham ( broken leg ) returns .',
         'A Corvette-style rear suspension greatly improved handling , and you could '
         "even get a @@ 1970 Chevrolet Camaro : Also from GM 's talented Mitchell , "
         "this Camaro 's stunning body admittedly was inspired by Ferrari 's classic "
         "1960s 250GT short-wheelbase model , styled by Italy 's inestimable "
         'Pininfarina .',
         'I get a hundred letters a month -- from law firms , investigators , people '
         'who want to come in and evaluate us -- all trying to get us to buy their '
         'corporate governance services , " said Margaret M. " Peggy " Foran , head of '
         'corporate governance policy at New York-based drug giant Pfizer Inc . "',
         'These days , helicopter tours , snorkeling boat rides and hunting safaris '
         'allow dozens of tourists to get a good view of -- or even set foot on -- '
         "Hawaii 's seventh-largest island nearly every day ."]

        """
        req = requests.post(self.example_api, json={"ngram": ngram_str})
        if req.status_code == 200:
            result = req.json()
            return result.get("examples", [])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
