import LCD_1in44
import time
import subprocess
from PIL import Image,ImageDraw,ImageFont,ImageColor
import time
from get_ip import get_ip

from menu import menu

LCD = LCD_1in44.LCD()

font_size = 20
x_pad = 5
y_pad = 5
index = 0
button_up = False
button_down = False
button_press_pin = False
button_key1 = False
menu_y = 0
current_menu = menu
parrent_menu = []
running_command_flag = False

def update():
    global index, button_up, button_down, button_press_pin, button_key1, menu_y, current_menu, parrent_menu, running_command_flag

    if LCD.digital_read(LCD.GPIO_KEY_UP_PIN ) == 1: # button is released
        if not button_up:
            button_up = True
            index -= 1
    else:
        button_up = False

    if LCD.digital_read(LCD.GPIO_KEY_DOWN_PIN ) == 1: # button is released
        if not button_down:
            button_down = True
            index += 1
    else:
        button_down = False


    if LCD.digital_read(LCD.GPIO_KEY1_PIN ) == 1: # button is released
        if not button_key1:
            button_key1 = True
            if parrent_menu:
                current_menu = parrent_menu[-1]
                parrent_menu.pop()
    else:
        button_key1 = False



    if LCD.digital_read(LCD.GPIO_KEY_PRESS_PIN ) == 1: # button is released
        if not button_press_pin:
            button_press_pin = True
            if current_menu[index % len(current_menu)]["sub_menu"]:
                parrent_menu.append(current_menu)
                current_menu = current_menu[index % len(current_menu)]["sub_menu"]
            elif current_menu[index % len(current_menu)]["command"][0] == "No":
                print("no")
                current_menu = parrent_menu[-1]
                parrent_menu.pop()
            else:
                running_command_flag = True


    else: # button is pressed:
        button_press_pin = False

    menu_y = (index % len(menu)) * font_size

def draw_screen():
    image = Image.new("RGB", (LCD.width, LCD.height), "BLACK")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', font_size)

    if running_command_flag:
        draw.text((x_pad, 0),  current_menu[index % len(current_menu)]["comment"], fill = "BLUE", font=font)
        LCD.LCD_ShowImage(image,0,0)
        time.sleep(3)
        subprocess.run(current_menu[index % len(current_menu)]["command"])
    else:

        draw.rectangle([(0, menu_y),(LCD.width ,menu_y + font_size)], fill = "WHITE")

        for i, item in enumerate(current_menu):
            # print(item)
            draw.text((x_pad, i * font_size),  item["title"], fill = "BLUE", font=font)


    font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', font_size // 2)
    draw.text((x_pad, LCD.height - font_size),  f"IP:{get_ip()}", fill = "BLUE", font=font)
    LCD.LCD_ShowImage(image,0,0)
    # time.sleep(3)


def main():


    Lcd_ScanDir = LCD_1in44.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
    LCD.LCD_Init(Lcd_ScanDir)
    LCD.LCD_Clear()

    while True:
        update()
        draw_screen()

if __name__ == '__main__':
    main()

#except:
#	print("except")
#	GPIO.cleanup()
