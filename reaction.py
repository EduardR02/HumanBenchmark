import mss
import numpy as np
import time
from pynput.mouse import Button, Controller

pixel_x, pixel_y = 2000, 500
mouse_x, mouse_y = 1800, 500


# noinspection PyTypeChecker
def main():
    mouse = Controller()
    sct = mss.mss()
    monitor = {'top': pixel_y, 'left': pixel_x, 'width': 1, 'height': 1}
    counter = 0
    t = time.time()
    n = 1
    c2 = 0
    mouse.position = (mouse_x, mouse_y)
    while c2 < 5:
        counter += 1
        img = np.asarray(sct.grab(monitor))
        if time.time() - t >= n:
            t = time.time()
            print("FPS:", counter)
            counter = 0
        if img[0][0][1] > 200:
            mouse.press(Button.left)
            mouse.release(Button.left)
            c2 += 1
            time.sleep(0.5)
            print("clicked")
        elif img[0][0][0] > 150:
            mouse.press(Button.left)
            mouse.release(Button.left)
            time.sleep(0.5)


if __name__ == "__main__":
    main()
