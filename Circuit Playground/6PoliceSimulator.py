from adafruit_circuitplayground import cp
import time

while True:
    light = cp.pixels[0][1]
    cp.pixels.fill((0,0,1-light)) # the color is sent so low so it doesn't hurt my eyes :)
    cp.play_tone(500, 0.5)
    cp.pixels.fill((1-light,0,0)) # the color is sent so low so it doesn't hurt my eyes :)
    cp.play_tone(900, 0.5)
