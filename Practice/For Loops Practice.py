#1
'''for i in range(10, 1, -1):
    print(i)


#2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0
for num in numbers:
    total += num
print(total)
    #or?
for num in numbers:
    total = total + num
print(total)


#3 kinda wrong?
num1to5 = [1, 2, 3, 4, 5]
for num in num1to5:
    print(num*num)

#4
stringvowels = input("Enter a word:\n>")
numvowels = 0
for character in stringvowels:
    if character in ["a", "e", "i", "o", "u"]:
        numvowels += 1
print(numvowels)

#5
usernum = input("Enter an integer:\n>")
try:
    usernum = int(usernum)
except:
    print("Not an interger...")
for i in range(1, 11):
    print(f"{str(usernum)} x {str(i)} = {str(usernum*i)}")

#6
names = ["Ashley", "Roxy", "Mally"]
for name in names:
    print(f"Hello, {name}!")'''