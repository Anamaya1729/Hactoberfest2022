# Number guessing game

import random
winningNumber=random.randint(1,20)
num=int(input("Game is started \nGuess the number "))
gameover=False
guess=0

while not gameover:
    if winningNumber==num:
        print("you win")
        print(f"total guesses are {guess}")
        gameover=True
    else:
       if num<winningNumber:
          print("too low")
          
       else :
          print("too high") 
       guess+=1 
       num=int(input("Guess the number again "))
