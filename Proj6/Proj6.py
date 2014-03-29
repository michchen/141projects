# Proj6.py
# CS 141
#
# Created by: Michelle Chen
# mchen01@email.wm.edu
# (937) 423-9630
#
# Creates a list of players and their overall ratings. Then it asks if user 
# wants information on an individual player. If yes, then it offers to find
# the overall rating or to display each year they played and their
# individual year ratings.

from Player import Player

# imports csv and then opens the file
import csv
file = open("passers.csv", "r", encoding = "windows-1252")



def list_compiler():
    """ Compiles all of the data into a list within a list"""
    passer_list = []
    
    for line in file:
        if "vname" in line:
            continue
            # Skips the header
        line = line.strip()
        inner_list = line.split(",")
        # Compiles a list of the passers' information
        passer_list.append(inner_list)
    
    return passer_list



def dict_builder(passer_list):
    """ builds a dictionary with names as keys and Player objects as values"""
    
    #create player dictionary
    player_dict = {}
    
    for player in passer_list:
        # creates the Player object using the names
        name = Player(player[0], player[1])
        if Player.returnName(name) in player_dict:
            # calls update to update the information in self.info
            player_dict[Player.returnName(name)].update(player[3], player[4], \
            player[6], player[7], player[8], player[9], player[12])  
        else:
            # if the name is not already in dictionary it creates an entry
            player_dict[Player.returnName(name)] = name
            # enters the first dictionary entry into the list
            player_dict[Player.returnName(name)].update(player[3], player[4], \
            player[6], player[7], player[8], player[9], player[12])             

    return player_dict



def sorted_list(player_dict):
    # sorts the list of information from the dictionary
    overall_list = sorted(player_dict.values())

    for item in overall_list:
        #print alpha player list
        print(item)



def menu():
    print("")
    print("Pick one")
    print("a) Overall passer rating")
    print("b) Individual years and ratings")
    print("")

################################################################################


passer_list = list_compiler()
dictionary = dict_builder(passer_list)
sorted_list(dictionary)

print("")
choice = input("Do you want information about a particular player? ")
print(choice)
choice = choice.lower()

while choice == "y": 
    player = input("Enter player's name: ")
    print(player)
    
    # checks if player is in dictionary
    if player in dictionary:
        menu()
        choice2 = input("Enter choice: ")
        print(choice2)
        choice2 = choice2.lower()
        
        if choice2 == "a":
            print("")
            # prints the overall rating for the player
            print(dictionary[player])
            print("")
        elif choice2 == "b":
            print("")
            # prints each year's rating
            dictionary[player].printInfo()
            print("")
        else:
            print("")
            print("You've entered an illegal choice")
            print("")
    else:
        print("")
        print("This player is not in the system.")
        print("")
    
    choice = input("Are you interested in another player? ")
    print(choice)
    choice = choice.lower()
    
file.close()
