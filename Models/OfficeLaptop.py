from Models.Laptop import Laptop


class OfficeLaptop(Laptop):
    def __init__(self, model="Lenovo", screen_size=17.3, ram=16, storage=256, battery_life=6, battery_level=100,
                 color="Black", price=25000):
        super().__init__(model, screen_size, ram, storage, battery_life, battery_level)
        self.color = color
        self.price = price

    def __str__(self):
        return f'Model: {self.model}, Screen size: {self.screen_size}, Ram: {self.ram}, Storage: {self.storage}, ' \
               f'Battery life: {self.battery_life}, Battery level: {self.battery_level}, Color: {self.color}, ' \
               f'Price: {self.price}'
