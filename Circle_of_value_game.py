#Nicholas Novak
#Text-based Wheel of Fortune Game


from IPython.display import clear_output
import random
letters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"


# # Python Code Sample: "Wheel of Fortune" Game
# 
# ### This assignment is from my Python Coursework and is an implementation of a popular TV show game.  Our game was called Circle of Value.
# 
# ### The phrases are generted from a co-located text file called "wheeloffortune.txt"
# 
# ### The game will perform like this:
# 
# ### Prompt the user for their name, save it as a string
# 
# ### The user starts off with 0 dollars at the beginning of the game, and their bankroll is updated as they either win money by correctly guessing, or pay 50 dollars to guess a vowel. The phrases are chosen at random.

# ### I used three spaces between words in order to make the blank phrases more readable. Furthermore, I am using spaces between the letters to better denote the number of letters in a word, and tabs to space out the words during the puzzle display.
# 
# ### Also, a string of the letters that have been guessed was created so the user will not guess the same letters.
# 
# ### The game is played until either the user guesses the phrase (by solving the puzzle or having guessed all the letters) or they decide to quit or fail at solving the puzzle (they only get one shot).  All user guesses are treated as uppercase regardless of what letter is entered in.  Vowels include AEIOU; Y is considered not a vowel for this program.  If the user guesses a letter in the word, they win the amount the wheel lands on times the number of letters that were in the phrase.  Vowels merely cost 100 dollars regardless of how many are in the word.  
# 
# 




## First, this opens the file and randomly select a line as our phrase for the game
## Than, the file is closed and the randomly selected line is returned
def get_phrase():
    wheel_file = open("wheeloffortune.txt","r")    #Find and open list of phrases
    
    wheelall = wheel_file.readlines()
    random.shuffle(wheelall)    #Assign random line numbers
    
    wheelline = wheelall[0].rstrip() #Find a random line
    
    count = wheelline.index(":")
    
    global phrase #Set phrase as a global variable
    phrase = ""
    for p in wheelline[count+1::]:  #Separate phrase from clue
        
        # Add spaces to phrase:
        phrase += " "
        phrase += p
        phrase += " "
        
    
    global clue  #Set clue as a gloabl variable
    
    clue = wheelline[:count:]
    #Grab clue text
    
    wheel_file.close() #Close the file
    return #End the function

## Steps to take:
## Get the randomly selected phrase
## Ask user for their name
## Loop until a lose condition occurs or until the puzzle is solved
## Spin the wheel and get the result
## Update the bankroll when either a letter has been guessed and is present in puzzle or vowel purchased
## If you go bankrupt, bankroll should go to zero and turn ends, begin next turn
## If logging is True, do not clear the screen otherwise by default it will clear the screen between turns





def play_game(logging=False):
    get_phrase() #Run the get phrase function
    
    user_name = input("What is your name?") #Determine name
    
    game = True #Break variable for while loop later used in game
    
    puzzle = "" #Assign variable for puzzle
    
    
    for i in phrase:
        if i in letters: #Create blank puzzle out of underscore characters
            puzzle += "_"
            
            
        else: #Insert spaces around any character not a letter.
            puzzle += ""
            puzzle += i
            puzzle += ""
            
        bankroll = 0 #Starting money
        
    letters_guessed = "" #Assign variable for guessed letters
    
    while game == True: #Dangerous loop! (Hence break variable built into all outcomes)
            
        print(user_name,"your current puzzle progress is",puzzle,"and you have guessed",letters_guessed,".")
        quit = input("Would you like to quit? Enter Y or N.\n")
        if quit in "Yy": #Check for quit
            print("Thanks for playing,",user_name,"! The phrase was: ",phrase)
            game == False
            return
        
        
        else:
            
            print("Here are the letters you have guessed so far,",user_name,":",letters_guessed,"\n") #Show guessed letters
            
            print("You have",bankroll,"dollars in your bankroll","\n")  #Show money accumulated
           
            print("Your clue is:",clue,"\n") #Show clue
            
            print("Current Progress:",puzzle,"\n") #Show puzzle progress
            
            print("Spinnging wheel.........now.\n") #Fun addition (serves no function except for the illusion of the program chugging/the wheel spinning in the background)
            
            spin_wheel() #Call spin wheel function
            
            print("Landed on $",lander) #Give landed value
            
            if lander == "BANKRUPT":

                print("Uh-oh! (Insert slide whistle) You got ",lander,"! Spin again and see if you can earn all that ",bankroll," dollars back!\n")
                bankroll == 0 #Exception for bankrupcy result (log not cleared for this)

                
            else:

                solver = input("Would you like to solve the puzzle? If not hit enter, otherwise type in your guess. WARNING: IF YOU SOLVE INCORRECTLY, THE GAME WILL BE OVER\n")
                solver = solver.upper() #Check if user wants to solve
                


                if solver == "": #If the user does not want to solve, continue
                    
                    
                    print("What letter would you like to guess? Keep in mind you have to buy vowels (y not included).\n")
                    guesser = input("Please type your guess here\n")
                    guesser = guesser.upper() #Interpret input guess into uppercase
                    
                    
                    if guesser in "aeiouAEIOU":  #Vowel result
                        bankroll += 0
                        print("This roll of",bankroll,"is forfeited to buy the vowel")
                       

                        if guesser in phrase: 
                            puzzle2 = ""
                            count1 = -1 #Assign temp variables for this loop
                            
                            
                            for i in phrase:
                                count1 += 1
                                if i == guesser: # If the letter matches the guessed letter
                                    puzzle2 += i
                                else:
                                    puzzle2 += puzzle[count1] #Add guess to puzzle
                                
                            letters_guessed += guesser
                            puzzle = puzzle2

                        elif guesser not in phrase: #Result if incorrect guess
                            print("Nooooo! That letter was not in the phrase!")
                            letters_guessed += guesser
                            
                            
                        
                            
                    elif guesser in "qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM" and guesser not in letters_guessed: #Consonant results tree
                        
                        if guesser in phrase:
                            puzzle2 = ""
                            count2 = -1
                            bankroll += lander 
                            for i in phrase: #Result if guess is in the phrase
                                count2 += 1
                  
                                if i == guesser:
                                    puzzle2 += i
                  
                                else: #Add letter to puzzle
                                    puzzle2 += puzzle[count2]
                            letters_guessed += guesser
                            puzzle = puzzle2
                            


                        elif guesser not in phrase: #Result if incorrect guess
                            print("Nooooo! That letter was not in the phrase!")
                            letters_guessed += guesser
                            


                    elif guesser in "qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM" and guesser in letters_guessed: #Check to see if letter has been guessed already
                        print("You already guessed that letter! Spin again!")
                        
                        
                    else: #Check if guess is not in alphabet
                        print("Please guess a letter!")
                        

                elif solver == phrase: #Check if puzzle solved
                    
                    if lander != "BANKRUPT": #Add final value
                        bankroll += int(lander)
                        
                        
                    print("Congratulations ",user_name," you won",bankroll,"dollars! Go ahead and spend them all in one place.")        
                    game == False #End game, game is won
                    
                    
                    print("The phrase was",phrase) #Show the phrase
                    
                    return

                else: #Incorrect puzzle solution guess
                    
                    print("The phrase was,",phrase,"and you guessed",solver,":(. Better luck next time!")
                    game == False #End game, game is lost
                    
                    
                    return
                if puzzle == phrase: #Result if user wins through raw smarts and guessing power

                    game == False

                    print("Congratulations",user_name,"you won",bankroll,"dollars! Go ahead and spend them all in one place.")
                    print("The phrase was",phrase) #Show the phrase
                    
                    return
                if logging == False:
                    clear_output() #Clear output between runs if logging is set to "True"
        
    pass




##Return a random element of this list whenever spin_wheel() is called
def spin_wheel(): #Randomized called value function
    wheel = [300,500,1000,1500,400,"BANKRUPT",2250,2500,200,100] #Wheel values
    
    wheel_val = random.randint(0,9) #Random value generated
    
    global lander #Create lander as a global variable for use in the game function
    lander = wheel[wheel_val] #Grab spin result
    
    return #End function without an output, since lander can be called at anytime in the game loop


play_game(logging = False) #Run the game without logging previous turns
