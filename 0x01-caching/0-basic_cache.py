#!/usr/bin/env python3
""" class BasicCache that is a caching system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ a caching system.
    """
    def __init__(self):
        """ Initialize
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item to  the cache with a specified key.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Retrieve item by key.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
