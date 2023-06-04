"""
Abstract Laptop Manager
This module provides a class for managing laptops and includes
various methods for managing and retrieving laptop information.
"""
# pylint: disable=import-error

from decorators.decorators import method_call_logger, pylint_checker
from models.abstract_laptop import AbstractLaptop
from models.gaming_laptop import GamingLaptop
from models.office_laptop import OfficeLaptop
from models.student_laptop import StudentLaptop
from models.ultrabook import Ultrabook
from managers.set_manager import SetManager


# pylint: disable=too-few-public-methods
@method_call_logger
class AbstractLaptopManager:
    """Class for managing laptops."""

    def __init__(self):
        self.laptops = []

    # pylint: disable=redefined-outer-name
    @pylint_checker
    def add_laptop(self, laptop: AbstractLaptop):
        """Add a laptop to the manager.

        Args:
            laptop (AbstractLaptop): The laptop to add.
        """
        self.laptops.append(laptop)

    @method_call_logger
    def find_all_with_same_ram(self, ram):
        """Find all laptops with the same RAM size.

        Args:
            ram: The RAM size to search for.

        Returns:
            list: List of laptops with the same RAM size.
        """
        return [l for l in self.laptops if l.ram == ram]

    @method_call_logger
    def find_all_with_same_model(self, model):
        """Find all laptops with the same model.

        Args:
            model: The model name to search for.

        Returns:
            list: List of laptops with the same model name.
        """
        return [l for l in self.laptops if l.model == model]

    def __len__(self):
        return len(self.laptops)

    def __getitem__(self, idx):
        return self.laptops[idx]

    def __iter__(self):
        return iter(self.laptops)

    @method_call_logger
    def screen_size(self):
        """Get the screen sizes of all laptops.

        Returns:
            list: List of screen sizes of the laptops.
        """
        return [l.screen_size for l in self.laptops]

    @method_call_logger
    def get_attributes_by_type(self, data_type):
        """Get attributes of laptops by data type.

        Args:
            data_type: The data type to filter attributes by.

        Returns:
            dict: Dictionary of attributes and their corresponding
            values of the specified data type.
        """
        return {
            attr: value
            for l in self.laptops
            for attr, value in l.__dict__.items()
            if isinstance(value, data_type)
        }

    @method_call_logger
    def get_enumerated_laptops(self):
        """Get enumerated list of laptops.

        Returns:
            list: List of tuples containing index and laptop object.
        """
        return list(enumerate(self.laptops))

    @method_call_logger
    def get_zip_with_method_result(self, method_name):
        """Get a zip of laptops with the result of a specified method.

        Args:
            method_name: The name of the method to invoke on each laptop.

        Returns:
            list: List of tuples containing laptop object and the result of the specified method.
        """
        return [(laptop, getattr(laptop, method_name)) for laptop in self.laptops]

    @method_call_logger
    def get_attributes_by_value_type(self, value_type):
        """Get attributes of laptops by value type.

        Args:
            value_type: The value type to filter attributes by.

        Returns:
            dict: Dictionary of attributes and their corresponding
            values of the specified value type.
        """
        return {
            attr: value
            for l in self.laptops
            for attr, value in l.__dict__.items()
            if isinstance(value, value_type)
        }

    @method_call_logger
    def check_all(self, condition):
        """Check if all laptops satisfy a specified condition.

        Args:
            condition: The condition to check for each laptop.

        Returns:
            dict: Dictionary with a single key 'all' and a boolean
            value indicating if all laptops satisfy the condition.
        """
        return {'all': all(condition(l) for l in self.laptops)}

    @method_call_logger
    def check_any(self, condition):
        """Check if any laptop satisfies a specified condition.

        Args:
            condition: The condition to check for each laptop.

        Returns:
            dict: Dictionary with a single key 'any' and a boolean
            value indicating if any laptop satisfies the condition.
        """
        return {'any': any(condition(l) for l in self.laptops)}


if __name__ == '__main__':
    laptop_manager = AbstractLaptopManager()

    gaming_laptop = GamingLaptop("Asus", 17.6, 32, 1024, 10, 100, "NVIDIA RTX 3080", 2)
    ultrabook = Ultrabook("Asus", 15.6, 16, 512, 5, 100, 1.8, 1.7)
    office_laptop = OfficeLaptop("Lenovo", 17.3, 16, 256, 6, 100, "Black", 25000)
    student_laptop = StudentLaptop("Acer", 17.3, 32, 1024, 12, 100, "Intel Core i7", "China")

    laptop_manager.add_laptop(gaming_laptop)
    laptop_manager.add_laptop(ultrabook)
    laptop_manager.add_laptop(office_laptop)
    laptop_manager.add_laptop(student_laptop)

    sm = SetManager(laptop_manager)

    laptops_with_same_ram = laptop_manager.find_all_with_same_ram(16)
    print("Laptops with RAM size of 16GB:")
    for index, laptop in enumerate(laptops_with_same_ram):
        print(f"Laptop {index + 1}: {laptop}")

    laptops_with_same_model = laptop_manager.find_all_with_same_model("Asus")
    print("Laptops with the model name 'Asus':")
    for index, laptop in enumerate(laptops_with_same_model):
        print(f"Laptop {index + 1}: {laptop}")

    print("Total number of laptops:", len(laptop_manager))
    print("Iterating through all laptops:")
    for index, laptop in enumerate(laptop_manager):
        print(f"Laptop {index + 1}: {laptop}")

    screen_sizes = laptop_manager.screen_size()
    print("Screen sizes of laptops:", screen_sizes)

    int_attributes = laptop_manager.get_attributes_by_type(int)
    print("Integer attributes of laptops:")
    for attr, value in int_attributes.items():
        print(f"{attr}: {value}")

    enumerated_laptops = laptop_manager.get_enumerated_laptops()
    print("Enumerated laptops:")
    for index, laptop in enumerated_laptops:
        print(f"Laptop {index + 1}: {laptop}")

    zip_results = laptop_manager.get_zip_with_method_result("screen_size")
    print("Zip results:")
    for laptop, result in zip_results:
        print(f"Laptop: {laptop}, Result: {result}")

    ValueType = int
    attributes_by_value_type = laptop_manager.get_attributes_by_value_type(ValueType)
    print(f"Attributes with value type {ValueType.__name__}:")
    for attr, value in attributes_by_value_type.items():
        print(f"{attr}: {value}")

    all_laptops_check = laptop_manager.check_all(lambda l: l.ram >= 16)
    print("All laptops have RAM size greater than or equal to 16GB:", all_laptops_check['all'])

    any_laptops_check = laptop_manager.check_any(lambda l: l.screen_size < 17)
    print("At least one laptop has screen size less than 17 inches:", any_laptops_check['any'])

    print("Total number of laptops (SM):", len(sm))
    print("Iterating through all laptops (SM):")
    for index, laptop in enumerate(sm):
        print(f"Laptop {index + 1}: {laptop}")
    print("First laptop (SM):", sm[0])
