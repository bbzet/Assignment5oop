from device import Device

class Laptop(Device):
    def __init__(self, name, price, stock, warranty_perdiod, ram_size, processor_speed):
        super().__init__(name, price, stock, warranty_perdiod)
        self.ram_size = ram_size
        self.processor_speed = processor_speed

    def run_program(self):
        return 'Running a program'

    def use_keyboard(self):
        return 'Using the keyboard'

