#####BRAINSTORM#####
#colored output, look into termcolor module?
#monster class
###probably similar to characters, but don't need nearly as much detail
###health, armor, attacks, maybe something else?
#weapon class
#supplies in dictionary where value is quantity
#easier commands (such as >>>2d4 instead of >>>dice(2,4)
#read in campaigns from encrypted files (via DM's password) w/ checksum
#extensive help pages & explanations
#combat function/class?
###rolling for initiative for all characters & monsters
###giving characters selection of weapons to use, via arrow key selection?
###allow characters to fight each other
###need to consider position in dungeon/when monsters enter combat?
#keep track of in-game date & time, announce when characters must eat/rest
#keep track of real life date & time to tag notes & name save files
####################

from random import randint

class character:

    ####CONSTRUCTOR####
    def __init__(self, Name, Class, Lvl):
        self.__name = Name
        self.__class = Class
        self.__level = Lvl
        #everything else on a character sheet: alignment, 6 physical attributes,
        #experience (linked to lvlUp), health, $ (in different denominations),
        #abilities and magic, supplies, armor class, character notes, species

    ####GETTERS####
    def chrSheet(self):
        pass
        #print out a character sheet nicely (centered name, etc.)

    ####SETTERS####
    def lvlUp(self):
        self.__level += 1

def dice(quantity, sides):
    #look into making functions of 1 or 2 parameters
    #in this case, it would assume 1 die if there were 1 parameter given
    dice = []
    total = 0
    for i in range(quantity):
        roll = randint(1,sides)
        dice.append(str(roll))
        total += roll
    print('Rolls:',' '.join(dice))
    print('Sum:',total)
