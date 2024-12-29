from threading import Event

import pyautogui as pg
from loguru import logger

WHITE_INVENTORY_LOCATION = (1062, 171)


def element(stop_event: Event, terminals_amnt: int):
    logger.debug("Starting element abb macro")

    while not stop_event.is_set():
        pg.sleep(0.1)

        pg.press("2")
        pg.press("2")
        pg.press("3")

        pg.sleep(0.5)

        i = 0
        while i < terminals_amnt:
            pg.press("r")

            pg.sleep(15)

            pg.press("f")

            pg.sleep(3)

            color = pg.pixelMatchesColor(1062, 171, (255, 255, 255))

            if not color:
                pg.keyUp("w")
                pg.sleep(0.3)
                pg.keyDown("w")

                pg.press("f")

                pg.sleep(2)

                color = pg.pixelMatchesColor(1062, 171, (255, 255, 255))

            if not color:
                continue

            pg.sleep(1)

            pg.moveTo(1247, 278)

            pg.leftClick()
            pg.leftClick()
            pg.leftClick()

            pg.sleep(0.5)

            pg.press("escape")

            pg.sleep(0.5)

            i += 1

        pg.press("r")

        pg.sleep(15)

        pg.press("2")
        pg.press("2")
        pg.press("2")
        pg.press("3")

        pg.press("l")
        pg.sleep(25 * 60)
        pg.press("escape")

    logger.debug("Stopping element abb macro")
