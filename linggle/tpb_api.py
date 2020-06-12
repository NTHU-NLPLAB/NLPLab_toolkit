import requests
import urllib


class TotalPhraseBook():
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
