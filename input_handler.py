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

    def update(self):
        for index, pin in enumerate(self.GPIO_KEYS):
            if self.LCD.digital_read(pin) == 1:
                self.button_states[index] = True
            else:
                self.button_states[index] = False

#
# global , menu_y, current_menu, parrent_menu, running_command_flag
#
#
# item = current_menu[index % len(current_menu)]
#
#
#     def inputs(self):
#
# if LCD.digital_read(LCD.GPIO_KEY_UP_PIN ) == 1:
#     if not button_up:
#         button_up = True
#         index -= 1
# else:
#     button_up = False
#
# if LCD.digital_read(LCD.GPIO_KEY_DOWN_PIN ) == 1:
#     if not button_down:
#         button_down = True
#         index += 1
# else:
#     button_down = False
#
#
# if LCD.digital_read(LCD.GPIO_KEY1_PIN ) == 1:#Back Button
#     if not button_key1:
#         button_key1 = True
#         running_command_flag = False
#         index = 0
#         if parrent_menu:
#             current_menu = parrent_menu[-1]
#             parrent_menu.pop()
#
# else:
#     button_key1 = False
#
#
#
# if LCD.digital_read(LCD.GPIO_KEY_PRESS_PIN ) == 1:
#     if not button_press_pin:
#         button_press_pin = True
#         if item.get("sub_menu"):
#             parrent_menu.append(current_menu)
#             current_menu = current_menu[index % len(current_menu)]["sub_menu"]
#             index = 0
#
#         elif item.get("command"):
#             if item["command"][0] == "No":   #Go Back
#                 current_menu = parrent_menu[-1]
#                 parrent_menu.pop()
#         elif item.get("p_command"):
#             item["p_command"]()
#             running_command_flag = True
#
#
#
#
# else: # button is pressed:
#     button_press_pin = False
#
# menu_y = (index % len(current_menu)) * font_size
