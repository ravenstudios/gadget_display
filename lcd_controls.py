class LCD_Controls(object):

    def __init__(self, lcd):
        self.lcd = lcd
        self.duty_cycle = 50

    def brightness_up(self):
        self.duty_cycle += 10
        self.set_brightness()
        return "UP"


    def brightness_down(self):
        self.duty_cycle -= 10
        self.set_brightness()
        return "DOWN"

    def set_brightness(self):
        self.duty_cycle = max(20, min(self.duty_cycle, 100))
        self.lcd.bl_DutyCycle(self.duty_cycle)
