"""FACTORY PATTERN"""

import ast
import json

from abc import ABCMeta, abstractstaticmethod


class IConfReader(metaclass=ABCMeta):
    """Interface for Conf Reader"""

    def __init__(self, input_data):
        self.conf = input_data
        self.data = None

    @abstractstaticmethod
    def read():
        raise NotImplementedError


class TextReader(IConfReader):
    def __init__(self, input_data):
        super().__init__(input_data)

    def read(self):
        self.data = str(self.conf)


class JsonReader(IConfReader):
    def __init__(self, input_data):
        super().__init__(input_data)

    def read(self):
        self.data = json.loads(self.conf)


class ConfFactory:
    """Factory to build objects dynamically"""

    @staticmethod
    def build_reader(input_data, input_type):
        if input_type.upper() == "TEXT":
            return TextReader(input_data)
        elif input_type.upper() == "JSON":
            return JsonReader(input_data)


if __name__ == "__main__":
    input_data = "This is Test Text"
    reader = ConfFactory.build_reader(input_data, "text")
    reader.read()
    assert reader.data == input_data
    input_data = json.dumps({'a': 'b', 'c': 'd', 'e': 'f', 'g': 'h'})
    reader = ConfFactory.build_reader(input_data, "json")
    reader.read()
    assert reader.data == ast.literal_eval(str(input_data))
