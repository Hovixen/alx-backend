#!/usr/bin/env python3
""" FIFO Caching """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ fifo caching class """
    def __init__(self):
        """ initializing the class """
        super().__init__()
        self.cache_list = []

    def put(self, key, item):
        """ function put item to the cache """
        if key is None or item is None:
            pass

        if key not in self.cache_list:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                print("Discard: {}".format(self.cache_list[0]))
                first_item = self.cache_list.pop(0)
                del self.cache_data[first_item]

        if key not in self.cache_data:
            self.cache_data[key] = item
            self.cache_list.append(key)

    def get(self, key):
        """ function get retrieves item from the cache """
        return self.cache_data.get(key, None)
