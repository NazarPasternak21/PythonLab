"""
This module defines a StudentLaptop class that represents
a laptop specifically designed for students, inheriting from the Laptop class.
"""

# pylint: disable= import-error
from models.abstract_laptop import AbstractLaptop


# pylint: disable= too-few-public-methods

class StudentLaptop(AbstractLaptop):
    """
    Represents a student laptop, inheriting from the AbstractLaptop class.
    """

    # pylint: disable= too-many-arguments
    def __init__(self, model="Acer", screen_size=17.3, ram=32,
                 storage=1024, battery_life=12, battery_level=100,
                 processor="Intel Core i7", producing_country="China"):
        """
        Initializes the StudentLaptop object.

        Args:
            model (str): The model of the student laptop. Defaults to "Acer".
            screen_size (float): The screen size in inches. Defaults to 17.3.
            ram (int): The RAM size in gigabytes. Defaults to 32.
            storage (int): The storage capacity in gigabytes. Defaults to 1024.
            battery_life (int): The battery life in hours. Defaults to 12.
            battery_level (int): The current battery level in percentage. Defaults to 100.
            processor (str): The processor model of the laptop. Defaults to "Intel Core i7".
            producing_country (str): The producing country of the laptop. Defaults to "China".
        """
        super().__init__(model, screen_size, ram, storage, battery_life, battery_level)
        self.processor = processor
        self.producing_country = producing_country
        self.optimal_processor_temperature = {45, 80}

    def __str__(self):
        """
        Returns a string representation of the student laptop.

        Returns:
            str: The string representation of the student laptop.
        """
        return f'Model: {self.model}, Screen size: {self.screen_size},' \
               f' Ram: {self.ram}, Storage: {self.storage}, ' \
               f'Battery life: {self.battery_life}, Battery level: {self.battery_level},' \
               f' Processor: {self.processor}, ' \
               f'Producing_Country: {self.producing_country}'
