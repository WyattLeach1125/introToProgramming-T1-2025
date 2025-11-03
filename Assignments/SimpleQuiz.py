score = int(0)

question1 = str(input("What show do I love that alfabusa makes?\n>"))
question2 = str(input("What is my favorite color?\n>"))
question3 = str(input("What year did TF2 release?\n>"))
question4 = str(input("What color is hornet from hollow knight's cloak?\n>"))
question5 = str(input("What is my favorite webcomic?\n>"))


def tally_score():
    global score
    if question1.lower() == "hunter the parenting": score += 1
    if question2.lower() == "pink": score += 1
    if question3.lower() == "2007": score += 1
    if question4.lower() == "red": score += 1
    if question5.lower() == "homestuck": score += 1

tally_score()
print("\nthe score is: ", score, "\n")
