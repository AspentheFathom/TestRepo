import random 


#generate a random number between 1 and 100 
randum = random.randint(1,101)

count = 0
guess = -99

while (guess != randum):
    # Get the user's guess
    guess = (int)(input("Enter your guess between 1 and 100: "))
    if guess < randum:
            print("higher")
    elif guess > randum:
            print("lower")
    else:
            print("you guessed it!")
            break 
    count = count + 1
#end of while loop

print("you took " + str(count) + " steps to guess the number")
