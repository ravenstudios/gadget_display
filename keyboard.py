class Keyboard():
    def __init__(self, LCD, inuput_handler):
        self.LCD = LCD
        self.is_active = False
        self.is_shifted = False
        self.font_size = 13
        self.ip = inuput_handler

        self.rows = [
            [
                ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"],
                ["a", "s", "d", "f", "g", "h", "j", "k", "l"],
                ["z", "x", "c", "v", "b", "n", "m"],
                ["SP", "BS", "EN"]

            ],

            [
                ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
                ["A", "S", "D", "F", "G", "H", "J", "K", "L", ],
                ["Z", "X", "C", "V", "B", "N", "M"],
                ["SP", "BS", "EN"]

            ],

            [
                ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
                ["`", "-", "=", "[", "]", "\\", ";", "'"],
                ["~", "_", "+", "{", "}", "|", ":"],
                ["!", "@", "#", "$", "%", "^", "&", "*"],
                ["/", "?", ",", ".", "<", ">", "(", ")"],
                ["SP", "BS", "EN"]

            ]
        ]
        self.row_index = 0
        self.selected_rows = self.rows[self.row_index]
        self.output_string = ""
        self.x = 0
        self.y = 0

    def update(self):
        if self.is_active:
            self.ip.update_keyboard(self)
        print(self.is_active)

    def enter(self):
        self.is_active = False

    def activate(self):
        self.is_active = True

    def select(self):
        print("select")
        char = self.selected_rows[self.y][self.x]
        if char == "SP":
            self.output_string += " "
        elif char == "BS":
            self.output_string = self.output_string[:-1]
        elif char == "EN":
            self.enter()
        else:
            self.output_string += char




    def shift(self):
        self.row_index += 1
        self.row_index = self.row_index % 3
        self.selected_rows = self.rows[self.row_index]


    def draw(self, image, draw, menu_system):

        fs = self.font_size
        font = menu_system.get_font(fs)

        draw.text((0, 0),  self.output_string, fill = "RED", font=font)

        y_pad = 4
        y_space = 20
        x_pad = 2
        ki = self.ip.get_keyboard_index()

        self.y = ki[1] % len(self.selected_rows)
        self.x = ki[0] % len(self.selected_rows[self.y])


        rect_x1 = self.x * fs
        rect_y1 = self.y * fs + (y_pad * self.y) + 2 + y_space
        rect_x2 = rect_x1 + fs
        rect_y2 = rect_y1 + fs

        if (self.selected_rows != 2 and self.y == 3) or self.y == 5:
            rect_x1 = self.x * fs * 2
            rect_y1 = self.y * fs + (y_pad * self.y) + 2 + y_space
            rect_x2 = rect_x1 + fs * 2
            rect_y2 = rect_y1 + fs

        rect = [(rect_x1, rect_y1), (rect_x2, rect_y2)]


        draw.rectangle(rect, fill = "WHITE")

        for r, row in enumerate(self.selected_rows):
            for c, col in enumerate(row):
                if col in ["SP", "BS", "EN"]:
                    x = c * (fs * 2) + (x_pad)
                else:
                    x = (c * fs) + (x_pad)
                y = (r * fs) + (r * y_pad) + y_space
                draw.text((x, y),  col, fill = "BLUE", font=font)
        menu_system.LCD.LCD_ShowImage(image,0,0)
