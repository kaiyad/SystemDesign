"""DATACLASS"""

from dataclasses import dataclass, field

@dataclass(order=True)
class Person():
    
    sort_index: float = field(init=False, repr=False)
    name: str
    age: int
    income: float = field(repr=True, default=0.0)

    def __post_init__(self):
        self.sort_index = self.income

if __name__ == '__main__':
    person1 = Person("John", 35, 567.89)
    person2 = Person("Snow", 28)
    person3 = Person("John", 35, 567.89)

    assert person1 == person3
    assert str(person1) == str(person3)
    assert person1 > person2
