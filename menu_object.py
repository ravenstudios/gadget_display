class Menu_Object(object):

    def __init__(self, title=None, sub_menu=None, command=None, pycommand=None, comment=None, font_size=None):
        self.title = title
        self.sub_menu = sub_menu
        self.command = command
        self.py_command = py_command
        self.comment = comment
        self.font_size = font_size

    def update(self):
        pass

    def draw(self):
        pass

    def command(self):
        pass

    def py_command(self):
        pass
