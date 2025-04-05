class LCD_Controls(object):

    def __init__(self, lcd):
        self.lcd = lcd
        self.duty_cycle = 50

    def brightness_up(self):
        self.duty_cycle += 10
        self.lcd.bl_DutyCycle(self.duty_cycle)

    def brightness_down(self):
        self.duty_cycle -= 10
        self.lcd.bl_DutyCycle(self.duty_cycle)
        if self.duty_cycle < 20:
             self.duty_cycle = 20
