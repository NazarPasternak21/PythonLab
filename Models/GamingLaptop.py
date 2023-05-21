from Models.Laptop import Laptop


class GamingLaptop(Laptop):
    def __init__(self, model="Asus", screen_size=17.3, ram=32, storage=1024, battery_life=8, battery_level=100,
                 gpu="NVIDIA GeForce RTX 3080", fan_count=2):
        super().__init__(model, screen_size, ram, storage, battery_life, battery_level)
        self.gpu = gpu
        self.fan_count = fan_count

    def __str__(self):
        return f'Model: {self.model}, Screen size: {self.screen_size}, Ram: {self.ram}, Storage: {self.storage}, ' \
               f'Battery life: {self.battery_life}, Battery level: {self.battery_level}, GPU: {self.gpu}, ' \
               f'Fan count: {self.fan_count}'
