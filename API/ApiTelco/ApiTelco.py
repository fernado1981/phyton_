import requests

from API.ApiTelco.DataApi import DataApi


class ApiTelco(DataApi):
    response = ''

    def __init__(self):
        self.data = DataApi.dataApi
        self.url = DataApi.dataApi['url']
        self.search = DataApi.dataApi['searchWord']

    def apiGet(self):
        self.response = requests.get(self.url)
        if self.response.status_code == 200:
            self.response = self.response.json()

    def searchData(self):
        for c, v in self.response.items():
            if c == self.search:
                self.data[True] = {c: v}

    def seeData(self):
        print(self.data)
