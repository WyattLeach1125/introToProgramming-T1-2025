from adafruit_circuitplayground import cp
import time

while True:
    if cp.switch:
        for i in range(0, 5):
            cp.pixels[i] = (0,1,0)
        for v in range(5, 10):
            cp.pixels[v] = (0,0,0)
    else:
        for v in range(5, 10):
            cp.pixels[v] = (0,1,0)
        for i in range(0,5):
            cp.pixels[i] = (0,0,0) #there has to be a beter way to do this
