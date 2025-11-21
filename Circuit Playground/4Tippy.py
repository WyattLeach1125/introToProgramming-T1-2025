from adafruit_circuitplayground import cp

while True:
    x, y, z = cp.acceleration
    if x > 0:
        for i in range(1, 4):
            cp.pixels[i] = (0,1,0)
        for v in range(6, 9):
            cp.pixels[v] = (0,0,0)
    else:
        for v in range(6, 9):
            cp.pixels[v] = (0,1,0)
        for i in range(1, 4):
            cp.pixels[i] = (0,0,0) #there has to be a beter way to do this
