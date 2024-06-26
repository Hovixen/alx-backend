#!/usr/bin/env python3
""" LIFO Caching """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ lifo caching class """
    def __init__(self):
        """ initializing the class """
        super().__init__()
        self.cache_list = []

    def put(self, key, item):
        """ function add items to cache """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                print("DISCARD: {}".format(self.cache_list[-1]))
                last_item = self.cache_list.pop(-1)
                del self.cache_data[last_item]

        self.cache_data[key] = item
        if key not in self.cache_list:
            self.cache_list.append(key)

    def get(self, key):
        """ function get, retrieves item from cache """
        return self.cache_data.get(key, None)
