import string, time, math, random
import uuid

def unique_id(prefix, more_entropy=False):
    uniqid = prefix + '-' + uuid.uuid4().hex
    return uniqid



# Test ID number collisions
if __name__ == "__main__":
    ids = set()
    for i in range(int(10000000)):
        gid = unique_id('id')
        if gid in ids:
            raise Exception("Collision after {} iterations".format(i))
        ids.add(gid)
