from threading import Event, Thread

import pyautogui as pg
from loguru import logger
from pynput import keyboard

import achatina
import element
import gacha
from utils import eat_n_drink

stop_event = Event()


def on_key_press(key):
    if key == keyboard.Key.f1:
        stop_event.set()
    elif key == keyboard.Key.f2:
        print(pg.position())

    elif key == keyboard.Key.f7:
        if stop_event.is_set():
            stop_event.clear()
        Thread(
            target=gacha.gacha,
            args=(
                stop_event,
                4,
            ),
        ).start()
    elif key == keyboard.Key.f8:
        if stop_event.is_set():
            stop_event.clear()
        Thread(target=achatina.achatina, args=(stop_event,)).start()
        Thread(target=eat_n_drink, args=(stop_event,)).start()
    elif key == keyboard.Key.f9:
        if stop_event.is_set():
            stop_event.clear()
        Thread(
            target=element.element,
            args=(
                stop_event,
                54,
            ),
        ).start()


if __name__ == "__main__":
    logger.info("    F1 -> Stop/exit")
    logger.info("    F7 -> Gacha")
    logger.info("    F8 -> Achatina")
    logger.info("    F9 -> Element Abb")

    listener = keyboard.Listener(on_press=on_key_press)
    listener.start()
    listener.join()
