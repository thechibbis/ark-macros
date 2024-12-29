from threading import Event
import pyautogui as pg


def eat_n_drink(stop_event: Event):
    print("Starting eat_n_drink macro")
    while stop_event.is_set():
        pg.sleep(10 * 60)

        pg.sleep(1)

        pg.press("2")
        pg.press("2")
        pg.press("2")

        pg.sleep(0.25)

        pg.press("3")
        pg.press("3")
        pg.press("3")

        pg.sleep(0.1)
    print("Stopping eat_n_drink macro")
