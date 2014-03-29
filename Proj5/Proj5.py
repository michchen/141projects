# Proj5.py, Fall 2013
# CS 141
#
# Created by: Michelle Chen
# mchen01@email.wm.edu
# (937)423-9630
#
# This program gives the user the option to 1. find a passer and print their
# career information and overall rating, 2. print all of the passers (sorted
# by year) of an individual team, 3. print a list of all players and their
# overall ratings.

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



def completions(passer_list, comp, attempt):
    """ Calculates completions part of algorithm and adds it to the """
    """ list of passers """
    count = 0
    
    for item in passer_list:
        # Calculates the completions part of algorithm
        completions = ((int(item[comp]) / int(item[attempt])) * 100 - 30) / 20
        # Appends it to the end of the list
        passer_list[count].append(completions)
        count += 1
    
    return passer_list
        


def yards(passer_list, yard, attempts):
    """ Calculates the yards part of algorithm and adds it to the passer list"""
    count = 0
    
    for item in passer_list:
        # Calculates the yards part
        yards = ((float(item[yard]) / (float(item[attempts])) - 3) / 4)
        # Adds it to the list
        passer_list[count].append(yards)
        count += 1
    
    return passer_list
    


def touchdowns(passer_list, touchdown, attempts):
    """ Calculates the touchdowns part of algorithm and adds it to the list"""
    count = 0
    
    for item in passer_list:
        # Calculates touchdowns
        touchdowns = (int(item[touchdown]) / (int(item[attempts])) * 20)
        passer_list[count].append(touchdowns)
        count += 1           
    
    return passer_list



def interceptions(passer_list, inter, attempts):
    """ Calculates the interceptions part of algorithm and adds it to list"""
    count = 0
    
    for item in passer_list:
        # Calculates interceptions part
        interceptions = 2.375 - ((int(item[inter]) / int(item[attempts])) * 25)
        passer_list[count].append(interceptions)
        count += 1
    
    return passer_list
    


def pass_rating(passer_list):
    """ Calculates the passer rating """
    count = 0
    
    # Calls the functions to compile the list    
    completions(passer_list, 6, 7)
    yards(passer_list, 8, 7)
    touchdowns(passer_list, 9, 7)
    interceptions(passer_list, 12, 7)
    
    for item in passer_list:
        # Uses the values to compile the rating and then appends it to the list        
        rating = ((item[13] + item[14] + item[15] + item[16]) / 6) * 100
        passer_list[count].append(rating)
        count += 1
    
    return passer_list



def overall_dictionary(passer_list):
    """ Calculates the overall passing rating """
    stats_list = []
    sum_list = []
    
    for item in passer_list:
        # Creates a list of values that we need with name first
        stats_list.append([(item[1] + ", " + item[0]), item[3], item[6], \
                             item[7], item[8], item[9], item[12]])
    
    stats_list.sort()
    # Sorts the list based on name
    
    name_list = []
    
    for item in stats_list:
        # Creates a list of unique names to later iterate through
        if item[0] in name_list:
            # Continues if the name is already in the list
            continue
        else:
            name_list.append(item[0])
            # Appends if it's not


    for name in name_list:
        # Iterates through the name list
        inner_list = []
        completion = 0
        attempts = 0
        yardage = 0
        touchdown = 0
        interception = 0
        # Variables that will later be used to keep track of sums
        
        for item in stats_list:
            if item[0] == name:
                # If the names match it sums up the corresponding values
                completion += int(item[2])
                attempts += int(item[3])
                yardage += int(item[4])
                touchdown += int(item[5])
                interception += int(item[6])
        # Appends all of this data into its own list
        sum_list.append([str(completion), str(attempts), str(yardage), \
                          str(touchdown), str(interception)])
    
    # Runs the functios defined earlier to calculate the overall passer rating 
    completions(sum_list, 0, 1)
    yards(sum_list, 2, 1)
    touchdowns(sum_list, 3, 1)
    interceptions(sum_list, 4, 1)
    count_two = 0
    for item in sum_list:
        rating = ((item[5] + item[6] + item[7] + item[8]) / 6) * 100
        sum_list[count_two].append(rating)
        count_two += 1
    
    # Initialize a overall list for all of the data
    overall_list =[]
    
    # Initialize a count to keep track of where in the name list we are
    count = 0
    
    for item in sum_list:
        # Creates a list of overall passer ratings and names
        overall_list.append([item[9], name_list[count]])
        count += 1
    
    overall_list.sort()
    overall_list = overall_list[::-1]
    # Sorts from greatest to least
    
    overall_dict = {}
    
    for value in overall_list:
        overall_dict[value[1]] = value[0]
        
    return overall_dict



def rating_dict(passer_list):
    """ Compiles the player dictionary and team dictionary"""
    
    info_list = []
    name_list = []
    team_list = []
    team_dict = {}
    player_dict = {}    

    for item in passer_list:
        # Generates a list of names, year, team, and ratings
        info_list.append([(item[0] + " " + item[1]), \
                          item[4], item[3], item[17]])
        
    for item in info_list:
        # Creates a list of unique names to later iterate through
        if item[0] in name_list:
            # Continues if the name is already in the list
            continue
        else:
            name_list.append(item[0])
            # Appends if it's not  
        
        # Creates a list of teams
        if item[2] in team_list:
            continue
        else:
            team_list.append(item[2])
        
    # Sorts name list
    name_list.sort()
    
    for name in name_list:
        # initializes dictionary keys and creates an empty list for the value
        player_dict[name] = []
    
    for name in name_list:
        for item in info_list:
            if item[0] == name:
                # Adds player data to their keys
                player_dict[name].append([item[1], item[2], item[3]])
    
    for team in team_list:
        # initializes team keys
        team_dict[team] = []
    
    for team in team_list:
        for item in info_list:
            if item[2] == team:
                # Adds team data to their keys
                team_dict[team].append([item[1], item[0], item[3]])
                
    return (team_dict, player_dict)

    

teams = \
{'MIA': 'Miami', 'NO':'New Orleans', 'STL':'St. Louis','NE':'New England',\
'SD':'San Diego','HOU':'Houston','MIN':'Minnesota','IND':'Indianapolis',\
'TEN':'Tennessee','OAK':'Oakland','ARI':'Arizona','KC':'Kansas City',\
'SF':'San Francisco','GB':'Green Bay','DAL':'Dallas','DET':'Detroit',\
'BAL':'Baltimore','CLE':'Cleveland','CIN':'Cincinnati','WAS':'Washington',\
'DEN':'Denver','NYG':'New York Giants','NYJ':'New York Jets','SEA':'Seattle',\
'ATL':'Atlanta', 'CAR':'Carolina','PHI':'Philadelphia','BUF':'Buffalo',\
'CHI':'Chicago','TB':'Tampa Bay',  'PIT':'Pittsburgh','JAX':'Jacksonville',\
'BOS':'Boston', 'BCL': 'Baltimore Colts' , 'NYY': 'New York Yankees',\
'NYT': 'Newark Tornadoes','DTX':'Dallas Texans' ,'RAM': 'Los Angeles Rams',\
'RAI':'Oakland Raiders','LAD':'Los Angeles Dons','LAC':'Los Angeles Chargers',\
'CRD':'Chicago Cardinals'}



def menu():
    print("Menu choices")
    print("a) Find a passer and print his career "\
"information and overall rating.")
    print("b) Find a team and print all the passers by year")
    print("c) Print a list of players and their ratings in alpha order")
    print("q) Quit")
    print("")



# Initializes the functions
passer_list = list_compiler()
rating = pass_rating(passer_list)
team_dict, player_dict = rating_dict(passer_list)
overall_dict = overall_dictionary(passer_list)

menu()
choice = input("Enter a choice: ")
# echo print
print(choice)
choice = choice.lower()

while choice != "q":
    
    if choice == "a":
        player = input("Enter the player's firstname lastname: ")
        print(player)
        
        if player in player_dict:
            # Sorts the list of values by year
            player_dict[player].sort()
            print("")
            print(player)
            for value in player_dict[player]:
                # Prints each list in the key's value
                print("    played for ", teams[value[1]], "in", value[0], \
                      "with a rating of %0.2f" % float(value[2]))
            
            # splits up the player's name to find it in the overall dictionary
            if len(player.split(" ")) == 2:
                # If there are only two parts, it assigns it to two variables
                firstname, lastname = player.split(" ")
                name = lastname + ", " + firstname                
            else:
                # If there are three, it uses three variables
                firstname, lastname, third = player.split(" ")
                # If the third part is a suffix, it assigns it to the end
                name = lastname + " " + third + ", " + firstname
                if name not in overall_dict:
                    # if the third part is a middle name it assigns it to the
                    # first name part
                    firstname, lastname, third = player.split(" ")
                    name = third + ", " + firstname + " " + lastname                   

            print(player, "has an overall rating of %0.2f" % \
                  (overall_dict[name]))
            print("")        
        else:
            # Error message if this person does not exist
            print("This person is not in the database\n")
        
    
    elif choice == "b":
        team = input("Enter the team's initials: ")
        print(team)
        
        if team in team_dict:
            # sorts values in the team by year
            team_dict[team].sort()
            print("")
            # Print long name of team
            print(teams[team])
            for player in team_dict[team]:
                # Prints each player in order of year
                print("   ", player[1], "played in", player[0], \
                      "with a rating of %0.2f" % float(player[2]))
            print("")
        else:
            # Error message
            print("This team is not in the database\n")
        
    elif choice == "c":
        print("")        
        for player in sorted(overall_dict):
            # Prints all the values
            print("%-22s %0.2f" % (player, float(overall_dict[player])))
        print("")
        
    else:
        print("")
        print("Illegal choice. Try again\n")
     
        
    menu()
    choice = input("Enter a choice: ")
    print(choice)
    choice = choice.lower()    


print("")        
print("Thanks for playing")
        
file.close()