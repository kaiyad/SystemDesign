"""FACTORY PATTERN"""

import json

from abc import ABC, abstract_method


class ConfReader(ABC):
    def __init__(self, conf):
        self.conf = conf
        self.data = ""
    
    @abstract_method
    def read(self):
        raise NotImplementedError

class TextReader(ConfReader):
    def read(self):
        with open(self.conf, 'r') as _conf:
	    self.data = _conf.read()

class JsonReader(ConfReader):
    def read(self):
        self.data = json.loads(self.conf)

if __name__ == '__main__':
    pass
 
