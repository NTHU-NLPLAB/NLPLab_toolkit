from collections import namedtuple

NGRAM_API_URI = "https://{0}.linggle.com/query/"
EXP_API_URI = "https://{0}.linggle.com/example/"


NgramResult = namedtuple("NgramResult", ["query", "ngrams", "total"])
