﻿Measurable target of sprints will be:

6 actions

def Sell (Object):
'''
Input parameter is object you want to sell to merchant, type is string
Return parameter is cash merchant dersires for object, type is int 
Takes money from player, then takes object out of container and places it into the players hands
'''

def Buy (Object): 
'''
Input parameter is object you want to buy from merchant, type is string
Return parameter is cash merchant will give you for object, type is int
Takes object from player, then takes cash out of pocket and places it into the players hands
'''

def Flee ():
'''
Return parameter is Location of NPC after he has fled, type is string
Receives physical contact from player, if there is physical contact then NPC flees to police station
shoving physical contact out of the way. 
'''

def Give_Directions (DesiredLocation):
'''
Input parameter is DesiredLocation from player, type is string
Return parameter is X, Y coordinates of location, type is list
NPC orients himself at the dead reckoning position towards a target and points, within this function there are 8 distinct
places the npc can recognize and point to 
'''
			
def MakePB&J (DesirePB):
'''
Input parameter is DesirePB from player, type is bool
Return parameter is PBSatisfied, type is bool
NPC makes peanut butter and jelly and provides it to player 
'''

def Wave ():
'''
Once npc sees player he attempts to wave the player towards him
'''
