from threading import Event

import pyautogui as pg
from loguru import logger


def gacha(stop_event: Event, towers_amnt: int):
    logger.debug("Starting gacha macro")

    while not stop_event.is_set():
        pg.sleep(0.1)

        pg.sleep(1.0)

        pg.press("e")
        pg.sleep(3.0)
        pg.press("e")

        pg.sleep(0.5)

        pg.press("2")
        pg.press("2")
        pg.press("3")

        pg.sleep(0.5)

        pg.keyDown("down")
        pg.sleep(0.25)
        pg.keyUp("down")

        i = 0
        while i < towers_amnt:
            pg.press("r")

            pg.sleep(3)

            pg.sleep(0.3)
            pg.press("ctrlleft")
            pg.sleep(0.3)

            pg.sleep(1.0)

            i += 1

        pg.sleep(0.5)

        pg.press("r")

        pg.sleep(3)

        #
        pg.press("capslock")

        pg.sleep(2)

        pg.leftClick(261, 197)

        pg.write("gacha crystal", interval=0.15)

        pg.leftClick(220, 279)

        i = 0
        while i < 15:
            pg.moveTo(220, 279)
            pg.press("e")

            pg.sleep(0.1)

            pg.moveTo(313, 279)
            pg.press("e")

            pg.sleep(0.1)

            pg.moveTo(407, 279)
            pg.press("e")

            pg.sleep(0.1)

            pg.moveTo(505, 279)
            pg.press("e")

            pg.sleep(0.1)

            pg.moveTo(594, 279)
            pg.press("e")

            pg.sleep(0.1)

            pg.moveTo(684, 279)
            pg.press("e")

            i += 1

        pg.sleep(0.5)
        pg.press("escape")
        pg.sleep(2.0)

        pg.press("e")
        pg.sleep(3.0)
        pg.press("e")

        pg.keyDown("left")
        pg.sleep(2)
        pg.keyUp("left")

        pg.sleep(0.7)

        pg.press("e", presses=3)

        pg.sleep(0.7)

        pg.keyDown("right")
        pg.sleep(4)
        pg.keyUp("right")

        pg.sleep(0.7)

        pg.press("e", presses=3)

        pg.sleep(0.7)

        pg.keyDown("left")
        pg.sleep(2)
        pg.keyUp("left")

        pg.sleep(0.5)

        pg.press("l")
        pg.sleep(5 * 60)
        pg.press("escape")

    logger.debug("Stopping gacha macro")
