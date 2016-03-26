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

    def ref(self):
        return {
            'type': 'enum',
            'id': self.__class__.__name__,
            'key': self.name
        }

    @classmethod
    def all(cls):
        return [cls[x] for x in list(cls.__members__)]

    @classmethod
    def ref_map(cls):
        def convert(data):
            if type(data) is dict:
                for key, value in data.items():
                    if type(value.__class__) is type(cls):
                        data[key] = value.ref()
                    else:
                        data[key] = convert(value)
            elif type(data) is list:
                for key, value in enumerate(data):
                    if type(value.__class__) is type(cls):
                        data[key] = value.ref()
                    else:
                        data[key] = convert(value)
            elif type(data) is tuple:
                data = list(data)
                for key, value in enumerate(data):
                    if type(value.__class__) is type(cls):
                        data[key] = value.ref()
                    else:
                        data[key] = convert(value)
                data = tuple(data)
            return data
        return {x: convert(cls[x].value) for x in list(cls.__members__)}
