# http interface class
import requests

class HttpInterface():
    def __init__(self):
        pass
    
    def get(self, url):
        return requests.get(url)
    
    def post(self, url, data):
        return requests.post(url, data)
    
    def put(self, url, data):
        return requests.put(url, data)
    
    def delete(self, url):
        return requests.delete(url)
    
    def patch(self, url, data):
        return requests.patch(url, data)
    
    def options(self, url):
        return requests.options(url)