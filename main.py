import menu_system

menu_system = menu_system.Menu_System()

def update():
    menu_system.update()

def draw():
    menu_system.draw()


def main():


    while True:
        update()
        draw()

if __name__ == '__main__':
    main()
