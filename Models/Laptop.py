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

    def replace_battery(self, capacity_in_hours):
        self.battery_life = capacity_in_hours
        self.battery_level = 100

    def __str__(self):
        return f"Model: {self.model}, Screen size: {self.screen_size}, Ram: {self.ram}, " \
               f"Storage: {self.storage}, Battery life: {self.battery_life}, " \
               f"Battery level: {self.battery_level}"
