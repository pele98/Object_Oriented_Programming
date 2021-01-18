# File name: Exercise1_8
# Author: Pekka Lehtola
# Description: Game of rock-paper-scissors against a bot. Best of 3 wins

import random

user_score = 0
bot_score = 0

#Main function
def rps(user):

    global user_score, bot_score

    #Chooses random choice for bot
    choices = ["rock", "paper", "scissors"]
    bot_choice = random.choice(choices)

    #Used for checking if there is a winner, if not game continues normally.
    def winner():

        global user_score, bot_score

        # Prints out current score
        print("score is : User", user_score, "Bot", bot_score, end="\n\n")

        #if bot wins and restarts the game
        if bot_score == 2:
            print("BOT WINS", end="\n\n")
            print("NEW GAME", end="\n\n")
            user_score, bot_score = 0, 0
            rps(input("Choose one *rock, paper, scissors* : "))

        #if user wins and restarts the game
        if user_score == 2:
            print("USER WINS", end="\n\n")
            print("NEW GAME", end="\n\n")
            user_score, bot_score = 0, 0
            rps(input("Choose one *rock, paper, scissors* : "))

        else:
            rps(input("Choose one *rock, paper, scissors* : "))

    #if user choose something else than rock paper or scissors.
    if user not in choices:
        print("Please choose one from the list", end="\n")
        rps(input("*rock, paper, scissors* : "))

    #Main logic behind the game. Check users choice against bot and dermites who wins.
    elif user == "rock":

        if user == bot_choice:
            print("TIE", end="\n")
            winner()

        elif bot_choice == "paper":
            print("POINT FOR BOT", end="\n")
            bot_score += 1
            winner()

        else:
            print("POINT FOR USER", end="\n")
            user_score += 1
            winner()

    if user == "paper":

        if user == bot_choice:
            print("TIE", end="\n")
            winner()

        elif bot_choice == "scissors":
            print("POINT FOR BOT", end="\n")
            bot_score += 1
            winner()

        else:
            print("POINT FOR USER", end="\n")
            user_score += 1
            winner()

    else:

        if user == bot_choice:
            print("TIE", end="\n")
            winner()

        elif bot_choice == "rock":
            print("POINT FOR BOT", end="\n")
            bot_score += 1
            winner()

        else:
            print("POINT FOR USER", end="\n")
            user_score += 1
            winner()

#User input
rps(input("Choose one *rock, paper, scissors* :"))