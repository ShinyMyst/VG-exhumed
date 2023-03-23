from control import Control
from display import Display
from data import SCREEN, FPS, CLOCK


def main():
    display = Display(SCREEN)
    control = Control()
    control.set_state('start')
    display.set_display(*control.get_gfx())

    while True:
        control.event_loop()
        display.render_screen()
        CLOCK.tick(FPS)



main()


# Need more tests
# Reorganize this file