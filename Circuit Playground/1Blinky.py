from adafruit_circuitplayground import cp
import time

while True:
    blinky = cp.pixels[0][1]
    cp.pixels.fill((0,1-blinky,0)) # the color is sent so low so it doesn't hurt my eyes :)
    time.sleep(.367)
    