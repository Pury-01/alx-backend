#!/usr/bin/env python3
"""LIFO caching system
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO cache system
    """

    def __init__(self):
        """Initialize
        """
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary the item value for the key
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = next(reversed(list(self.cache_data.keys())))
            del self.cache_data[last_key]
            print("DISCARD:", last_key)

        self.cache_data[key] = item

    def get(self, key):
        """retrieve the value of the specified key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
