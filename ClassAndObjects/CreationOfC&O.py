class Bulb:
    def __init__(self, onOff):
        self.onOff=onOff
    def turnOn(self):
        print("on")
    def turnOff(self):
        print("off")

surya=Bulb("true")
surya.turnOn()