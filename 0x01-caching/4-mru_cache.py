#!/usr/bin/env python3
"""Most-Recently-Used caching system
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRU caching
    """
    def __init__(self):
        """Initializing
        """
        super().__init__()

    def put(self, key, item):
        """assigns dictionary item to key
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            most_recently_used_item \
                    = next(reversed(list(self.cache_data.keys())))
            del self.cache_data[most_recently_used_item]
            print("DISCARD:", most_recently_used_item)

        self.cache_data[key] = item

    def get(self, key):
        """Retrieve item from cache as most recently used
        """
        if key is None or key not in self.cache_data:
            return None

        value = self.cache_data.pop(key)
        self.cache_data[key] = value
        return value
