import requests
from urllib.parse import quote, urljoin

API_URL = "https://f.linggle.com/api/"
__write_api_url = urljoin(API_URL, 'write_call')
__aes_api_url = urljoin(API_URL, 'aes')
__check_api_url = urljoin(API_URL, 'aes_dect')
__suggest_api_url = urljoin(API_URL, 'suggest/')


def suggest_pattern(text):
    """This is `LinggleWrite <https://f.linggle.com/>`_ api function for writing suggestions.
    you can enter a text and it will provide continuous writing suggestions.

    Parameters
    ----------
    text : str
        An incomplete text to suggestion continuous writing pattern

    Returns
        -------
        results : the headword, PoS, and continuous writing patterns


    Example
    -------
    >>> suggest_pattern('Let me tell you a')  # doctest: +ELLIPSIS
    {'text': 'Let me tell you a', 'headword': 'tell', 'pos': 'V', 'patterns': [...]}

    """
    r = requests.post(__write_api_url, json={'text': text})
    return r.json()


def assess_essay(text):
    """This is `LinggleWrite <https://f.linggle.com/>`_ api function for assessing an essay.
    you can enter a text and it will provide a CEFR level.

    Parameters
    ----------
    text : str
        An essay to be assessed

    Returns
        -------
        results : a CEFR level


    Example
    -------
    >>> assess_essay('Let me tell you a')  # doctest: +ELLIPSIS
    '...'

    """
    # TODO: fix the typo in api: courpus -> corpus, cerf -> cefr
    r = requests.post(__aes_api_url, json={'courpus': text})
    return r.json().get('cerf')


def check_essay(text):
    # TODO: fix the typo in api: courpus -> corpus
    r = requests.post(__check_api_url, json={'courpus': text})
    result = r.json()
    return list(zip(result.get('sen_arry'), result.get('tag_arry'), result.get('score_arry')))


def suggest_edits(ngram, error_type):
    """
    print(suggest_edits('good this', 'insert'))
    """
    r = requests.get(urljoin(__suggest_api_url, quote(ngram, safe='')), params={'err_type': error_type})
    return r.json()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
