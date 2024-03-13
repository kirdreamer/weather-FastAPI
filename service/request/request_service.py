import urllib3
from ..url_manager import UrlManagerMixin


class RequestManager(UrlManagerMixin):
    def __init__(self):
        self.http = urllib3.PoolManager()
        
    def performGetRequest(self, url: str):
        return self.http.request("GET", url)
