import requests
from urllib.parse import quote, urljoin

API_URL = "https://{0}.linggle.com/"


# ver: Version can be `www`, `coca`, `cna`, `udn`, `zh, `x`
class Linggle(dict):
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
        self.__ver = ver
        url = API_URL.format(ver)
        self.__ngram_api_url = urljoin(url, 'ngram/')
        self.__example_api_url = urljoin(url, 'example/')

    @property
    def ver(self):
        return self.__ver

    @ver.setter
    def set_version(self, ver):
        self.__ver = ver
        url = API_URL.format(ver)
        self.__ngram_api_url = urljoin(url, 'ngram/')
        self.__example_api_url = urljoin(url, 'example/')

    @property
    def ngram_api_url(self):
        return self.__ngram_api_url

    @property
    def example_api_url(self):
        return self.__example_api_url

    def __getitem__(self, query):
        return self.query(query)

    def query(self, query):
        """This function gets ngrams from Linggle

        Parameters
        ----------
        query : str
            The query string to query Linggle.
            You can check `Linggle <https://linggle.com/>`_ for more instructions.
        Returns
        -------
        results : list of (ngram, count)



        Example
        -------
        >>> linggle = Linggle()
        >>> linggle.query('discuss ?about the issue')  # doctest: +ELLIPSIS
        [...]

        """
        url = urljoin(self.ngram_api_url, quote(query, safe=''))
        req = requests.get(url)
        if req.status_code == 200:
            return req.json()['ngrams']
        else:
            # TODO: handle when status code is not 200
            pass

    def get_example(self, ngram):
        """This function gets example of ngram from Linggle

        Parameters
        ----------
        ngram : str
            The ngram to query for examples

        Returns
        -------
        results : list of example sentences


        Example
        -------
        >>> linggle = Linggle()
        >>> linggle.get_example('present a method')  # doctest: +ELLIPSIS
        [...]

        """
        url = urljoin(self.example_api_url, quote(ngram, safe=''))
        req = requests.get(url)
        if req.status_code == 200:
            return req.json().get("examples", [])
        else:
            # TODO: handle when status code is not 200
            pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
