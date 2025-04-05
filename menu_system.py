from menu_object import Menu_Object
from get_ip import get_ip
from lcd_controls import LCD_Controls

import subprocess
from PIL import Image,ImageDraw,ImageFont,ImageColor
import time
import input_handler
import LCD_1in44
import subprocess



def system_menu(LCD):
    system_menu = Menu_Object(title="System")

    lcd = LCD_Controls(LCD)

    get_ip_menu = Menu_Object(title="Get IP", py_command=get_ip, font_size=14)

    shutdown_yes = Menu_Object(title="Yes", command=["sudo", "shutdown", "-h", "now"], comment="Shuting Down...")
    shutdown_no = Menu_Object(title="No")
    shutdown_menu = Menu_Object(title="Shutdown", sub_menu=[shutdown_yes, shutdown_no])

    reboot_yes = Menu_Object(title="Yes", command=["sudo", "reboot"], comment="Rebooting...")
    reboot_no = Menu_Object(title="No")
    reboot_menu = Menu_Object(title="Reboot", sub_menu=[reboot_yes, reboot_no])

<<<<<<< HEAD
    
=======
    brightness_up = Menu_Object(title="UP", py_command=lcd.brightness_up, comment="UP")
    brightness_down = Menu_Object(title="DOWN", py_command=lcd.brightness_down, comment="DOWN")
>>>>>>> class
    brightness = Menu_Object(title="Brightness", sub_menu=[brightness_up, brightness_down])

    system_menu.sub_menu = [
        shutdown_menu,
        reboot_menu,
        get_ip_menu,
        brightness
    ]
    return system_menu


def main_menu(LCD):
    menu2 = Menu_Object(title="Menu 2")
    menu3 = Menu_Object(title="Menu 3")
    sys_menu = system_menu(LCD)
    main_menu = Menu_Object(sub_menu=[sys_menu, menu2, menu3])
    return main_menu

class Menu_System():
    def __init__(self):
        self.LCD = LCD_1in44.LCD()
        self.Lcd_ScanDir = LCD_1in44.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
        self.LCD.LCD_Init(self.Lcd_ScanDir)
        self.LCD.LCD_Clear()
        self.ip = input_handler.Input_Handler(self.LCD)
        self.current_menu = main_menu(self.LCD).sub_menu
        self.parrent_menu = []
        self.font_size = 20
        self.command_flag = False
        self.py_command_flag = False


    def update(self):
        self.ip.update(self)



    def draw(self):
            image = Image.new("RGB", (self.LCD.width, self.LCD.height), "BLACK")
            draw = ImageDraw.Draw(image)
            font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', self.font_size)
            x_pad = 5
            y_pad = 5



            if self.py_command_flag:
                command = self.current_menu[self.ip.get_index(self.current_menu)].py_command()
                if self.current_menu[self.ip.get_index(self.current_menu)].font_size:
                    font_size = self.current_menu[self.ip.get_index(self.current_menu)].font_size
                    font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', font_size)
                draw.text((x_pad, y_pad),  command, fill = "BLUE", font=font)
                self.parrent_menu.append(self.current_menu)
                self.ip.index_mode_on = False

            elif self.command_flag:
                command = self.current_menu[self.ip.get_index(self.current_menu)].command
                if self.current_menu[self.ip.get_index(self.current_menu)].font_size:
                    font_size = self.current_menu[self.ip.get_index(self.current_menu)].font_size
                    font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', font_size)
                comment = self.current_menu[self.ip.get_index(self.current_menu)].comment
                draw.text((x_pad, y_pad),  comment, fill = "BLUE", font=font)
                self.LCD.LCD_ShowImage(image,0,0)
                time.sleep(3)
                subprocess.run(command)
                self.parrent_menu.append(self.current_menu)
                self.ip.index_mode_on = False


            else:
                menu_y = self.ip.get_index(self.current_menu) % len(self.current_menu) * self.font_size
                draw.rectangle([(0, menu_y),(self.LCD.width ,menu_y + self.font_size)], fill = "WHITE")
                for i, item in enumerate(self.current_menu):
                    draw.text((x_pad, i * self.font_size),  item.title, fill = "BLUE", font=font)

            self.LCD.LCD_ShowImage(image,0,0)


    def back(self):
        if self.parrent_menu:
            self.current_menu = self.parrent_menu[-1]
            self.parrent_menu.pop()
            self.command_flag = False
            self.ip.index_mode_on = True



    def load(self):
        if self.current_menu[self.ip.get_index(self.current_menu)].sub_menu:
            self.parrent_menu.append(self.current_menu)
            self.current_menu = self.current_menu[self.ip.get_index(self.current_menu)].sub_menu

        elif self.current_menu[self.ip.get_index(self.current_menu)].py_command:
            self.py_command_flag = True

        elif self.current_menu[self.ip.get_index(self.current_menu)].command:
            self.command_flag = True
