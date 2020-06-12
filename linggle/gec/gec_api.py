import requests


NMT_API_URL = 'https://whisky.nlplab.cc/translate/?text={}'
SMT_API_URL = "http://ryze.nlplab.cc:9988/correct/{}"
LM_API_URL = "http://ryze.nlplab.cc:9998/correct"


def nmt_correct(text):
    r = requests.get(NMT_API_URL.format(text))
    result = r.json()
    return result.get('result', '')


def lm_correct(sent, threshold=0.97, threshold_insert=0.96):
    r = requests.post(LM_API_URL, json={"sent": sent, "threshold": threshold, "threshold_insert": threshold_insert})
    if r.status_code == 200:
        result = r.json()
        return result.get('result')[1]
    return ''


def smt_correct(text):
    r = requests.get(SMT_API_URL.format(text))
    result = r.json()
    return result.get('result', '')
