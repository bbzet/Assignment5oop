from device import Device

class Tablet(Device):

    def __init__(self, name, price, stock, warranty_period, screen_resolution, weight):
        super().__init__(name, price, stock, warranty_period)
        self.screen_resolution = screen_resolution
        self.weight = weight

    def browse_internet(self):
        return 'Browsing the internet'

    def use_touch_screen(self):
        return 'Using the touch screen'


