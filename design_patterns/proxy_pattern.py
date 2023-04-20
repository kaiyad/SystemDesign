"""PROXY PATTERN"""

import json

from abc import ABCMeta, abstractstaticmethod

class IConfReader(metaclass=ABCMeta):

    def __init__(self, input_data):
        self.conf = input_data
        self.data = None
        
    @abstractstaticmethod
    def read():
        raise NotImplementedError


class JsonReader(IConfReader):
   
    def __init__(self, input_data):
        super().__init__(input_data)

    def read(self):
        self.data = json.loads(self.conf)

class ProxyJsonReader(IConfReader):

    def __init__(self, input_data):
        self.reader = JsonReader(input_data)

    def read(self):
        print("proxy reader")
        self.reader.read()

if __name__ == '__main__':
    input_data = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
    proxy_reader = ProxyJsonReader(json.dumps(input_data))
    proxy_reader.read()
    assert proxy_reader.data == input_data
