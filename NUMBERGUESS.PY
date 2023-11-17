import random
import math
print("HELLO!! WELCOME TO THE NUMBER GUESSING GAME.\n YOU HAVE GOT 7 CHANCES TO GUESS THE NUMBER. \n LET'S BEGINNN!!")

upper = int(input("ENTER THE LOWER BOUND NUMBER:-"))
lower = int(input("ENTER THE UPPER BOUND NUMBER:-"))
r = random.randint(upper,lower)

print("\n\tYou've only 7 chances to guess the integer!\n")

chance = 7
count = 0

while count < chance:
        count+=1
        guess = int(input("GUESS A NUMBER:-"))
        if r==guess:
                print("CONGRATULATIONS!! YOU DID IT IN",count,"TRY")
                break
        elif r > guess:
                print("THE NUMBER IS TOO SMALL :[")
        elif r < guess:
                print("THE NUMBER IS TOO HIGH :[")  
if count >= chance:
        print("\n THE NUMBER IS %d" %r)  
        print("\t BETTER LUCK NEXT TIME!!")                