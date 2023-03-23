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


if __name__ == '__main__':
    main()

# TODO:
# Need more tests
# Code 'start' somewhere else so init values all in one place
# setup should also pull from that somewhere for screen size info
