# Import necessary modules
import random
import time


# Pick a number between 1 and 100
number=random.randint(1,100)

def intro():
    print("May i ask for your name?")
    # Declaring name variable global so it can be accessed outside the function
    global Name
    Name = input() #Asks for name
    print(Name + ", we are going to play a game. I am thinking of a number between 1 and 100")
    if(number%2==0):
        x='even'
    else:
        x='odd' 
    print("\nThis is an {}number".format(x)) 
    time.sleep(.5)
    print("Go ahead. Guess!")

def pick():    
    guessesTaken = 0


    #If the number of guesses is less than 6
    while guessesTaken <6:
        time.sleep(.25)
        # Inserts the place to get a number
        enter=input("Guess: ")


        #Check if a number was entered
        try:

            #Stores the guess as an integer instead of a string
            guess = int(enter)

            if guess<=100 and guess>=1: # If they are in range 
                guessesTaken=guessesTaken+1 #Adds one guess each time the player is wrong
                if guessesTaken<6:
                    if guess<number:
                        print("The guess of the number that you have entered is too low")
                    if guess>number:
                        print("The guess of the number that you have entered is too high")
                    if guess != number:
                        time.sleep(.5)
                        print("Try Again!")
                    if guess==number:
                        break
                if guess>100 or guess<1:
                    print("Silly goose! That  number isnt in the range!")
                    time.sleep(.25)
                    print("Please enter a nujmber between 1 and 100")
        except: 
            print("I dont think that "+enter+"is a number. Sorry")        
    if guess == number:
        guessesTaken = str(guessesTaken) 
        print('Good job, {} You guessed my number in {} guesses!'.format(Name, guessesTaken))

    if guess != number:
        print('Nope. The number i was thinking of was ' + str(number)) 

playagain="yes" 
while playagain=="yes" or playagain=="y" or playagain=="Y":
    intro()
    pick()
    print("Do you wnat to play again?")
    playagain=input()