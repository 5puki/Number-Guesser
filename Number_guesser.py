import random

print("Create a range of numbers then try to guess the random number selected in that range.")

max_num = input("Set the range: ")

if max_num.isdigit():
    max_num = int(max_num)

    if max_num <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

random_num = random.randint(0, max_num)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    if user_guess == random_num:
        print("You got it!")
        break
    elif user_guess > random_num:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in", guesses, "guesses!")