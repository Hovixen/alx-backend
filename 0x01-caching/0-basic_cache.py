#!/usr/bin/env python3
""" Basic cache dictionary """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Class inheriting from BaseCaching """

    def __init__(self):
        """ initializing the class """
        super().__init__()

    def put(self, key, item):
        """ the put function adds an item to cache """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ the get function retrives item from cache """
        return self.cache_data.get(key, None)
