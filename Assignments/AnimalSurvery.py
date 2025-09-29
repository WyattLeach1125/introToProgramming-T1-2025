import os

print("\nAnimal Survey\n")

#asking the user to input answers to a few questions
fav_animal = input("What is your favorite animal?\n>")
question_fav_animal = input("Why is this your favorite animal?\n>")
sound_fav_animal = input("What sound does your favorite animal make?\n>")
location_fav_animal = input("Where does your favorite animal originate?\n>")
fact_fav_animal = input("What is a random fact about your favorite animal?\n>")
color_fav_animal = input("What color is your favorite animal?\n>")
land_sea_sky_fav_animal = input("Does your favorite animal walk, swim, or fly?\n>")
diet_fav_animal = input("What does your favorite animal eat?\n>")
size_fav_animal = input("What is the size of your favorite animal?\n>")
children_fav_animal = input("How does your favorite animal raise its young?\n>")

#this clears the terminal
os.system('cls')
print("\nAnimal Survey\n")

#this prints all the answers to the questions
print(f"Your favorite animal:\n>{fav_animal}")
print(f"Reason for that being your favorite animal:\n>{question_fav_animal}")
print(f"Sound that your favorite animal makes:\n>{sound_fav_animal}")
print(f"Location of your favorite animal:\n>{location_fav_animal}")
print(f"Fun fact about your favorite animal:\n>{fact_fav_animal}")
print(f"Color of your favorite animal:\n>{fact_fav_animal}")
print(f"If your animal walks, swims, or flys:\n{land_sea_sky_fav_animal}")
print(f"Food of your favorite animal:\n>{diet_fav_animal}")
print(f"Size of your favorite animal:\n>{size_fav_animal}")
print(f"How your favorite child raises its young:\n>{children_fav_animal}")

print("\nThank you for participating in our survey\n")
