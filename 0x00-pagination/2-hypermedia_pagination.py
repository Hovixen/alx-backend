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
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        # Calculate the start and end index for the page
        start_index, end_index = index_range(page, page_size)

        # Retrieve the dataset
        dataset = self.dataset()

        # Return the appropriate slice or an empty list if out of range
        if start_index >= len(dataset):
            return []
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get a page from the dataset.

        Parameters:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

        Returns:
        Dictionary: A dictionary of rows corresponding to the page.
        """
        start_idx, end_idx = index_range(page, page_size)
        # Retrieve the dataset and data
        dataset = self.dataset()
        data = self.get_page(page, page_size)

        prev_page = None
        if (page > 1):
            prev_page = page - 1
        next_page = None
        if (end_idx < len(dataset)):
            next_page = page + 1

        total_page = math.ceil(len(dataset) / page_size)
        return {
                "page_size": len(data),
                "page": page,
                "data": data,
                "next_page": next_page,
                "prev_page": prev_page,
                "total_pages": total_page
                }
