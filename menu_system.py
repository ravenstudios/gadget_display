from menu_object import Menu_Object
from get_ip import get_ip
from lcd_controls import LCD_Controls
from get_battery import get_battery
import subprocess
from PIL import Image,ImageDraw,ImageFont,ImageColor
import time
import input_handler
import LCD_1in44
import keyboard
from menu import main_menu



class Menu_System():
    def __init__(self):
        self.LCD = LCD_1in44.LCD()
        self.Lcd_ScanDir = LCD_1in44.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
        self.LCD.LCD_Init(self.Lcd_ScanDir)
        self.LCD.LCD_Clear()
        self.ip = input_handler.Input_Handler(self.LCD)

        self.parrent_menu = []
        self.font_size = 20
        self.command_flag = False
        self.py_command_flag = False
        self.keyboard = keyboard.Keyboard(self.LCD, self.ip)
        self.current_menu = main_menu(self.LCD, self.keyboard).sub_menu

    def update(self):
        self.keyboard.update()
        self.ip.update(self)



    def draw(self):
            image = Image.new("RGB", (self.LCD.width, self.LCD.height), "BLACK")
            draw = ImageDraw.Draw(image)
            # font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', self.font_size)
            font = self.get_font(self.font_size)

            x_pad = 5
            y_pad = 5




            if self.keyboard.is_active:
                self.keyboard.draw(image, draw, self)


            elif self.py_command_flag:
                command = self.current_menu[self.ip.get_index(self.current_menu)].py_command()
                if self.current_menu[self.ip.get_index(self.current_menu)].font_size:
                    font_size = self.current_menu[self.ip.get_index(self.current_menu)].font_size
                    font = self.get_font(font_size)
                if command:
                    draw.text((x_pad, y_pad),  command, fill = "BLUE", font=font)
                self.parrent_menu.append(self.current_menu)
                self.ip.index_mode_on = False

            elif self.command_flag:
                command = self.current_menu[self.ip.get_index(self.current_menu)].command
                if self.current_menu[self.ip.get_index(self.current_menu)].font_size:
                    font_size = self.current_menu[self.ip.get_index(self.current_menu)].font_size
                    font = self.get_font(font_size)
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

            if not self.keyboard.is_active:
                batt = f"{float(get_battery()):.0f}"
                draw.text((75, self.LCD.height - self.font_size - 1),  f"\U000026A1{batt}%", fill = "WHITE", font=font)
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



    def get_font(self, size):
        return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf", size)
