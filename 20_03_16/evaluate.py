from collections import OrderedDict


class LRUCache(object):
    def __init__(self, cache_size=128):
        self.od = OrderedDict()
        self.size = cache_size

    def get(self, key):
        if key in self.od:
            val = self.od.get(key)
            self.od.move_to_end(key)
            return val
        else:
            return -1

    def put(self, key, value):
        if key in self.od:
            del self.od[key]
            self.od[key] = value
        else:
            self.od[key] = value
            if len(self.od) > self.size:
                self.od.popitem(last=True)
