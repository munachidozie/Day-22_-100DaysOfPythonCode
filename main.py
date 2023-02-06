import random

print ("== Welcome To One-Million-to-One !!!! ==")
print()
print ("The game is simple. There is a programmed number between 1 and 1,000,000 and you have to guess what it is. The goal is to do so in the least number of tries. That's it!!!!")
print ()

counter = 1
number = random.randint(1, 1000000)
while True:
  guess =  int(input("Pick a number between 1 and 1,000,000  "))
  if guess == number:
    print ("You got it. You're a really winner")
    break
  elif guess <= 0 or guess >= 1000000:
    print ("That's just wrong. I guess now we'll never know.")
    exit()
  elif guess <= number:
    print ("Way too low. Go higher")
    counter += 1
    continue
  elif guess >= number:
    print ("Too high. Go lower")
    counter += 1
    continue
  else:
    print ("Come on. That's not even a number.")
print ("It took you", counter, "attempt(s) to get the correct answer.")