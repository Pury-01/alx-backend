#!/usr/bin/env python3
"""
function named index_range that calculates the start
and end indexes for a specific page and page size.
"""


from typing import Tuple


def index_range(page, page_size) -> Tuple[int, int]:
    """Calculates start and end index for pagination.

    Args:
        page (int): Current page number (1-indexed).
        page_size (int): Number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start and end indexes.
    """
    start_index = page_size * (page - 1)
    end_index = page_size + start_index
    return start_index, end_index
