#!/usr/bin/env python3
""" Last Recently Used caching """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LRU caching class """
    def __init__(self):
        """ initializing the class """
        super().__init__()
        self.lru_list = []

    def put(self, key, item):
        """ function put adds item to cache """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            print("DISCARD: {}".format(self.lru_list[0]))
            lru_key = self.lru_list.pop(0)
            del self.cache_data[lru_key]

        self.cache_data[key] = item
        self.lru_list.append(key)

    def get(self, key):
        """ function get retrives item from cache """
        if key is None or key not in self.cache_data:
            return None
        self.lru_list.remove(key)
        self.lru_list.append(key)
        return self.cache_data.get(key, None)
