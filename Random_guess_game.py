import random

guess_num = int(input("Enter your guessing number :"))

random_guess = random.choice(range(1, 11))
#put your number range inside the range here
#remember, end number must be +1 ( if end number is 10, put 11 there)

if guess_num == random_guess:
    print("Hurray !")
else:
    print("Not Matched,", end=" ")
    print("Correct number:", random_guess)
