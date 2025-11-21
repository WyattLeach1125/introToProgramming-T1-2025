from adafruit_circuitplayground import cp
import time

while True:
    lightMeter = cp.light
    if lightMeter <= 30:
        cp.pixels[0] = (1,1,0)
    else:
        cp.pixels[0] = (0,0,0)
    if lightMeter <= 27:
        cp.pixels[1] = (1,1,0)
    else:
        cp.pixels[1] = (0,0,0)
    if lightMeter <= 24:
        cp.pixels[2] = (1,1,0)
    else:
        cp.pixels[2] = (0,0,0)
    if lightMeter <= 21:
        cp.pixels[3] = (1,1,0)
    else:
        cp.pixels[3] = (0,0,0)
    if lightMeter <= 18:
        cp.pixels[4] = (1,1,0)
    else:
        cp.pixels[4] = (0,0,0)
    if lightMeter <= 15:
        cp.pixels[5] = (1,1,0)
    else:
        cp.pixels[5] = (0,0,0)
    if lightMeter <= 12:
        cp.pixels[6] = (1,1,0)
    else:
        cp.pixels[6] = (0,0,0)
    if lightMeter <= 9:
        cp.pixels[7] = (1,1,0)
    else:
        cp.pixels[7] = (0,0,0)
    if lightMeter <= 6:
        cp.pixels[8] = (1,1,0)
    else:
        cp.pixels[8] = (0,0,0)
    if lightMeter <= 3:
        cp.pixels[9] = (1,1,0)
    else:
        cp.pixels[9] = (0,0,0)
    time.sleep(0.5) #this exists so my eyes dont hurt, side note: my light meter might be a bit glitchy for some reason?