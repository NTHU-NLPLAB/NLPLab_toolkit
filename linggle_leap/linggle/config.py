from collections import namedtuple

NGRAM_API_URI = "https://{0}.linggle.com/query/"
EXP_API_URI = "https://{0}.linggle.com/example/"
API_LIST = [
    'www',
    'coca',
    'cna',
    'udn',
    'zh',
    'x',
    'bi',
    'writeahead',
    'smartwrite',
    'cooleng',
    'lingglewrite',
    'levelup',
    'tellmewhy',
    'booster',
    'langnet',
    'textnet'
]

NgramResult = namedtuple("NgramResult", ["query", "ngrams", "total"])
