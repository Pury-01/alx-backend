#!/usr/bin/env python3
"""
pagination with Server class and get_page method
"""
import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Calculate start and end index for pagination."""
    start_index = page_size * (page - 1)
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieve a page of data from the dataset.

        Args:
            page (int): page number (1-indexed)
            page_size (int): Number of items per page

        Returns:
            List[List]: list of rows corresponding to the specified page.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        data = self.dataset()

        if start_index >= len(data):
            return []

        return data[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, any]:
        """Retrieve a dictionary

        Args:
            page (int): Current page number
            page_size (int): number of items per page.

        Returns:
            Dict[str, any]: Dictionary with pagination details
        """
        data = self.get_page(page, page_size)

        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
                "page_size": len(data),  # length of current page
                "page": page,            # current page number
                "data": data,            # dataset page data
                "next_page": next_page,
                "prev_page": prev_page,
                "total_pages": total_pages
        }
