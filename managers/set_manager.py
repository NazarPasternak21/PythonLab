"""
This module defines the SetManager class that manages a set of laptops.
"""

# pylint: disable= import-error
from typing import Iterator
from models.abstract_laptop import AbstractLaptop


class SetManager:
    """
    A class that manages a set of laptops, based on a regular manager.

    Args:
        regular_manager (AbstractLaptop): The regular manager containing the laptops.

    Attributes:
        regular_manager (AbstractLaptop): The regular manager containing the laptops.
        laptops_set (set): The set of laptops.
    """

    def __init__(self, regular_manager: AbstractLaptop):
        """
        Initializes the SetManager object.

        Args:
            regular_manager (AbstractLaptop): The regular manager containing the laptops.
        """
        self.regular_manager = regular_manager
        self.laptops_set = set()

        for laptop in self.regular_manager:
            self.laptops_set.add(laptop)

    def __iter__(self) -> Iterator[AbstractLaptop]:
        """
        Returns an iterator for the laptops in the set.

        Returns:
            Iterator[AbstractLaptop]: An iterator for the laptops.
        """
        return iter(self.laptops_set)

    def __len__(self):
        """
        Returns the number of laptops in the set.

        Returns:
            int: The number of laptops in the set.
        """
        return len(self.laptops_set)

    def __getitem__(self, index):
        """
        Returns the laptop at the specified index in the set.

        Args:
            index (int): The index of the laptop.

        Returns:
            AbstractLaptop: The laptop at the specified index.
        """
        return list(self.laptops_set)[index]
