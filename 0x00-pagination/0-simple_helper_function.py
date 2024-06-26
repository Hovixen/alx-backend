#!/usr/bin/env python3
""" simple helper function """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """ function that takes two integer argument
    returns a Tuple
    """
    start_idx = (page - 1) * page_size
    end_idx = page * page_size
    return (start_idx, end_idx)
