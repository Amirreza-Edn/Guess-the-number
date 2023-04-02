import random
import time

# Generate a random number between 0 and 100
number = random.randint(0, 100)
# initialize recording the number of attempts
attempts = 0
guess = input("Guess the number between 0 and 100: ")
start_time = time.time()

# indicates if the program is still running or should be stopped
game_running = True

# check if the user's guess is a valid integer
if guess.isdigit():
    attempts += 1
    if int(guess) > number:
        print("the number is lower.")
    elif int(guess) < number:
        print("the number is higher.")
    else:
        print("Wow! you got superpowers! you guessed the number in the first try!")
        game_running = False  # end the game if the user guessed right
else:
    print("please enter a number!")

# Loop until the user guesses the correct number or quits the game
while True:
    guess = input("try again or stop the game by pressing 'q': ")
    # check if the user wants to quit
    if guess == 'q':
        print("Quitting the game...")
        end_time = time.time()
        # calculate and print the time spent 
        elapsed_time = end_time - start_time
        print("time spent:", elapsed_time, "seconds")
        break
    if guess.isdigit():
        attempts += 1
        if int(guess) > number:
            print("The number is lower.")
        elif int(guess) < number:
            print("The number is higher.")
        else:
            print("Congratulations! You guessed the number in", attempts, "attempts.")
            end_time = time.time()
            elapsed_time = end_time - start_time
            print("your record was:", elapsed_time, "seconds")
            break
    else:
        print("please enter a number!")
