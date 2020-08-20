import requests
from urllib.parse import quote, urljoin

API_URL = "https://f.linggle.com/api/"
__write_api_url = urljoin(API_URL, 'write_call')
__aes_api_url = urljoin(API_URL, 'aes')
__check_api_url = urljoin(API_URL, 'aes_dect')
__suggest_api_url = urljoin(API_URL, 'suggest/')


def suggest_pattern(text):
    """This is `LinggleWrite <https://f.linggle.com/>`_ api function for writing suggestions.
    You can enter a text and it will provide continuous writing suggestions.

    Example
    -------
    >>> suggest_pattern('Let me tell you a')  # doctest: +ELLIPSIS
    {'text': 'Let me tell you a', 'headword': 'tell', 'pos': 'V', 'patterns': [...]}

    """
    r = requests.post(__write_api_url, json={'text': text})
    return r.json()


def assess_essay(text):
    """This is `LinggleWrite <https://f.linggle.com/>`_ api function for assessing an essay.
    You can enter a text and it will provide a CEFR level.

    Example
    -------
    >>> assess_essay('Let me tell you a story.')
    'A2'

    """
    # TODO: fix the typo in api: courpus -> corpus, cerf -> cefr
    r = requests.post(__aes_api_url, json={'courpus': text})
    return r.json().get('cerf')


def check_essay(text):
    """This is `LinggleWrite <https://f.linggle.com/>`_ api function for checking an essay.
    You can enter a text and it will return sentence scores, tokenized sentences,
    and tags in DIRC format.

    Example
    -------
    >>> check_essay('We can stay in tent.')
    [(['We', 'can', 'stay', 'in', 'tent', '.'], ['O', 'O', 'O', 'O', 'B-I', 'O'], 0.16666666666666666)]

    """
    # TODO: fix the typo in api: courpus -> corpus
    r = requests.post(__check_api_url, json={'courpus': text})
    result = r.json()
    return list(zip(result.get('sen_arry'), result.get('tag_arry'), result.get('score_arry')))


def suggest_edits(ngram, error_type, index):
    """This is `LinggleWrite <https://f.linggle.com/>`_ api function for suggesting edits given a
    problematic ngram and the error type.
    It will return suggestions with a linggle query and query results.

    Example
    -------
    >>> suggest_edits('in tent', 'insert', 1)  # doctest: +ELLIPSIS
    {'query': 'in ?_ tent', 'ngrams': [...]}

    """
    r = requests.get(urljoin(__suggest_api_url, quote(ngram, safe='')), params={'err_type': error_type, 'index': index})
    return r.json()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
