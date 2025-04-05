import LCD_1in44
import time
import subprocess
from PIL import Image,ImageDraw,ImageFont,ImageColor
import time
from get_ip import get_ip

import menu
import lcd_controls

import input_handler

LCD = LCD_1in44.LCD()
menu = menu.Menu(LCD)

font_size = 20
x_pad = 5
y_pad = 5
index = 0
button_up = False
button_down = False
button_press_pin = False
button_key1 = False
menu_y = 0
current_menu = menu.menu
parrent_menu = []
running_command_flag = False

ip = input_handler.Input_Handler(LCD)

def update():
    ip.update()

def draw_screen():
    menu_item = current_menu[index % len(current_menu)]
    image = Image.new("RGB", (LCD.width, LCD.height), "BLACK")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', font_size)

    if running_command_flag:
        if menu_item.get("font_size"):
            font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', menu_item["font_size"])
        if menu_item.get("comment"):
            draw.text((x_pad, 0),  menu_item["comment"], fill = "BLUE", font=font)
            LCD.LCD_ShowImage(image,0,0)
        if menu_item.get("sleep_time"):
            time.sleep(menu_item["sleep_time"])
        if menu_item.get("command"):
            subprocess.run(menu_item["command"])

    else:

        draw.rectangle([(0, menu_y),(LCD.width ,menu_y + font_size)], fill = "WHITE")

        for i, item in enumerate(current_menu):
            draw.text((x_pad, i * font_size),  item["title"], fill = "BLUE", font=font)

    LCD.LCD_ShowImage(image,0,0)


def main():
    Lcd_ScanDir = LCD_1in44.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
    LCD.LCD_Init(Lcd_ScanDir)
    LCD.LCD_Clear()

    while True:
        update()
        draw_screen()

if __name__ == '__main__':
    main()
