from control import Control
from display import Display
from data import SCREEN, FPS, CLOCK, initial_scene


def main():
    display = Display(SCREEN)
    control = Control()
    control.set_state(initial_scene)
    display.set_display(*control.get_gfx())

    while True:
        control.event_loop()
        if control.update_gfx:
            display.set_display(*control.get_gfx())
        display.render_screen()
        CLOCK.tick(FPS)


if __name__ == '__main__':
    main()
