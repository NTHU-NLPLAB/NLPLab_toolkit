import requests
from urllib.parse import quote_plus, urljoin

API_URI = "https://{0}.linggle.com/"


# ver: Version can be `www`, `coca`, `cna`, `udn`, `zh, `x`
class LinggleAPI(dict):
    """This is `Linggle <https://linggle.com/>`_ api class.
    you can use `ver` parameter to select different API version.

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
        self.api_url = urljoin(API_URI.format(ver), 'query')

    def __getitem__(self, query):
        return self.query(query)

    def query(self, query):
        """This function gets ngrams from Linggle

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
        results : list of (ngram, count)



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
        # TODO: add back xlinggle
        # if x_lang == "zh" and self.ver == "x":
        #     self.ngram_api = "https://x.linggle.com/equery/"
        req = requests.get(urljoin(self.api_url, quote_plus(query)))
        if req.status_code == 200:
            return req.json()['ngrams']
        else:
            # TODO: handle when status code is not 200
            pass

    def get_example(self, ngram):
        """This function gets example of ngram from Linggle

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
        # TODO: add back xlinggle
        # if self.ver == "x":
        #     req = requests.get("https://x.linggle.com/tgtngram/")
        # else:
        req = requests.post(self.example_api, json={"ngram": ngram})
        if req.status_code == 200:
            result = req.json()
            return result.get("examples", [])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
