# Proj4.py
# Fall 2013
# CS 141
#
# Created by: Michelle Chen
# mchen01@email.wm.edu
# (937)423-9630
#
# This program pulls information from a CSV file that contains passing
# information. The information is then sorted and the 50 players with the
# highest passer rating (computed using completions per attempt, yards
# per attempt, touchdowns per attempt, and interceptions per attempt).
# It also displays information on most yards passed, most touchdowns,
# highest completions per attempted pass, highest yardage for per attempted
# pass, and who got the most interceptions.

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



def completions(passer_list, value, valuetwo):
    """ Calculates completions part of algorithm and adds it to the """
    """ list of passers """
    count = 0
    
    for item in passer_list:
        # Calculates the completions part of algorithm
        completions = ((int(item[value]) / int(item[valuetwo])) * 100 - 30) / 20
        # Appends it to the end of the list
        passer_list[count].append(completions)
        count += 1
    
    return passer_list
        

def yards(passer_list, value, value_two):
    """ Calculates the yards part of algorithm and adds it to the passer list"""
    count = 0
    
    for item in passer_list:
        # Calculates the yards part
        yards = ((float(item[value]) / (float(item[value_two])) - 3) / 4)
        # Adds it to the list
        passer_list[count].append(yards)
        count += 1
    
    return passer_list
    

def touchdowns(passer_list, value, value_two):
    """ Calculates the touchdowns part of algorithm and adds it to the list"""
    count = 0
    
    for item in passer_list:
        # Calculates touchdowns
        touchdowns = (int(item[value]) / (int(item[value_two])) * 20)
        passer_list[count].append(touchdowns)
        count += 1           
    
    return passer_list


def interceptions(passer_list, value, value_two):
    """ Calculates the interceptions part of algorithm and adds it to list"""
    count = 0
    
    for item in passer_list:
        # Calculates interceptions part
        interceptions = 2.375 - ((int(item[value]) / int(item[value_two])) * 25)
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



def data_list(passer_list):
    """ Compiles a list of the top 50 passer ratings"""
    data = []
    
    for item in passer_list:
        # Compiles a list putting passer rating at index 0
        data.append([item[17], (item[0] + " " + item[1]), item[3], item[4]])
    
    data.sort()
    data = data[::-1]
    # Sorts the data and then reverses it to show the biggest values first
    
    # Only returns the first 50 players because that's what we want
    return data[0:50]
    
    
def overall_passing(passer_list):
    """ Calculates the overall passing rating """
    overall_list = []
    data_list = []
    
    for item in passer_list:
        # Creates a list of values that we need with name first
        overall_list.append([(item[0] + " " + item[1]), item[3], item[6], \
                             item[7], item[8], item[9], item[12]])
    
    overall_list.sort()
    # Sorts the list based on name
    
    name_list = []
    
    for item in overall_list:
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
        
        for item in overall_list:
            if item[0] == name:
                # If the names match it sums up the corresponding values
                completion += int(item[2])
                attempts += int(item[3])
                yardage += int(item[4])
                touchdown += int(item[5])
                interception += int(item[6])
        # Appends all of this data into its own list
        data_list.append([str(completion), str(attempts), str(yardage), \
                          str(touchdown), str(interception)])
    
    # Runs the functios defined earlier to calculate the overall passer rating 
    completions(data_list, 0, 1)
    yards(data_list, 2, 1)
    touchdowns(data_list, 3, 1)
    interceptions(data_list, 4, 1)
    count_two = 0
    for item in data_list:
        rating = ((item[5] + item[6] + item[7] + item[8]) / 6) * 100
        data_list[count_two].append(rating)
        count_two += 1
    
    # Initialize a master list for all of the data
    master_list =[]
    
    # Initialize a count to keep track of where in the name list we are
    count = 0
    
    for item in data_list:
        # Creates a list of overall passer ratings and names
        master_list.append([item[9], name_list[count]])
        count += 1
    
    master_list.sort()
    master_list = master_list[::-1]
    # Sorts from greatest to least
      
    return master_list



def most_yards(passer_list):
    """ Calculates who has the most yards in a year"""
    yard_list = []
    
    for item in passer_list:
        # Creates a list of the yardages
        yard_list.append([int(item[8]), item[0], item[1], item[3], item[4]])
    
    yard_list.sort()
    # Sorts from largest to smallest
    yard_list = yard_list[::-1]
    
    # Returns only the largest value
    return yard_list[0]


def most_touchdowns(passer_list):
    """ Calculates who has the most touchdowns in a year"""
    tdown_list = []
    
    for item in passer_list:
        # Creates a list of the touchdowns
        tdown_list.append([int(item[9]), item[0], item[1], item[3], item[4]])
    
    tdown_list.sort()
    # Sorts from largest to smallest
    tdown_list = tdown_list[::-1]
    
    # Returns only the largest value
    return tdown_list[0]

def highest_completions(passer_list):
    """ Calculates who has the highest number of completions per pass attempt"""
    comp_list = []
    
    for item in passer_list:
        # Compiles a list of the highest completions
        comp_list.append([((int(item[6]) / int(item[7])) * 100), \
                          item[0], item[1], item[3], item[4]])
    
    comp_list.sort()
    # Sorts from largest to smallest
    comp_list = comp_list[::-1]
    
    # Returns only the largest value
    return comp_list[0]    

def highest_yardage(passer_list):
    """ Calculates who has the highest yardage per attempted pass """
    yardage_list = []
    
    for item in passer_list:
        # Creates a list of the yardage per attempted pass
        yardage_list.append([(float(item[8]) / float(item[7])), \
                             item[0], item[1], item[3], item[4]])
    
    yardage_list.sort()
    # Sorts from largest to smallest
    yardage_list = yardage_list[::-1]
    
    # Only returns the largest value
    return yardage_list[0]      


def most_interceptions(passer_list):
    """ Calculates who got the most interceptions """
    intercep_list = []
    
    for item in passer_list:
        # Creates list of the most interceptions
        intercep_list.append([int(item[12]), item[0], \
                              item[1], item[3], item[4]])
    
    intercep_list.sort()
    # Sorts from largest to smallest
    intercep_list = intercep_list[::-1]
    
    # Only returns the largest value
    return intercep_list[0]


def specific_player(master_list, first_name, last_name):
    """ Finds the overall passing rating for a specific player """
    # Iterates through the list of overall pass ratings
    for item in master_list:
        if first_name in item[1] and last_name in item[1]:
            # Returns a list of information if above is true
            return [first_name, last_name, item[0]]
        else:
            # Returns an error message if there are no people with that name
            return "There are no players with that name"



# Run through all of the functions
passer_list = list_compiler()
rating = pass_rating(passer_list)
rating_list = data_list(passer_list)
most_yards = most_yards(passer_list)
most_touch = most_touchdowns(passer_list)
high_comp = highest_completions(passer_list)
high_yard = highest_yardage(passer_list)
most_inter = most_interceptions(passer_list)
overall_rating = overall_passing(passer_list)


print("The top 50 passers based on their passer rating in individual \
years are:")
print("")
print("%s %28s %7s %5s" % ("Name", "Year", "Rating", "Team"))

# Prints all of the 50 values in the list of passer ratings
for item in rating_list:
    print("%-28s %-5s %-7.2f %s" % (item[1], item[3], item[0], item[2]))


# Prints the best overall passing player
print("")
print("The best player is: ", overall_rating[0][1], "with an overall \
passer rating of %0.2f." % (overall_rating[0][0]))
print("")
print("The remainder of the top 20 are:")

count = 1
for value in overall_rating[1:20]:
    # Count keeps a number count on the left most side
    count += 1
    # Prints the rest of the 20 overall best passing players
    print("%2d   %-20s %-5.2f" % (count, value[1], value[0]))

print("")
print("The person who passed for the most yardage is:")
# Prints whoever has the most yardage
print("   %s %s passing %d yards for %s in %s." \
% (most_yards[1], most_yards[2], most_yards[0], most_yards[3], most_yards[4]))

print("")
print("The person who scored the most passing touchdowns is:")
# Prints the person with the most passing touchdowns
print("   %s %s scoring %d touchdowns for %s in %s." \
% (most_touch[1], most_touch[2], most_touch[0], most_touch[3], most_touch[4]))

print("")
print("The person who has the highest completions per attempted pass is:")
# Prints the person with the highest completions
print("   %s %s with a %0.2f percent completion rate for %s in %s." \
% (high_comp[1], high_comp[2], high_comp[0], high_comp[3], high_comp[4]))

print("")
print("The person who has the highest yardage per attempted pass is:")
# Prints the person with the highest yardage
print("   %s %s passing %0.1f yards per attempt for %s in %s." \
% (high_yard[1], high_yard[2], high_yard[0], high_yard[3], high_yard[4]))

print("")
print("The person with the most interceptions in a season is:")
# Prints the person with the most interceptions
print("   %s %s with %d interceptions for %s in %s." \
% (most_inter[1], most_inter[2], most_inter[0], most_inter[3], most_inter[4]))
print("")


choice = input("Are you interested in the overall rating of a \
particular player? ")
print(choice)
# Lowercase the choice
choice = choice.lower()

while choice == "y":
    first_name = input("Enter the player's first name: ")
    print(first_name)
    # Capitalize the name in case it was entered in lowercase
    first_name = first_name.capitalize()
    
    last_name = input("Enter the player's last name: ")
    print(last_name)
    # Capitalize again
    last_name = last_name.capitalize()
    print("")
    
    player_info = specific_player(overall_rating, first_name, last_name)
    
    # Prints the player if found
    try:
        print("%s %s  %0.2f" % (player_info[0], player_info[1], player_info[2]))
    # If no values are found it will return a TypeError
    except TypeError:
        print(player_info)
        # Prints the error message
    print("")
    
    # Keeps the loop from becoming infinite
    choice = input("Are you interested in the overall rating of a \
particular player? ")
    print(choice)
    # Lowercase the choice
    choice = choice.lower()    

file.close()
