#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None,
                        page_size: int = 10) -> Dict[str, Any]:
        """Get a page from the indexed dataset, resilient to deletions.

        Parameters:
        index (int): The starting index of the page.
        page_size (int): The number of items per page.

        Returns:
        dict: A dictionary containing pagination details and the dataset page.
        """
        # Ensure index is a valid integer within the valid range
        indexed_dataset = self.indexed_dataset()
        assert isinstance(index, int) and 0 <= index < len(indexed_dataset)

        data = []
        current_index = index
        next_index = index

        # Collect the data for the page size, skipping deleted rows
        while len(data) < page_size and next_index < len(indexed_dataset):
            if next_index in indexed_dataset:
                data.append(indexed_dataset[next_index])
            next_index += 1

        # Return the hypermedia pagination details
        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data
        }
