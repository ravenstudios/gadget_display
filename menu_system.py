from menu_object import Menu_Object

class Menu_SYSTEM(Menu_Object):
    def __init__(self):
        super().__init__()  # Call parent constructor
        self.title = "SYSTEM"
        self.sub_menu = [
            Menu_Shutdown(),
            Menu_Restart()

        ]


class Menu_Shutdown(Menu_Object):
    def __init__(self):
        super().__init__()  # Call parent constructor
        self.title = "SHUTDOWN"
        menu_shutdown_yes = Menu_Object()
        menu_shutdown_yes.title = "Yes"
        menu_shutdown_yes.command = ["sudo", "shutdown", "-h", "now"]
        menu_shutdown_no = Menu_Object()
        menu_shutdown_no.title = "No"
        self.sub_menu = [
            menu_shutdown_yes,
            menu_shutdown_no
        ]


class Menu_Restart(Menu_Object):
    def __init__(self):
        super().__init__()  # Call parent constructor
        self.title = "RESTART"
        menu_restart_yes = Menu_Object()
        menu_restart_yes.title = "Yes"
        menu_restart_yes.command = ["sudo", "reboot"]
        menu_restart_no = Menu_Object()
        menu_restart_no.title = "No"
        self.sub_menu = [
            menu_restart_yes,
            menu_restart_no
        ]
