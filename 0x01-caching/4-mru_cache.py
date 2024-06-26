#!/usr/bin/env python3
""" MRU Caching """
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ mru cache class """
    def __init__(self):
        """ initializing the class """
        super().__init__()
        self.mru_list = []

    def put(self, key, item):
        """ function put adds item to cache """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            print("DISCARD: {}".format(self.mru_list[-1]))
            mru_key = self.mru_list.pop(-1)
            del self.cache_data[mru_key]

        self.cache_data[key] = item
        self.mru_list.append(key)

    def get(self, key):
        """ function get retrieves item from cache """
        if key is None or key not in self.cache_data:
            return None
        self.mru_list.remove(key)
        self.mru_list.append(key)
        return self.cache_data.get(key, None)
