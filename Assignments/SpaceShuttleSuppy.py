import os

os.system('cls')
print("\n")
print("Shuttle is preparing to launch, please make preperations listed:\n")
countdown = input("Insert seconds left until launch\n>")
oxygen_tanks = input("Insert amount of oxygen tanks stored\n>")
food_packs = input("Insert amount of food packs stored\n>")
water_packs = input("Insert amount of water packs stored\n>")

print("\n")
print(f" Countdown: {countdown}\n Oxygen tanks: {oxygen_tanks}\n Food packs: {food_packs}\n Water packs: {water_packs}\n")

oxygen_tanks = input("Please confirm oxygen tank supply, we implore you to double check:\n>")

print("\n")
print(f" Countdown: {countdown}\n Oxygen tanks: {oxygen_tanks}\n Food packs: {food_packs}\n Water packs: {water_packs}\n")
