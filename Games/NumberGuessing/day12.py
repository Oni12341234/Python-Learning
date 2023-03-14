import random
print("Welcome to the Number Guessing Game!")
print("I\'m thinking of a number between 1 and 100")
choice=input("Choose a difficulty. Type 'easy' or 'hard'")

def easy():
    HasWon=0
    guesses=10
    random_number=random.randint(0,101)
    print (f"Hey, the number is {random_number}")
    while guesses>0 and HasWon!=1:
        print (f"You have {guesses} attempts to guess the number.")
        choice=input("Make a guess: ")
        if int(choice)>random_number:
             print("Too high")
             print("Guess again.")
        elif int(choice)<random_number:
             print ("Too low")
             print ("Guess again.")
        else:
             print (f"You got it! The answer was {random_number}")
             HasWon=1
        guesses-=1
        if guesses==0 and HasWon==0:
                 print (f"You've lost! The answer was {random_number}")
                 return 0
    
def hard():
    HasWon=0
    guesses=5
    random_number=random.randint(0,101)
    print (f"Hey, the number is {random_number}")
    while guesses>0 and HasWon!=1:
        print (f"You have {guesses} attempts to guess the number.")
        choice=input("Make a guess: ")
        if int(choice)>random_number:
             print("Too high")
             print("Guess again.")
        elif int(choice)<random_number:
             print ("Too low")
             print ("Guess again.")
        else:
             print (f"You got it! The answer was {random_number}")
             HasWon=1
        guesses-=1
    if guesses==0 and HasWon==0:
        print ("You've lost")
        return 0



if choice=="easy":
    easy()
elif choice=="hard":
    hard()
else:
    print("Type only 'easy' or 'hard'")