from control import Control
from display import Display
from data import SCREEN


def main():
    display = Display(SCREEN)
    control = Control()
    display.set_display(*control.get_gfx())

    display.render_screen()


main()