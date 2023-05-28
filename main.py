class Laptop:
    def __init__(self, model="Unknown", screen_size=15.6, ram=8, storage=256, battery_life=5, battery_level=100):
        self.model = model
        self.screen_size = screen_size
        self.ram = ram
        self.storage = storage
        self.battery_life = battery_life
        self.battery_level = battery_level

    def upgrade_ram(self, value):
        self.ram += value

    def upgrade_storage(self, value):
        self.storage += value

    def charge(self):
        self.battery_level = 100
        self.battery_life = 10

    def __str__(self):
        return f'Model: {self.model}, Screen size: {self.screen_size}, RAM: {self.ram}, Storage: {self.storage}, Battery life: {self.battery_life}, Battery level: {self.battery_level}'


if __name__ == '__main__':
    laptops = [
        Laptop(),
        Laptop("Acer", 15.6, 16, 512, 10, 100),
        Laptop(),
        Laptop()
    ]

    for laptop in laptops:
        print(laptop)
