from get_ip import get_ip
import lcd_controls


class Menu():
    def __init__(self, LCD):
        self.lcd = lcd_controls.LCD_Controls(LCD)
        self.menu = [
            {
                "title":"SYSTEM",
                "sub_menu":[
                    {
                        "title":"SHUTDOWN",
                        "sub_menu":[
                            {
                                "title":"No",
                                "command":["No"],
                            },
                            {
                                "title":"Yes",
                                "command":["sudo", "shutdown", "-h", "now"],
                                "comment": "Shutting\n Down",
                                "sleep_time": 3,
                            },
                        ],
                    },
                    {
                        "title":"RESTART",
                        "sub_menu":[
                            {
                                "title":"No",
                                "command":["No"],
                            },
                            {
                                "title":"Yes",
                                "command":["sudo", "reboot"],
                                "comment": "Restarting",
                                "sleep_time": 3,
                            },
                        ],
                    },
                    {
                        "title":"GET IP",
                        "p_command":get_ip,
                        "comment": f"IP:\n{get_ip()}",
                        "font_size": 15,
                        "running_command_flag" : True
                    },
                    {
                        "title":"BRIGHTNESS",
                        "sub_menu":[
                            {
                                "title":"UP",
                                "p_command":self.lcd.brightness_up,
                                # "comment": "UP",
                            },
                            {
                                "title":"DOWN",
                                "p_command":self.lcd.brightness_down,
                                # "comment": "DOWN",
                            },
                        ]
                    },
                ],
            },
            {
                "title":"Show Files",
                "sub_menu":[],
                "command":["ls"],

            },
            {
                "title":"MENU 3",
                "sub_menu":[],
                "command":[],

            },
        ]
