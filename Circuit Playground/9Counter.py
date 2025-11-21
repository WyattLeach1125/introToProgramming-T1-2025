from adafruit_circuitplayground import cp
import time
counter = 0

while True:
    if counter == 10:
        counter = 9
    if counter < 0:
        counter = 0
    if cp.button_a:
        cp.pixels[counter] = (1,1,0)
        counter += 1
    if cp.button_b:
        cp.pixels[counter] = (0,0,0)
        counter -= 1
    time.sleep(.11)
