#!/usr/bin/env python3
""" Simple Pagination """
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """ function that takes two integer argument
    returns a Tuple
    """
    start_idx = (page - 1) * page_size
    end_idx = page * page_size
    return (start_idx, end_idx)


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
        """Get a page from the dataset.

        Parameters:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

        Returns:
        List[List]: A list of rows corresponding to the page.
        """
        # Ensure page and page_size are positive integers
        assert isinstance(page, int) and page > 0, "page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "page_size must be a positive integer"

        # Calculate the start and end index for the page
        start_index, end_index = index_range(page, page_size)

        # Retrieve the dataset
        dataset = self.dataset()

        # Return the appropriate slice or an empty list if out of range
        if start_index >= len(dataset):
            return []
        return dataset[start_index:end_index]
