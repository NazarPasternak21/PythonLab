from Models.laptop import Laptop


class StudentLaptop(Laptop):
    def __init__(self, model="Acer", screen_size=17.3, ram=32, storage=1024, battery_life=12, battery_level=100,
                 Processor="Intel Core i7", Producing_Country="China"):
        super().__init__(model, screen_size, ram, storage, battery_life, battery_level)
        self.Processor = Processor
        self.Producing_Country = Producing_Country

    def __str__(self):
        return f'Model: {self.model}, Screen size: {self.screen_size}, Ram: {self.ram}, Storage: {self.storage}, ' \
               f'Battery life: {self.battery_life}, Battery level: {self.battery_level}, Processor: {self.Processor}, ' \
               f'Producing_Country: {self.Producing_Country}'
