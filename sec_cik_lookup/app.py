import requests
import json

class SecEdgar:
    def __init__(self, fileurl):
        self.fileurl = fileurl
        self.namedict = {}
        self.tickerdict = {}

        headers = {'user-agent': 'MLT JQ jayquin89@gmail.com'}
        r = requests.get(self.fileurl, headers=headers)

        self.filejson = r.json()
        # print(r.text)
        print(self.filejson)

        self.cik_json_to_dict()

    def cik_json_to_dict(self) -> None:
        self.namedict = {} 
        self.tickerdict = {}
        for entry in self.filejson.values():
            # each entry is a dict with keys 'cik_str', 'ticker', 'title'
            cik = entry['cik_str']
            ticker = entry['ticker']
            name = entry['title'].lower() # make all lowercase
            self.namedict[name] = (cik, name, ticker)
            self.tickerdict[ticker] = (cik, name, ticker)

    # return tuple of (cik, name, ticker)
    def name_to_cik(self, name):
        return self.namedict.get(name)

    # return tuple of (cik, name, ticker)
    def ticker_to_cik(self, ticker):
        return self.tickerdict.get(ticker)

se = SecEdgar('https://www.sec.gov/files/company_tickers.json')