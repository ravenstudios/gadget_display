import LCD_1in44
import time
import subprocess
from PIL import Image,ImageDraw,ImageFont,ImageColor
import time
from get_ip import get_ip

import menu
import lcd_controls
from get_battery import get_battery

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



def update():
    global index, button_up, button_down, button_press_pin, button_key1, menu_y, current_menu, parrent_menu, running_command_flag


    item = current_menu[index % len(current_menu)]



    if LCD.digital_read(LCD.GPIO_KEY_UP_PIN ) == 1:
        if not button_up:
            button_up = True
            index -= 1
    else:
        button_up = False

    if LCD.digital_read(LCD.GPIO_KEY_DOWN_PIN ) == 1:
        if not button_down:
            button_down = True
            index += 1
    else:
        button_down = False


    if LCD.digital_read(LCD.GPIO_KEY3_PIN ) == 1 or LCD.digital_read(LCD.GPIO_KEY_LEFT_PIN ) == 1:#Back Button
        if not button_key1:
            button_key1 = True
            running_command_flag = False
            index = 0
            if parrent_menu:
                current_menu = parrent_menu[-1]
                parrent_menu.pop()
    else:
        button_key1 = False



    if LCD.digital_read(LCD.GPIO_KEY_PRESS_PIN ) == 1 or LCD.digital_read(LCD.GPIO_KEY_RIGHT_PIN ) == 1 or LCD.digital_read(LCD.GPIO_KEY1_PIN ) == 1:
        if not button_press_pin:
            button_press_pin = True
            if item.get("sub_menu"):
                parrent_menu.append(current_menu)
                current_menu = current_menu[index % len(current_menu)]["sub_menu"]
                index = 0

            elif item.get("command"):
                if item["command"][0] == "No":   #Go Back
                    current_menu = parrent_menu[-1]
                    parrent_menu.pop()
                else:
                    running_command_flag = True
            elif item.get("p_command"):
                item["p_command"]()
                if item.get("running_command_flag"):
                    running_command_flag = True
    else: # button is pressed:
        button_press_pin = False

    menu_y = (index % len(current_menu)) * font_size

def draw_screen():
    menu_item = current_menu[index % len(current_menu)]
    image = Image.new("RGB", (LCD.width, LCD.height), "BLACK")
    draw = ImageDraw.Draw(image)
    # font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', font_size)
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf", font_size)
    if running_command_flag:
        if menu_item.get("font_size"):
            # font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', menu_item["font_size"])
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf", menu_item["font_size"])
        if menu_item.get("comment"):
            draw.text((x_pad, 0),  menu_item["comment"], fill = "BLUE", font=font)
            LCD.LCD_ShowImage(image,0,0)
        if menu_item.get("sleep_time"):
            time.sleep(menu_item["sleep_time"])
        if menu_item.get("command"):
            # subprocess.run(menu_item["command"])
            result = subprocess.run(menu_item["command"], capture_output=True, text=True)
            draw.text((x_pad, 0),  result.stdout, fill = "BLUE", font=font)
            LCD.LCD_ShowImage(image,0,0)
    else:

        draw.rectangle([(0, menu_y),(LCD.width ,menu_y + font_size)], fill = "WHITE")

        for i, item in enumerate(current_menu):
            draw.text((x_pad, i * font_size),  item["title"], fill = "BLUE", font=font)


    batt = f"{float(get_battery()):.0f}"
    # font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', font_size)

    draw.text((75, LCD.height - font_size - 1),  f"\U000026A1{batt}%", fill = "WHITE", font=font)
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
