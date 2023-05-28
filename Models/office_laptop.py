"""
This module defines a OfficeLaptop class that represents
a laptop specifically designed for office, inheriting from the Laptop class.
"""

# pylint: disable= import-error
from Models.abstract_laptop import AbstractLaptop


# pylint: disable= too-few-public-methods
class OfficeLaptop(AbstractLaptop):
    """
    Represents an office laptop, inheriting from the AbstractLaptop class.
    """
    # pylint: disable= too-many-arguments
    def __init__(self, model="Lenovo", screen_size=17.3,
                 ram=16, storage=256, battery_life=6, battery_level=100,
                 color="Black", price=25000):
        """
        Initializes the OfficeLaptop object.

        Args:
            model (str): The model of the office laptop. Defaults to "Lenovo".
            screen_size (float): The screen size in inches. Defaults to 17.3.
            ram (int): The RAM size in gigabytes. Defaults to 16.
            storage (int): The storage capacity in gigabytes. Defaults to 256.
            battery_life (int): The battery life in hours. Defaults to 6.
            battery_level (int): The current battery level in percentage. Defaults to 100.
            color (str): The color of the laptop. Defaults to "Black".
            price (int): The price of the laptop. Defaults to 25000.
        """
        super().__init__(model, screen_size, ram, storage, battery_life, battery_level)
        self.color = color
        self.price = price
        self.optimal_processor_temperature = {45, 60}

    def __str__(self):
        """
        Returns a string representation of the office laptop.

        Returns:
            str: The string representation of the office laptop.
        """
        return f'Model: {self.model}, Screen size: {self.screen_size},' \
               f' Ram: {self.ram}, Storage: {self.storage}, ' \
               f'Battery life: {self.battery_life}, Battery level: {self.battery_level},' \
               f' Color: {self.color}, ' \
               f'Price: {self.price}'
