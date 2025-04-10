from menu_object import Menu_Object
from get_ip import get_ip
from lcd_controls import LCD_Controls

def system_menu(LCD):
    system_menu = Menu_Object(title="System")

    lcd = LCD_Controls(LCD)

    get_ip_menu = Menu_Object(title="Get IP", py_command=get_ip, font_size=14)

    shutdown_yes = Menu_Object(title="Yes", command=["sudo", "shutdown", "-h", "now"], comment="Shuting\nDown...")
    shutdown_no = Menu_Object(title="No")
    shutdown_menu = Menu_Object(title="Shutdown", sub_menu=[shutdown_no, shutdown_yes])

    reboot_yes = Menu_Object(title="Yes", command=["sudo", "reboot"], font_size=14, comment="Rebooting...")
    reboot_no = Menu_Object(title="No")
    reboot_menu = Menu_Object(title="Reboot", sub_menu=[reboot_no, reboot_yes])

    brightness_up = Menu_Object(title="UP", py_command=lcd.brightness_up, comment="UP")
    brightness_down = Menu_Object(title="DOWN", py_command=lcd.brightness_down, comment="DOWN")

    brightness = Menu_Object(title="Brightness", sub_menu=[brightness_up, brightness_down])

    system_menu.sub_menu = [
        shutdown_menu,
        reboot_menu,
        get_ip_menu,
        brightness
    ]
    return system_menu


def main_menu(LCD, keyboard, menu_system):

    sys_menu = system_menu(LCD)
    menu2 = Menu_Object(title="Keyboard", py_command=lambda: keyboard.activate(menu_system.back))
    menu3 = Menu_Object(title="Menu 3")
    main_menu = Menu_Object(sub_menu=[sys_menu, menu2, menu3])
    return main_menu
