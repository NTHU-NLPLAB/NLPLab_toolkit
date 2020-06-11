import requests
from urllib.parse import quote, urljoin

API_URL = "https://f.linggle.com/api/"
__write_api_url = urljoin(API_URL, 'write_call')
__aes_api_url = urljoin(API_URL, 'aes')
__check_api_url = urljoin(API_URL, 'aes_dect')
__suggest_api_url = urljoin(API_URL, 'suggest/')


def suggest_pattern(text):
    r = requests.post(__write_api_url, json={'text': text})
    return r.json()


def assess_essay(text):
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
