import random
number=random.randint(1,9)
chances = 0
while chances < 5:
    question=int(input("Gues a number between 1 and 9"))
    if question == number:
        print("Congratulations You Won!!")
        break
    elif question>number:
        print("Your guess is high, guess a lower number")
    else:
        print("Your guess is too low, guess a higher number")
    chances+=1
if not chances <5:
      print("You Lose!! The number is", number)








