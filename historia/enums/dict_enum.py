from enum import Enum

class DictEnum(Enum):
    "A Enum whose values are dict types, with defaults provided by cls.__defaults__"
    def __init__(self, values):
        items = values.items()
        if hasattr(self, '__defaults__'):
            items = self.__defaults__
            items.update(dict(values.items()))
            items = items.items()
        for key, value in items:
            setattr(self, key, value)
