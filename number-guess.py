import random

Y = int(input("Guess a number between 1 and 100: "))
X = random.randint(1,100)

while True:
    if Y != X:
        if Y > X:
         print("Your guess is high")
        else:
           print("Your guess is low")

        Y = int(input("Guess a number between 1 and 10: "))

    else:
        print("Correct!!!")
        break
    

