#!/usr/bin/env python3
"""Least frequently used caching system
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFU caching system
    """
    def __init__(self):
        """Initializing
        """
        super().__init__()
        self.frequency = {}

    def put(self, key, item):
        """assign dictionary item to value
        """
        if key is None or item is None:
            return

        # if the item is new and the cache full
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            least_frequently_used_key \
                    = min(self.frequency, key=self.frequency.get)
            # find the least frequently used key
            del self.cache_data[least_frequently_used_key]
            del self.frequency[least_frequently_used_key]
            print("DISCARD:", least_frequently_used_key)

        # Add or update the key
        self.cache_data[key] = item
        self.frequency[key] = self.frequency.get(key, 0) + 1

    def get(self, key):
        """Retrieve item from cache and update frequency
        """
        if key is None or key not in self.cache_data:
            return None

        # update the frequency
        self.frequency[key] += 1
        return self.cache_data[key]
