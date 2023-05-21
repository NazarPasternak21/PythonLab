from Models.Laptop import Laptop
from Models.GamingLaptop import GamingLaptop
from Models.OfficeLaptop import OfficeLaptop
from Models.StudentLaptop import StudentLaptop
from Models.Ultrabook import Ultrabook


class AbstractLaptopManager:
    def __init__(self):
        self.laptops = []

    def add_laptop(self, l: Laptop):
        self.laptops.append(l)

    def find_all_with_same_ram(self, ram):
        return [l for l in self.laptops if l.ram == ram]

    def find_all_with_same_model(self, model):
        return [l for l in self.laptops if l.model == model]


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

    laptops_with_same_ram = laptop_manager.find_all_with_same_ram(16)
    print("Laptops with RAM size of 16GB:")
    for laptop in laptops_with_same_ram:
        print(laptop)

    laptops_with_same_model = laptop_manager.find_all_with_same_model("Asus")
    print("Laptops with the model name 'Asus':")
    for laptop in laptops_with_same_model:
        print(laptop)
