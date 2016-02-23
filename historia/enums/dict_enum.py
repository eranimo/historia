from enum import Enum

class DictEnum(Enum):
    def __init__(self, values):
        for key, value in values.items():
            setattr(self, key, value)
