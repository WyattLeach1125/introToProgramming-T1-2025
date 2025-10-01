#woah!!! :O

#Parameters AND arguements

#Create a function that adds 2 numbers together
def add(x,y,z):
    print(x+y+z)


add(10,30,1)
add(12,4,3)

'''
Create a function called add_five_numbers that takes five parameters
-one for each number
print the sum of the five numbers
run the function three times with different arguements
'''

def add_five_numbers(a, b, c, d, e):
    print(a+b+c+d+e)

add_five_numbers(1, 2, 3, 4, 5)
add_five_numbers(6, 7, 8, 9, 10)
add_five_numbers(11, 12, 13, 14, 15)


'''
Create a function calle full_name that prints the concatenation of a person's first and last name
take input using the input function, then run the function once
'''

def full_name(firstName, lastName):
    print(f"{firstName} {lastName}")

full_name(input("Firstname: "), input("Lastname: "))


'''
Create a function called area_calculator that calculates the area of a rectangle.
Take Length and width as parameters.
Run the function three times. No input.
'''

def area_calculator(length, width):
    print(f"The area of a rectangle is the Length times the Width\narea: {length*width}")

area_calculator(1, 2)
area_calculator(3, 4)
area_calculator(5, 6)

'''
Create a function called word_smash that takes 2 parameters.
The function should simply concatenate the 2 parameters
Convert the arguements as strings within the functions to gaurd against non-string values
Rune the function 3 times
'''

def word_smash(a, b):
    print(str(a)+str(b))

word_smash(1, "a")
word_smash(2, "b")
word_smash(3, "c")

'''
Create a function called echo that prints a string a number of times
The function should take 2 parameters 
    -one for the string, one for the number of times
Example- you, 5 = youyouyouyouyou
'''

def echo(roxy, seven):
    print(str(roxy) * int(seven))

echo("Echo, echo, echo, echo, echo, echo, echo", 7)

'''
Create a function called happy_birthday that takes one parameter name
When the function runs, it should print the happy birthday song for the name
run it once
'''

def happy_birthday(name):
    print(f"happy birthday to you {name}")

happy_birthday("roxy") 
