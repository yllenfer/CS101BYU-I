import random
guessNum = 0
num = random.randint(1,75)

print("Enter an integer from 1 to 75")

while guessNum < 6:
   print("Try to guess: ")
   guess = input()
   guess = int(guess)
   guessNum+= 1

   if guess < num:
    print(f"That number is too low, you have {guessNum - (6)} attempts left")
   elif guess > num:
    print(f"That number is too high, you have {guessNum - (6)} attempts left")
   elif guess == num:
    print(f"That's the right one, you guessed the number"
          f" in {guessNum} attempts. You have won!")
    break
