class Input_Handler():
    def __init__(self, LCD):
        self.LCD = LCD
        self.index = 0
        self.button_states = [False, False, False, False, False, False, False, False]
        self.GPIO_KEYS = [
            self.LCD.GPIO_KEY_UP_PIN,
            self.LCD.GPIO_KEY_DOWN_PIN,
            self.LCD.GPIO_KEY_LEFT_PIN,
            self.LCD.GPIO_KEY_RIGHT_PIN,
            self.LCD.GPIO_KEY_PRESS_PIN,
            self.LCD.GPIO_KEY1_PIN,
            self.LCD.GPIO_KEY2_PIN,
            self.LCD.GPIO_KEY3_PIN,
        ]
        self.index_mode_on = True

        self.x_index = 0
        self.y_index = 0

    def update(self, menu_system):
        self.get_button_states(menu_system)



    def get_index(self, menu):
        l = len(menu)
        if l > 0:
            return self.index % l
        else:
            return 0


    def get_button_states(self, menu_system):
        # Up Button
        if self.LCD.digital_read(self.GPIO_KEYS[0]):
            if not self.button_states[0] and self.index_mode_on:
                self.index -= 1
                self.button_states[0] = True
        else:
            self.button_states[0] = False

        # Down Button
        if self.LCD.digital_read(self.GPIO_KEYS[1]):
            if not self.button_states[1] and self.index_mode_on:
                self.index += 1
                self.button_states[1] = True
        else:
            self.button_states[1] = False

        # Center Button
        if self.LCD.digital_read(self.GPIO_KEYS[4]):
            if not self.button_states[4]:
                menu_system.load()
                self.button_states[4] = True
        else:
            self.button_states[4] = False


        # Key3 Back Button
        if self.LCD.digital_read(self.GPIO_KEYS[7]):
            if not self.button_states[7]:
                menu_system.back()
                self.button_states[7] = True
        else:
            self.button_states[7] = False


    def get_keyboard_index(self):
        return (self.x_index, self.y_index)



    def update_keyboard(self, keyboard):

        # Up Button
        if self.LCD.digital_read(self.GPIO_KEYS[0]):
            if not self.button_states[0]:
                self.y_index -= 1
                self.button_states[0] = True
        else:
            self.button_states[0] = False

        # Down Button
        if self.LCD.digital_read(self.GPIO_KEYS[1]):
            if not self.button_states[1]:
                self.y_index += 1
                self.button_states[1] = True
        else:
            self.button_states[1] = False

        # Left Button
        if self.LCD.digital_read(self.GPIO_KEYS[2]):
            if not self.button_states[2]:
                self.x_index -= 1
                self.button_states[2] = True
        else:
            self.button_states[2] = False

        # Right Button
        if self.LCD.digital_read(self.GPIO_KEYS[3]):
            if not self.button_states[3]:
                self.x_index += 1
                self.button_states[3] = True
        else:
            self.button_states[3] = False

        # Key1 Button enter
        if self.LCD.digital_read(self.GPIO_KEYS[5]):
            if not self.button_states[5]:
                keyboard.select()
                self.button_states[5] = True
        else:
            self.button_states[5] = False
        # Center button enter
        if self.LCD.digital_read(self.GPIO_KEYS[4]):
            if not self.button_states[4]:
                keyboard.select()
                self.button_states[4] = True
        else:
            self.button_states[4] = False

        # Key3 Button Switch keyboards
        if self.LCD.digital_read(self.GPIO_KEYS[7]):
            if not self.button_states[7]:
                keyboard.shift()
                self.button_states[7] = True
        else:
            self.button_states[7] = False
