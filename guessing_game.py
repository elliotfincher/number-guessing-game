"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random



def start_game():
    
    #Assign variables that will be referenced later
    highscore=10000000000  
    
    #Welcome message
    print("Welcome to the Elliot's number guessing game!")
       
    while True:
    
      randnum=random.randint(1,10)
      number_of_attempts=1
      
      player_guess=input("Please guess a number: ")
      
      while True:
        try:
          player_guess=int(player_guess)
        except ValueError as err:
          print("Please ensure you enter a number between 1 and 10")
          number_of_attempts += 1
          player_guess=input("Please guess a number: ")
          continue
        if (player_guess <=0) or (player_guess >10):
          print("Please ensure you enter a number between 1 and 10")
          number_of_attempts += 1
          player_guess=input("Please guess a number: ")
        else:
          break
      
      while (player_guess != randnum):
        if (player_guess > randnum):
          print("It's lower")
          player_guess=input("Please guess a number: ")
          player_guess=int(player_guess)
          number_of_attempts += 1
        else:
          print("It's higher")
          player_guess=input("Please guess a number: ")
          player_guess=int(player_guess)
          number_of_attempts +=1
      else:
        print("You got it!")
        print("You took {} attempts".format(number_of_attempts))
        if(number_of_attempts < highscore):
          highscore = number_of_attempts
        
        
        playagain=input("Would you like to play again? (y/n) ")    
        #ensure no value other than "y" and "n" can be entered
        
        while (playagain.lower() != "y") and (playagain.lower() != "n"):
          playagain=input("Please choose either 'y' or 'n': ")
        else:
          if(playagain.lower() == "n"):
            print("Thank you for playing the number guessing game :)")
            break
          else:
            print("The highscore is {} attempts".format(highscore))
            continue
          

# Kick off the program by calling the start_game function.
start_game()
