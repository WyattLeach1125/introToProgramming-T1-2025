from adafruit_circuitplayground import cp
import time
import random
buffer = False

while True:
    if cp.button_a and not buffer:
        buffer = True
        dice = random.randint(0, 10)
        for i in range(0, dice):
            cp.pixels[i] = (1,1,0)
    elif not cp.button_a and buffer:
        buffer = False
    if cp.button_b:
        dice = random.randint(0, 3)
        cp.pixels.fill((0,0,0))
