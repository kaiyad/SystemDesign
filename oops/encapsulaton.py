"""Encapsulation Example"""

class Person():

    def __init__(self, name):
        self.__name = name

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, val):
        if not isinstance(val, str):
            raise Exception("Name should be string")
        self.__name = val

if __name__ == '__main__':
    me = Person("John Snow")
    assert me.Name == "John Snow"
    me.Name = "White Walker"
    assert me.Name == "White Walker"
    try:
        me.Name = 43
        assert False, "Expected Exception"
    except Exception as e:
        assert str(e) == "Name should be string"
