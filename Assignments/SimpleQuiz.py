score = int(0)

print("\nall answers must be in lowercase and with no special symbols\n")
question1 = str(input("What show do I love that alfabusa makes?\n>"))
question2 = str(input("What is my favorite color?\n>"))
question3 = str(input("What year did TF2 release?\n>"))
question4 = str(input("What color is hornet from hollow knight's cloak?\n>"))
question5 = str(input("What is my favorite webcomic?\n>"))


def tally_score():
    global score
    if question1 == "hunter the parenting":
        score += 1
    if question2 == "pink":
        score += 1
    if question3 == "2007":
        score += 1
    if question4 == "red":
        score += 1
    if question5 == "homestuck":
        score += 1

tally_score()
print("the score is: ", score, "\n")