# File: Game 1 - 100 Game
# Purpose:Two players start from 0 and alternatively add a number from 1 to 10 to the sum. The player who reaches 100 wins.
# Author: Mohamed Akram Abbas
# ID: 20230322


steps = [1,2,3,4,5,6,7,8,9,10]          # A list of all the possible moves the player can do.
print("*** 100 Game ***")               # Welcoming Message.
print("Choose A NUMBER FROM 1~10")
sum = int(0)                              # Intializing the incrementing variable.

while sum < 100:                           # As long as the sum of the two players' moves is still less than 100 --> Keep prompting.
    plyr1 = int(input("Player 1:"))
    while plyr1  not in steps:              # Prompting till the Player enters a valid number from the list.
        plyr1 = int(input("Player 1 Please enter a valid number:"))
    sum += plyr1
    print("The number is now ", sum)            # Prompting the Total sum of the players' moves.
    if sum == 100:
        print("Player 1 Wins")                  # if the first player got to 100 first Print "Player 1 wins".
        exit()                                  # Terminate the Application...
    elif sum > 100:
        print("Player 2 Wins")
        exit()

    plyr2 = int(input("Player 2:"))
    while plyr2 not in steps:
        plyr2 = int(input("Player 2:"))
    sum += plyr2
    print("The number is now ", sum)
    if sum == 100:
        print("Player 2 Wins")                 # if the second player got to 100 first Print "Player 1 wins".
        exit()                                 # Terminate the Application..
    elif sum > 100:
        print("Player 1 Wins")
        exit()