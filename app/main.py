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
        if control.change:
            display.set_display(*control.get_gfx())
        display.render_screen()
        CLOCK.tick(FPS)


if __name__ == '__main__':
    main()

# TODO:
# Need more tests
# Code 'start' somewhere else so init values all in one place
# setup should also pull from that somewhere for screen size info

# TODO
# Next project step:
# Battle field
# Enemy/ally commander
# One unit on each side
# Give commands - commands refresh when all are used
# Whichever commander loses all HP loses.

# Spells, summoning, mana, and other details next step
