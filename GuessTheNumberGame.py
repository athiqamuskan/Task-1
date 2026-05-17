import random
secret_num = random.randint(1, 100)
count = 0
print("🎯 Guess the hidden number between 1 and 100!")
while True:
    user_input = int(input("Enter your guess: "))
    count += 1
    if user_input > secret_num:
        print("Too high, try again!")
    elif user_input < secret_num:
        print("Too low, try again!")
    else:
        print("Well done! You guessed it right.")
        print("Attempts taken:", count)
        break
