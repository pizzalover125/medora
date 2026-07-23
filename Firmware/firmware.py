import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.GP10, 8, brightness=0.3, auto_write=False)

RED = (255, 0, 0)
OFF = (0, 0, 0)

while True:
    pixels.fill(RED)
    pixels.show()
    time.sleep(0.5)

    pixels.fill(OFF)
    pixels.show()
    time.sleep(0.5)