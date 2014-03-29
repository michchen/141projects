# Proj2.py
# Fall 2013
# craps
#
# Modified by: Michelle Chen
# 
# This program simulates the game Craps where two die are rolled
# If the result is a 7 or 11, you win
# If the result is 2, 3, or 12, you lose
# If the result is anything else, you continue to roll until you match your
# original point (which means you win) or roll a 7 (which causes you to lose)

import random

wins = 0
throws = 0 
total_ones = 0
total_twos = 0
total_threes = 0
total_fours = 0
total_fives = 0
total_sixes = 0
games = 0
# All of the variables that need to be initialized to 0

seed = input("Please enter the random number seed: ")
print(seed)
seed = int(seed)
random.seed(seed)
# Random seed function

total_games = input("Please enter the number of games to play: ")
print(total_games)
total_games = int(total_games)

while games < total_games:
    die_one = random.randint(1,6)
    die_two = random.randint(1,6)
    orig_point = die_one + die_two
    # Adds up the randomly generated die values to get the point
    throws += 2
    # Adds up the throws for the end
    games += 1
    new_point = 0
    # new_point is initialized to 0 each time to prepare it for the next
    # while loop that uses the new_point as its condition
    if die_one == 1:
        total_ones += 1
    if die_one == 2:
        total_twos += 1
    if die_one == 3:
        total_threes += 1
    if die_one == 4:
        total_fours += 1
    if die_one == 5:
        total_fives += 1
    if die_one == 6:
        total_sixes += 1
    if die_two == 1:
        total_ones += 1 
    if die_two == 2:
        total_twos += 1
    if die_two == 3:
        total_threes += 1
    if die_two == 4:
        total_fours += 1
    if die_two == 5:
        total_fives += 1
    if die_two == 6:
        total_sixes += 1 
    # Counts the die values. Use if statement because if-elif-else causes
    # function to stop once one of the conditions in the if-elif-else is met
    if orig_point == 2 or orig_point == 3 or orig_point == 12:
        wins += 0
        # Loss leads to a win addition of 0
    elif orig_point == 7 or orig_point == 11:
        wins += 1 
    else:
        while new_point != orig_point and new_point != 7:
            die_one = random.randint(1,6)
            die_two = random.randint(1,6)
            new_point = die_one + die_two
            throws += 2
            # 2nd while loop to continue rolling until the above conditions are
            # met
            if die_one == 1:
                total_ones += 1
            if die_one == 2:
                total_twos += 1
            if die_one == 3:
                total_threes += 1
            if die_one == 4:
                total_fours += 1
            if die_one == 5:
                total_fives += 1
            if die_one == 6:
                total_sixes += 1
            if die_two == 1:
                total_ones += 1 
            if die_two == 2:
                total_twos += 1
            if die_two == 3:
                total_threes += 1
            if die_two == 4:
                total_fours += 1
            if die_two == 5:
                total_fives += 1
            if die_two == 6:
                total_sixes += 1 
            # counts the die values again
        if new_point == orig_point:
            wins += 1
        if new_point == 7:
            wins += 0

probability = wins / total_games
prob_one = total_ones / throws
prob_two = total_twos / throws
prob_three = total_threes / throws
prob_four = total_fours / throws
prob_five = total_fives / throws
prob_six = total_sixes / throws
# Figures out the probability for all of the individual dice and the whole.

print("")
print("We simulated {} games of Craps. ".format(total_games))
print("")
print("In all, a die was tossed {} times ".format(throws))
print("The numbers:  %11s %7s %7s %7s %7s %7s" % (1, 2, 3, 4, 5, 6))
print("Their frequencies:  %7s %7s %7s %7s %7s %7s" % \
(total_ones, total_twos, total_threes, total_fours, total_fives, total_sixes))
print("Their probabilities: %7.4f %7.4f %7.4f %7.4f %7.4f %7.4f" % \
(prob_one, prob_two, prob_three, prob_four, prob_five,  prob_six))
print("Of the {} simulated games, you won {} times. ".format(total_games, wins))
print("So the probability of winning at Craps is:  %.4f" % (probability))
# Prints all of the values with their own formatting