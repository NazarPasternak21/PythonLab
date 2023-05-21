from Models.Laptop import Laptop


class Ultrabook(Laptop):
    def __init__(self, model="Asus", screen_size=15.6, ram=16, storage=512, battery_life=5, battery_level=100,
                 weight=1.8, thickness=1.7):
        super().__init__(model, screen_size, ram, storage, battery_life, battery_level)
        self.weight = weight
        self.thickness = thickness

    def replace_battery(self, capacity_in_hours):
        raise NotImplementedError("Battery replacement is not possible for Ultrabook.")

    def __str__(self):
        return f'Model: {self.model}, Screen size: {self.screen_size}, Ram: {self.ram}, Storage: {self.storage}, ' \
               f'Battery life: {self.battery_life}, Battery level: {self.battery_level}, Weight: {self.weight}, ' \
               f'Thickness: {self.thickness}'
