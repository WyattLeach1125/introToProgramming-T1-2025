import random, os

def start_adventure():
     print(str.title("\nadventure starts here\n"))
     print("You wake up in your bed, dirty and tired as always you lay in your bed, what do you do?")
     print(" 1- what day is it again? (check the calander)\n 2- did i stay up late again? (check the clock)\n 3- if nobody woke me up, must be a weekend! i can sleep again (go back to sleep)")

     choice = input("> ")

     if choice == "1":
          checkCalander()
     elif choice == "2":
          checkClock()
     elif choice == "3":
          ending_sleep()
     else:
          os.system('cls')
          print("invalid expression, try again")
          start_adventure()


def checkCalander(): #1
     print("Its a weekend, thank god!.. but now you are too awake to go back to bed so you get up, what do you do?")
     print(" 1- you see your piano, it'd be fun to give the old thing a spin! (play the piano)")
     print(" 2- you're still in your pj's, probably should get dressed. (put on some clothes you hooligan!)\n 3- screw the other options! I'm going to dance around my room like a maniac! (what are you, an animal?)")

     choice = input("> ")

     if choice == "1":
          piano()
     elif choice == "2":
          dressed()
     elif choice == "3":
          dancingAnimal()
     else:
          os.system('cls')
          print("invalid expression, try again")
          checkCalander()


def piano(): #2
     print("You sit down, getting ready to play something, what do you want to play?")
     print(" 1- something beautiful, to make others feel welcomed during this dull morning (play something beautiful).\n 2- play something boring (who would choose this?)\n 3- screw that other option, PLAY SOMETHING LOUD AND BOLD (be an annoying prick)")

     choice = input("> ")

     if choice == "1":
          beautifulMusic()
     elif choice == "2":
          boringMusic()
     elif choice == "3":
          annoyingPrick()
     else:
          os.system('cls')
          print("invalid expression, try again")
          piano()


def beautifulMusic(): #3
     print("everyone in the building wakes up to an angelic harmony of notes, a few people come up to thank you for the wonderful music!... actually thats more than a few people. You should start running, but to where or how?")
     print(" 1- (hide in the closet)\n 2- see if you can pretend you arent you, most of them probably don't know what you look like. (hide in the crowd)\n 3- open the doors and welcome them in for a fight! (weird but cool, FIGHT!!!)")

     choice = input("> ")

     if choice == "1":
          hideCloset()
     elif choice == "2":
          hideCrowd()
     elif choice == "3":
          fight()
     else:
          os.system('cls')
          print("invalid expression, try again")
          beautifulMusic()


def hideCloset(): #4
     print("wow the silence is... deafening, how long do you want to hide?")
     print("1- I'll wait a few hours, then I'll leave\n 2- I am hidding until they go away!")

     choice = input("> ")

     if choice == "1":
          ending_hoursCloset()
     elif choice == "2":
          ending_theyNeverLeave()
     else:
          os.system('cls')
          print("invalid expresion, try again")
          hideCloset()


def ending_hoursCloset(): #5
     print("--ENDING_HOURS UPON HOURS-- after a few hours you open the closet door, yet they are still there... waiting for you. input anything to restart")
     
     input("> ")

     os.system('cls')
     start_adventure()


def ending_theyNeverLeave(): #5
     print("--ENDING_THEY NEVER LEAVE-- minutes become hours, hours become days, days lead to nothing yet hunger and thirst. input anything to restart")
     
     input("> ")

     os.system('cls')
     start_adventure()


def hideCrowd(): #4
     print("you manage to hide in the crowd, where do you go from here?\n 1- (left)\n 2- (right)")
     
     input("> ")

     ending_hideCrowd()


def ending_hideCrowd(): #5
     print("--ENDING_ONE IN THE CROWD-- it never mattered where you went... you were always hidding among them")
     
     input("> ")

     os.system('cls')
     start_adventure()


def fight(): #4
     print("AWW YEAH BBY, HOW DO YOU WANNA DO THIS?\n 1- WITH MY BARE FISTS (FISTS)\n 2- I am going to try to find a weapon, like a stick or something (find a weapon)\n 3- I THOUGHT THIS WAS GONNA BE AN ENDING! I'll just start throwing stuff (throw random crap)")
     
     choice = input("> ")

     if choice == "1":
          ending_bareKnuckleBeatdown()
     elif choice == "2":
          ending_weapon()
     elif choice == "3":
          ending_whyDoYouHaveSoMuchStuff()
     else:
          os.system('cls')
          print("invalid expresion, try again")
          fight()


def ending_bareKnuckleBeatdown(): #5
     print("--ENDING_BEAT THEM BLOODY-- THE JOY OF BATTLE. input anything to restart")
          
     input("> ")

     os.system('cls')
     start_adventure()


def ending_weapon(): #5
     print("--ENDING_FIGHT SMARTER-- easier to beat them this way! input anything to restart")
          
     input("> ")

     os.system('cls')
     start_adventure()


def ending_whyDoYouHaveSoMuchStuff(): #5
     print("--ENDING_AVALANCHE OF STUFF-- you must've been a massive hoarder, because you never run out of stuff to throw. input anything to restart")
          
     input("> ")

     os.system('cls')
     start_adventure()


def boringMusic(): #3
     print("Your music manages to be so boring that nobody on the entire planet earth can wake up, what do you do?")
     print("1- you're kidding, right? (I am not) Well I guess I'll have more time to uh... sleep (WAIT DON'T SLEEP)\n 2- start scavanging for things that will help you survive (scanvanger)")
          
     choice = input("> ")

     if choice == "1":
          ending_foreverDream()
     elif choice == "2":
          ending_scavange()
     else:
          os.system('cls')
          print("invalid expression, try again")
          boringMusic()


def ending_foreverDream(): #4
     print("--ENDING_FOREVER DREAM-- nobody ever wakes up, but this dream is amazing. input anythint to restart")
     
     input("> ")

     os.system('cls')
     start_adventure()


def ending_scavange(): #4
     print("--ENDING_SCAVANGE-- you live out the rest of your days among bodies of those who will never wake up. input anything to restart")
     
     input("> ")

     os.system('cls')
     start_adventure()


def annoyingPrick(): #3
     print("OW MY YEARS, WOW OKAY. You somehow managed to upset THE ENTIRE BUILDING with how damn LOUD that was, so many people are mad at you... how are you gonna escape this?")
     print(" 1- (apologize for being a dick)\n 2- keep that door locked, nobody can come into my fort! (on the defense)\n 3- OUT THE WINDOW!!!!!! (what!? youre kidding... right?)")

     choice = input("> ")

     if choice == "1":
          apologize()
     elif choice == "2":
          ending_defense()
     elif choice == "3":
          ending_OUT_THE_WINDOW()
     else:
          os.system('cls')
          print("invalid expression, try again")
          annoyingPrick()


def apologize(): #4
     print("now what do you say?\n 1- *sigh* I say sorry (good)\n 2- I WAS SCREWING WITH YOU, I NEVER APOLOGIZE!!! (you're a dick)")
     
     choice = input("> ")

     if choice == "1":
          ending_sorry()
     elif choice == "2":
          ending_dick()
     else:
          os.system('cls')
          print("inalid expression, try again")
          apologize()


def ending_sorry(): #5
     print("--ENDING_WELL THAT WAS RUDE!-- when they finally reach you they, reasonably, do not accept your apology; however, they, unreasonably, start eating you alive... they were zombies, aparentally. input anything to restart")
          
     input("> ")

     os.system('cls')
     start_adventure()     


def ending_dick(): #5
     print("--ENDING_DICK-- you keep your door locked and closed, you will never apologize. input anything to restart")
          
     input("> ")

     os.system('cls')
     start_adventure()


def ending_defense(): #4
     print("--ENDING_IMPENETRABLE FORT-- nobody is getting past this! input anything to restart")
          
     input("> ")

     os.system('cls')
     start_adventure()


def ending_OUT_THE_WINDOW(): #4
     print("--ENDING_YOU ARE SO DUMB-- you jump out the window and fall to your death, idiot. input anything to restart")
     
     input("> ")
     
     os.system('cls')
     start_adventure()     


def dressed(): #2
     print(" Well, lets see what you can put on.\n 1- (dress)\n 2- (suit)\n 3- TEAR THEM ALL OFF!!! (naked)")

     choice = input("> ")

     if choice == "1":
          dress()
     elif choice == "2":
          suit()
     elif choice == "3":
          ending_naked()
     else:
          os.system('cls')
          print("invalid expression, try again")
          dressed()


def dress(): #3
     print("lookin' pretty! how do you wanna show off?")
     print(" 1- don't have to show off to anybody, I'm happy just feeling pretty! (thats nice :3)\n 2- just gonna walk around, feeling pretty in public! (thats also nice :3)")

     choice = input("> ")

     if choice == "1":
          ending_prettyInside()
     elif choice == "2":
          ending_prettyOutside()
     else:
          os.system('cls')
          print("invalid expression, try again")
          dressed()


def ending_prettyInside(): #3
     print("--ENDING_DON'T HAVE TO PROVE I AM PRETTY, I KNOW IM PRETTY-- you love yourself! input anything to restart")
     
     input("> ")

     os.system('cls')
     start_adventure()


def ending_prettyOutside(): #3
     print("--ENDING_STRUT YA STUFF!-- you look pretty, girl! input anything to restart")
     
     input("> ")

     os.system('cls')
     start_adventure()


def suit(): #3
     print("lookin' spiffy! how do you wanna show off?")
     print(" 1- don't have to prove I look awesome, I am always awesome! (thats nice :])\n 2- just gonna walk around, feeling awesome in public! (thats also nice :])")

     choice = input("> ")

     if choice == "1":
          ending_spiffyInside()
     elif choice == "2":
          ending_spiffyOutside()
     else:
          os.system('cls')
          print("invalid expression, try again")
          dressed()


def ending_spiffyInside(): #4
     print("--ENDING_SPIFFY INSIDE-- very spiffy! so spiffy! input anything to restart")
     
     input("> ")

     os.system('cls')
     start_adventure()


def ending_spiffyOutside(): #4
     print("--ENDING_MAN IN BLACK-- yes that is a movie reference. input anything to restart")
     
     input("> ")

     os.system('cls')
     start_adventure()


def ending_naked(): #3
     print("--ENDING_NAKED-- you are not going out naked! input anything to restart.")
     
     input("> ")

     os.system('cls')
     start_adventure()


def dancingAnimal(): #2
     print("okay so you dance around like a maniac, you really have no self control... but seriously, what do you do?")
     print("1- Okay, I'll do something else. (return to previous choice)\n 2- JUMP ON MY BED AND BLEAT LIKE A GOAT!!! (what? no you are not!)")
          
     choice = input("> ")

     if choice == "1":
          start_adventure()
     elif choice == "2":
          goat()
     else:
          os.system('cls')
          print("invalid expression, try again")
          dancingAnimal()


def goat(): #3
     print("as you jump on your bed, you realize that it isn't anywhere above the floor, actually... the walls look padded.\n 1- where am I?\n 2- (YOU DON'T GET ANOTHER CHOICE)")

     choice = input("> ")

     if choice == "1":
          ending_insanity()
     else:
          os.system('cls')
          print("try again, dumbass")
          goat()


def ending_insanity(): #4
     print("you find yourself in a jacket that has belts all over, unable to move your arms from your sides. You are in an insane asylum.\n--ENDING_INSANITY-- next time, dont be a prick. input something to restart, dumbass.")

     input("> ")

     os.system('cls')
     start_adventure()


def checkClock(): #1
     time = random.randint(7,11)
     if time < 10:
          print(f"oh good, its still before 10, guess you have lots of time to get stuff done!")
          print(f" 1- since I'm not in the mood to play piano, I could start drawing (draw)\n 2- I could play some video games, that could be fun! (GAMER)\n 3- CAUSE TERROR, GO AROUND YELLING AND SCREAMING YOUR LUNGS OUT!!! (what?)")
          
          choice = input("> ")

          if choice == "1":
               draw()
          elif choice == "2":
               gamer()
          elif choice == "3":
               terror()
          else:
               os.system('cls')
               print("invalid expression, try again")
     else:
          print(f"oh god its {time}, i better get a move on!")
          ending_lateClock()


def draw(): #2
     print("hmmmm... what should I draw?\n 1- furries (cool)\n 2- MYSELF, I AM AWESOME!!! (that you are)")
          
     choice = input("> ")

     if choice == "1":
          ending_furry()
     elif choice == "2":
          ending_myself()
     else:
          os.system('cls')
          print("invalid expression, try again")
          draw()


def ending_furry(): #3
     print("--ENDING_FURRIES-- nothing else to say, I guess it's cool. input anything to restart")
     
     input("> ")

     os.system('cls')
     start_adventure()


def ending_myself(): #3
     print("--ENDING_I AM AWESOME-- congrats, you love yourself! input anything to restart")
     
     input("> ")

     os.system('cls')
     start_adventure()


def gamer(): #2
     print("what should I play?\n 1- Empty Paladin: Satin Melody\n 2- DIGMAKE\n 3- Deceased Bolt\n 4- are all these legally distinct versions of other games?")

     choice = input("> ")

     if choice == "1":
          ending_EmptyPaladin()
     elif choice == "2":
          ending_DIGMAKE()
     elif choice == "3":
          ending_DeceasedBolt()
     elif choice == "4":
          ending_yeah()
     else:
          os.system('cls')
          print("invalid expression, try again")
          gamer()


def ending_EmptyPaladin(): #3
     print("--ENDING_EMPTY PALADIN: SATIN MELODY-- this game is so gosh darn hard! input anything to restart")
     
     input("> ")

     os.system('cls')
     start_adventure()


def ending_DIGMAKE(): #3
     print("--ENDING_DIGMAKE-- I will get executed for this, but this game isn't that good. input anything to restart")
     
     input("> ")

     os.system('cls')
     start_adventure()


def ending_DeceasedBolt(): #3
     print("--ENDING_DECEASEDBOLT-- this game is so toxic, omg. input anything to restart")
          
     input("> ")

     os.system('cls')
     start_adventure()


def ending_yeah(): #3
     print("--ENDING_YEAH-- yeah. input anything to yeah")
          
     input("> ")

     os.system('cls')
     print("yeah")
     start_adventure()


def terror(): #2
     print("if you're going to be causing terror, you can at least do it in more interesting ways.\n 1- stalk the living (boogyman)\n 2- BECOME A WIZARD THAT STRIKES ANYONE DOWN WHO DARES OPPOSE YOU (YOU ARE GREAT AND MIGHTY)")
     
     choice = input("> ")

     if choice == "1":
          ending_boogyman()
     elif choice == "2":
          ending_wizard()
     else:
          os.system('cls')
          print("invalid expression, try again")
          terror()


def ending_boogyman(): #3
     print("--ENDING_BOOGYMAN-- BOO, HAHAHHA. input anything to restart")
     
     input("> ")

     os.system('cls')
     start_adventure()


def ending_wizard(): #3
     print("--ENDING_WIZARD-- I AM GREAT AND MIGHTY!!! input anything to restart")
          
     input("> ")

     os.system('cls')
     start_adventure()


def ending_lateClock(): #2
     print("--ENDING_YOU'RE LATE-- input anything to restart")
     
     input("> ")

     os.system('cls')
     start_adventure()


def ending_sleep(): #1
     print("---ENDING_SLEEP---\n Well you go back to sleep, ya lazy bum. input anything to restart")
     
     input("> ")

     os.system('cls')
     start_adventure()


start_adventure()