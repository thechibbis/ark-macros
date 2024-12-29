from threading import Event

import pyautogui as pg
from loguru import logger


def achatina(stop_event: Event):
    logger.debug("Starting achatina macro")

    while not stop_event.is_set():
        pg.sleep(0.1)

        pg.press("ctrlleft")

        pg.sleep(1.0)

        pg.keyDown("down")
        pg.sleep(3.0)
        pg.keyUp("down")

        pg.sleep(0.2)

        pg.press("e")

        pg.sleep(1)

        pg.keyDown("up")
        pg.sleep(2.0)
        pg.keyUp("up")

        pg.sleep(0.5)

        pg.press("l")

        pg.sleep(5)

        pg.press("escape")

        pg.sleep(2)

    logger.debug("Stopping achatina macro")
