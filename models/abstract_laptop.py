"""
This module defines a Laptop class that
represents a laptop with various specifications and functionalities.
"""
from decorators.decorators import logged
from exceptions.exceptions import RedundantChargeException


class AbstractLaptop:
    """
    Represents an abstract laptop.
    """

    # pylint: disable= too-many-arguments
    def __init__(self, model="Unknown", screen_size=15.6, ram=8,
                 storage=256, battery_life=5, battery_level=100):
        """
        Initializes the AbstractLaptop object.

        Args:
            model (str): The model of the laptop. Defaults to "Unknown".
            screen_size (float): The screen size in inches. Defaults to 15.6.
            ram (int): The RAM size in gigabytes. Defaults to 8.
            storage (int): The storage capacity in gigabytes. Defaults to 256.
            battery_life (int): The battery life in hours. Defaults to 5.
            battery_level (int): The current battery level in percentage. Defaults to 100.
        """
        self.model = model
        self.screen_size = screen_size
        self.ram = ram
        self.storage = storage
        self.battery_life = battery_life
        self.battery_level = battery_level
        self.optimal_processor_temperature = set()

    def upgrade_ram(self, value):
        """
        Upgrades the RAM size of the laptop.

        Args:
            value (int): The amount of RAM to be added in gigabytes.
        """
        self.ram += value

    def upgrade_storage(self, value):
        """
        Upgrades the storage capacity of the laptop.

        Args:
            value (int): The amount of storage to be added in gigabytes.
        """
        self.storage += value

    @logged(RedundantChargeException, 'console')
    def charge(self):
        """Charge the laptop's battery."""
        if self.battery_level == 100:
            raise RedundantChargeException("Battery level is already at 100%")
        else:
            print("Charging the battery...")
            self.battery_level = 100
            print("Battery is fully charged.")

    def replace_battery(self, capacity_in_hours):
        """
        Replaces the laptop's battery with a new one.

        Args:
            capacity_in_hours (int): The capacity of the new battery in hours.
        """
        self.battery_life = capacity_in_hours
        self.battery_level = 100

    def __str__(self):
        """
        Returns a string representation of the laptop.

        Returns:
            str: The string representation of the laptop.
        """
        return f"Model: {self.model}, Screen size: {self.screen_size}, Ram: {self.ram}, " \
               f"Storage: {self.storage}, Battery life: {self.battery_life}, " \
               f"Battery level: {self.battery_level}"

    def __iter__(self):
        """
        Returns an iterator for the optimal processor temperatures.

        Returns:
            iterator: Iterator for optimal processor temperatures.
        """
        return iter(self.optimal_processor_temperature)
