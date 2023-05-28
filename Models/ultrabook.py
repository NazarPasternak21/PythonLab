"""
This module defines an Ultrabook class that represents
a laptop specifically designed for ultrabook, inheriting from the Laptop class.
"""

# pylint: disable= import-error
from Models.abstract_laptop import AbstractLaptop


# pylint: disable= too-few-public-methods

class Ultrabook(AbstractLaptop):
    """
    Represents an ultrabook, inheriting from the AbstractLaptop class.
    """
    # pylint: disable= too-many-arguments
    def __init__(self, model="Asus", screen_size=15.6, ram=16,
                 storage=512, battery_life=5, battery_level=100,
                 weight=1.8, thickness=1.7):
        """
        Initializes the Ultrabook object.

        Args:
            model (str): The model of the ultrabook. Defaults to "Asus".
            screen_size (float): The screen size in inches. Defaults to 15.6.
            ram (int): The RAM size in gigabytes. Defaults to 16.
            storage (int): The storage capacity in gigabytes. Defaults to 512.
            battery_life (int): The battery life in hours. Defaults to 5.
            battery_level (int): The current battery level in percentage. Defaults to 100.
            weight (float): The weight of the ultrabook in kilograms. Defaults to 1.8.
            thickness (float): The thickness of the ultrabook in centimeters. Defaults to 1.7.
        """
        super().__init__(model, screen_size, ram, storage, battery_life, battery_level)
        self.weight = weight
        self.thickness = thickness
        self.optimal_processor_temperature = {45, 60}

    def replace_battery(self, capacity_in_hours):
        """
        Raises NotImplementedError as battery replacement is not possible for Ultrabook.
        """
        raise NotImplementedError("Battery replacement is not possible for Ultrabook.")

    def __str__(self):
        """
        Returns a string representation of the ultrabook.

        Returns:
            str: The string representation of the ultrabook.
        """
        return f'Model: {self.model}, Screen size: {self.screen_size},' \
               f' Ram: {self.ram}, Storage: {self.storage}, ' \
               f'Battery life: {self.battery_life}, Battery level: {self.battery_level},' \
               f' Weight: {self.weight}, ' \
               f'Thickness: {self.thickness}'
