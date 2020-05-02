# -*- coding: utf-8 -*-
import requests
import urllib
from abc import abstractmethod
from .config import NGRAM_API_URI, EXP_API_URI, API_LIST


class APIFactory:
    """This is `Linggle <https://linggle.com/>`_ api factory class.
    you can use ver parameter to select different API version.

    ver: Version can be `www`, `coca`, `cna`, `udn`, `zh, `x`, `bi`
    
    Parameters
    ----------
    ver : {'www', 'coca', 'cna', 'udn', 'zh', 'x', 'bi'}
        version of different linggle API
            * www - Google 1T
            * coca - Corpus of Contemporary American English
            * cna - 中央社
            * udn - 聯合新聞網
            * zh
            * x - 雙語Linggle
            * bi - PhraseBookAPI
    """

    @staticmethod
    def get_api(name="www"):
        """This function geterate Linggle api by query argument

        Parameters
        ----------
        name : str{'www', 'coca', 'cna', 'udn', 'zh', 'x', 'bi'}
            The query string to query Linggle
            you can check `Linggle <https://linggle.com/>`_ for more details.
     
        Returns
        -------
        NgramResult : dict
            query, ngrams, total



        Example
        -------
        >>> from linggle_leap.linggle.api import APIFactory
        >>> api = APIFactory.get_api('www')

        """
        if name not in API_LIST:
            return None
        if name in ["www", "coca", "cna", "udn", "zh", "x"]:
            return LinggleAPI(name)
        if name == "bi":
            return PhraseBookAPI()


class API:
    @abstractmethod
    def query(self, query):
        return NotImplemented

    @abstractmethod
    def get_example(self, ngram_str):
        return NotImplemented


class PhraseBookAPI(API):
    def __init__(self):
        self.API_URI = "https://bi.linggle.com/phrase/"
        self.EXAMPLE_URI = "https://bi.linggle.com/sentence"

    def query(self, query, offset=0):
        self.data = {"offset": offset}
        query = urllib.parse.quote(query, safe="")
        req = requests.get(self.API_URI + query)
        if req.status_code == 200:
            return req.json()

    def get_example(self, phrase_array):
        req = requests.get(
            self.EXAMPLE_URI, params={"ch": phrase_array[0], "en": phrase_array[1]}
        )
        if req.status_code == 200:
            return req.json()


# ver: Version can be `www`, `coca`, `cna`, `udn`, `zh, `x`
class LinggleAPI(API):
    """This is `Linggle <https://linggle.com/>`_ api class.
    you can use ver parameter to select different API version.

    ver: Version can be `www`, `coca`, `cna`, `udn`, `zh, `x`
    
    Parameters
    ----------
    ver : {'www', 'coca', 'cna', 'udn', 'zh', 'x'}
        version of different linggle API
            * www - Google 1T
            * coca - Corpus of Contemporary American English
            * cna - 中央社
            * udn - 聯合新聞網
            * zh
            * x - 雙語Linggle
    """

    def __init__(self, ver="www"):
        self.ver = ver
        self.ngram_api = NGRAM_API_URI.format(ver)
        self.example_api = EXP_API_URI.format(ver)

    # def __getitem__(self, query):
    #     return self.query(query)

    def query(self, query, x_lang="en"):
        """This function query Linggle by query argument

        Parameters
        ----------
        query : str
            The query string to query Linggle
            you can check `Linggle <https://linggle.com/>`_ for more details.
        x_lang : str{'en', 'zh'}
            The query language to use in x.linggle, this parameter will only be applied when version is set as "x".
            Default value is "en".
        Returns
        -------
        NgramResult : dict
            query, ngrams, total



        Example
        -------
        >>> from linggle_leap.linggle.api import APIFactory
        >>> api = APIFactory.get_api('www')
        >>> api.query('discuss ?about the issue')
        {...}

        Example - x.linggle
        -------
        >>> from linggle_leap.linggle.api import APIFactory
        >>> api = APIFactory.get_api('x')
        >>> api.query(u'吃藥', x_lang='zh')
        {...}
        """
        if x_lang == "zh" and self.ver == "x":
            # self.ngram_api = NGRAM_API_URI.replace("query", "equery")
            self.ngram_api = "https://x.linggle.com/equery/"
        query = query.replace("/", "@")
        query = urllib.parse.quote(query, safe="")
        req = requests.get(self.ngram_api + query)
        if req.status_code == 200:
            return req.json()

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
        >>> from linggle_leap.linggle.api import APIFactory
        >>> from pprint import pprint
        >>> api = APIFactory.get_api('www')
        >>> pprint(api.get_example('get a'))
        [...]

        """
        if self.ver == "x":
            req = requests.get("https://x.linggle.com/tgtngram/")
        else:
            req = requests.post(self.example_api, json={"ngram": ngram_str})
        if req.status_code == 200:
            result = req.json()
            return result.get("examples", [])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
