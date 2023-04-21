"""Singleton Pattrn"""

from abc import ABCMeta, abstractstaticmethod

class IConfReader(metaclass=ABCMeta):

    @abstractstaticmethod
    def get_instance_count():
        raise NotImplementedError

class ConfReaderSingleton(IConfReader):

    __instance = None
    count = 0

    @staticmethod
    def check_instance():
       if ConfReaderSingleton.__instance is not None:
           raise Exception("An instance already exists")
    
    def __init__(self):
        ConfReaderSingleton.check_instance()
        ConfReaderSingleton.__instance = self
        ConfReaderSingleton.count +=  1

    @classmethod
    def get_instance_count(cls):
        return cls.count


if __name__ == '__main__':
    conf_instance = ConfReaderSingleton()
    try:
        conf_instance2 = ConfReaderSingleton()
        assert False, "Expected an Exception"
    except Exception as e:
        assert str(e) == "An instance already exists"
    assert ConfReaderSingleton.get_instance_count() <= 1
