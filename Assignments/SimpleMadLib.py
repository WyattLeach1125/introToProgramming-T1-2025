#woah :O
import os

os.system ('cls')
# Once upon a time, in a [adjective] [noun],
# there lived a [adjective] [noun].
# Every day, the [noun] would [verb] [adverb].
# One day, a [adjective] [noun] appeared
# and [verb] the [noun] away.
# The [noun] was [adjective] and [emotion].

'''

-make the user input an adj
-make the user input a noun
-make the user input another adj
-make the user input another noun
-make the user input a verb
-make the user input an adverb
-make the user input another adj
-make the user input another noun
-make the user input another verb
-make the user input another adj
-make the user input an emotion

-print all that into the madlib format

'''
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

