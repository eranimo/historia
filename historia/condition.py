# def Scope(obj):
#     class Getter(object):
#
#         def __init__(self, key):
#             self.key = key
#             self.value = getattr(obj, key)
#
#         def __lt__(self, other):
#             return self.value < other
#         def __gt__(self, other):
#             return self.value > other
#         def __le__(self, other):
#             return self.value <= other
#         def __ge__(self, other):
#             return self.value >= other
#         def __eq__(self, other):
#             return self.value == other
#         def __ne__(self, other):
#             return self.value != other
#         def __nonzero__(self):
#             return self.value is True
#
#     return Getter

def Any(*args):
    return any(list(args))

def All(*args):
    return all(list(args))
