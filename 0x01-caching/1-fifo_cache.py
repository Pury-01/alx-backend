#!/usr/bin/env python3
"""class FIFOCache that inherits from BaseCaching
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching system
    """

    def __init__(self):
        """Initialize
        """
        super().__init__()  # initialize self.cache_data as a dictionary

    def put(self, key, item):
        """Assign to the dictionary the item value for key
        """
        if key is None or item is None:
            return

        # check if cache exceeds max_items
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            oldest_key = next(iter(self.cache_data))
            del self.cache_data[oldest_key]
            print("DISCARD:", oldest_key)

        # Add the new key_value pair
        self.cache_data[key] = item

    def get(self, key):
        """get the value associated with key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
