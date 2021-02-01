import random
randomNo=random.randint(1,9)
chances=0

while(chances<5):
    guess=int(input("Enter your guess"))
    if(guess<randomNo and chances<4):
        print("Guess a number more than "+str(guess)) 
    elif(guess>randomNo and chances<4):
        print("Guess a number less than "+str(guess))
    elif(guess==randomNo):
        print("Congratulation!! You Won")
        break
    chances=chances+1
if(guess!=randomNo):
    print("You Lose!! The number was "+str(randomNo))

     
