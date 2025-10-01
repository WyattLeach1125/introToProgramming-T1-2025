
# V this is global stuff V
import os
taxrate = 0.06875

# A func
def calculate_tax(item, price, rate):
    print(f"The {item} has the tax of {price*rate}")
calculate_tax("apple", 2, taxrate)


# A func that is a func of the SimpleMadLib we did
def SimpleMadLib():
    timeAdj = input("Once upon a time, in a...\nadjective: ")
    timeNoun = input(f"Once upon a time, in a {timeAdj}...\nnoun: ")
    livedAdj= input("there lived a...\nadjective: ")
    livedNoun = input(f"there lived a {livedAdj}\nnoun: ")
    everyVerb = input(f"Every day, the {livedNoun} would...\nverb: ")
    everyAdverb = input(f"Every day, the {livedNoun} would {everyVerb}...\nadverb: ")
    oneAdj = input("One day, a...\nadjective: ")
    oneNoun = input(f"One day, a {oneAdj}...\nnoun: ")
    andVerb = input("and...\nverb: ")
    # print(f"and {andVerb} the {livedNoun}")
    theAdj = input(f"The {timeNoun} was...\nadjective: ")
    theEmotion = input(f"The {timeNoun} was {theAdj} and...\nemotion: ")

    os.system('cls')

    print(f"Once upon a time, in a {timeAdj} {timeNoun}\nthere lived a {livedAdj} {livedNoun}.")
    print(f"Every day, the {timeAdj} {timeNoun}\nthere lived a {livedAdj} {livedNoun}\nEvery day, the {livedNoun} would {everyVerb} {everyAdverb}")
    print(f"One day, a {oneAdj} {oneNoun} appeared\nand {andVerb} the {livedNoun} away\nThe {timeNoun} was {theAdj} and {theEmotion}\n")

SimpleMadLib
