'''
#1
word1 = input("give a random word: ")
word2 = input("give another random word: ")
word3 = input("give one more random word: ")
print(word1, word2, word3)
'''
#2
int1 = int(input("\ngive a random integer: "))
int2 = int(input("give another integer: "))
int3 = int(input("give one more integer: "))
def add_three(x, y, z):
    print(x + y + z)

add_three(int1, int2, int3)

#3
def data_three():
    word4 = input("\ngive a random word: ")
    int4 = float(input("give a random integer: "))
    float1 = float(input("give a random float: "))
    print(word4, int4 + float1)

data_three()
