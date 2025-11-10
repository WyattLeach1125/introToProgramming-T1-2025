import random

games = ["Elden Ring", "Shadow of the Colossus", "Diablo III", "Minecraft", "Super Mario World"]
for game in games:
    print(game)

#print every number from 1 -5 using a for loop
for i in range(5):
    print(f"Rank {str(i)}: {games[i]}")

#print every odd number from 1-100
for i in range(0, 100, 10):
    print(i)

#1. Generate 100 random numbers
randint_list = []
for i in range(0, 100):
    randint_list.append(random.randint(-100, 101))

#2. Print only positive numbers
for i in range(0, len(randint_list)):
    if randint_list[i] < 0:
        randint_list.pop(i)

print(randint_list)