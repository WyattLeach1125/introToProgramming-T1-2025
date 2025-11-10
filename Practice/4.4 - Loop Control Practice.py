import random

for i in range(1, 21):
    if i == 15:
        break
    print(i)

for i in range(30):
    if i % 2 == 0:
        continue
    print(i)

for i in range(10):
    pass # to pick a random number out of 10
    print(i)

for i in range(10, 1, -1):
    if i == 5: continue
    print(i)

list = [5, 4, 3, 2, 1, 0 , -1, -2, -3]
sum = 0
for i in list:
    if i <= -1:
        break
    sum += i
print(sum)