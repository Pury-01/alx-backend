#!/usr/bin/env python3
"""Least Recently Used caching system
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):

    """LRU caching system
    """
    def __init__(self):
        """Initializing
        """
        super().__init__()

    def put(self, key, item):
        """Assign dictionary key value to item
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            least_key = next(iter(self.cache_data))
            del self.cache_data[least_key]
            print("DISCARD:", least_key)

        self.cache_data[key] = item

    def get(self, key):
        """retrieves item from cache and mark as recently used
        """
        if key is None or key not in self.cache_data:
            return None

        value = self.cache_data.pop(key)
        self.cache_data[key] = value
        return value
