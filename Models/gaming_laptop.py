"""
This module defines a GamingLaptop class that represents
a laptop specifically designed for gamers, inheriting from the Laptop class.
"""

# pylint: disable= import-error
from Models.abstract_laptop import AbstractLaptop


# pylint: disable= too-few-public-methods
class GamingLaptop(AbstractLaptop):
    """
    Represents a gaming laptop, inheriting from the AbstractLaptop class.
    """

    # pylint: disable= too-many-arguments
    def __init__(self, model="Asus", screen_size=17.3, ram=32,
                 storage=1024, battery_life=8, battery_level=100,
                 gpu="NVIDIA GeForce RTX 3080", fan_count=2):
        """
        Initializes the GamingLaptop object.

        Args:
            model (str): The model of the laptop. Defaults to "Asus".
            screen_size (float): The screen size in inches. Defaults to 17.3.
            ram (int): The RAM size in gigabytes. Defaults to 32.
            storage (int): The storage capacity in gigabytes. Defaults to 1024.
            battery_life (int): The battery life in hours. Defaults to 8.
            battery_level (int): The current battery level in percentage. Defaults to 100.
            gpu (str): The GPU model of the laptop. Defaults to "NVIDIA GeForce RTX 3080".
            fan_count (int): The number of fans in the laptop. Defaults to 2.
        """
        super().__init__(model, screen_size, ram, storage, battery_life, battery_level)
        self.gpu = gpu
        self.fan_count = fan_count
        self.optimal_processor_temperature = {65, 80}

    def __str__(self):
        """
        Returns a string representation of the gaming laptop.

        Returns:
            str: The string representation of the gaming laptop.
        """
        return f'Model: {self.model}, Screen size: {self.screen_size},' \
               f' Ram: {self.ram}, Storage: {self.storage}, ' \
               f'Battery life: {self.battery_life}, Battery level: {self.battery_level},' \
               f' GPU: {self.gpu}, ' \
               f'Fan count: {self.fan_count}'
