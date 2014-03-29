# Player.py
# CS 141
#
# Created by: Michelle Chen
# mchen01@email.wm.edu
# (937) 423-9630
#
# A class that calculates overall ratings, ratings by year, and figures out
# if names are equal, greater than, or less than each other. It then prints all
# information about ratings into a pretty format.

class Player (object):
    def __init__ (self, first, last):
        '''the constructor for a player'''
        self.first = first
        self.last = last
        self.rating = 0
        self.info = []


    def update(self, team, year, comp, att, yards, tds, itcs):
        '''create a list of information for this player for this year and 
append it to the info field. Then call calcrating.'''
        # appends the new info to the list
        self.info.append([year, team, comp, att, yards, tds, itcs])
       
        # calls calcrating to produce a new overall rating
        self.rating = self.calcrating()

        return self.info


    def calcrating(self):
        '''go through all sub-lists in info adding up totals for comps, 
attempts, etc. Then calculate the overall rating for this player. Store it
in the instance variable "rating" '''
        comp = 0
        att = 0
        yards = 0
        tds = 0
        itcs = 0         

        for item in self.info:
            # keeps a running total for overall rating
            comp += float(item[2])
            att += float(item[3])
            yards += float(item[4])
            tds += float(item[5])
            itcs += float(item[6])
        
        # does all of the calculations
        over_comp = ((comp / att) * 100 - 30) / 20
        over_yards = ((yards / att) - 3) / 4
        over_tds = (tds / att) * 20
        over_itcs = 2.375 - ((itcs / att) * 25)
        
        # calculates the rating
        self.rating = ((over_comp + over_yards + over_tds + over_itcs) / 6) \
            * 100
        
        return self.rating


    def returnName(self):
        '''return the name of the player first last'''
        return str(self.first) + " " + str(self.last)


    def returnReverseName(self):
        '''return the name of the player as last, first'''
        return str(self.last) + ", " + str(self.first)


    def __eq__ (self, other):
        '''determine if this person's name is the same as the other person's
name'''
        return self.first == other.first and self.last == other.last


    def __lt__(self, other):
        '''determine if this person's name is less than the other person's
name alphabetically'''
        # makes sure the to compare first name if last names are the same
        if self.last == other.last:
            return self.first < other.first
        else:
            return self.last < other.last


    def __gt__ (self, other):
        '''determine if this person's name is greater than the other person's
name alphabetically'''
        # makes sure the to compare first name if last names are the same
        if self.last == other.last:
            return self.first > other.first
        else:
            return self.last > other.last


    def __str__(self):
        '''return a string of the person's name and their rating in a nice
format'''
        return "{:20s} {:10.2f}".format((self.returnName()), self.rating)


    def calc(self, sublist):
        '''calculate a passer rating for one sub-list year in  the info list'''
        
        # looks through the info list
        for item in self.info:
            # finds the year
            if item[0] == sublist:
                # assigns variables
                comp = int(item[2])
                att = int(item[3])
                yards = int(item[4])
                tds = int(item[5])
                itcs = int(item[6])
        
        # does all of the calculations
        comp_rating = ((comp / att) * 100 - 30) / 20
        yards_rating = ((yards / att) - 3) / 4
        tds_rating = (tds / att) * 20
        itcs_rating = 2.375 - ((itcs / att) * 25)
        
        rating = ((comp_rating + yards_rating + tds_rating + itcs_rating) / 6) \
            * 100
        
        return rating


    def printInfo(self):
        '''print individual year information about his player including each 
year's passer rating. The list should be in year order. Use calc to assist.'''
        # sorts the list by year
        self.info.sort()
        rating = []
        count = 0
        for item in self.info:
            # appends all of these ratings into a list
            rating.append(self.calc(item[0]))
        
        print(self.returnName())
        
        for item in self.info:
            # uses a count to print out the right rating with the right year
            print(item[0], "in {:>3s} - {:>6.2f}".format(item[1], \
                                                         rating[count]))
            count += 1
