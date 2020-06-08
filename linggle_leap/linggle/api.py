# -*- coding: utf-8 -*-
from .config import API_LIST


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


if __name__ == "__main__":
    import doctest

    doctest.testmod()
