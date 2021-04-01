#Hearing 
def hearing(x,y):

	'''
	This function allows the NPC to hear with in the world
	
	leftEar() - When the an object makes a noise it will make an a line that grows +2 in each direction then remove its self and if left ear in range return Heard
	
	rightEar() - When the an object makes a noise it will make an a line that grows +2 in each direction then remove its self and if right ear in range return Heard
	
	steroLocate() - Will do ifs and figure out a cardnial direction based off the x and y of the incoming line  
	
	'''

	def leftEar(self,x,y):
		'''
		checks if left ear sound detection is in hearing radius   
		lat is the x of the soundline emitted by sound
		lon its the y of the soundline emitted by sound
		'''
			
	def rightEar(self,x,y):
		'''
		checks if right ear sound detection is in hearing radius   
		lat is the x of the soundline emitted by sound
		lon its the y of the soundline emitted by sound
		'''

	def steroLocate(self,x,y):
		'''
		Uses bothe leftEar and rightEar are true then checks direction based off that
		lat is the x of the soundline emitted by sound
		lon its the y of the soundline emitted by sound
		'''


 def Sight(AI.position,Player.Position,FaceDirection):
    #returns seen as true if the player has been seen
    #returns seen as false if the player has not seen
    """
    Params:
        AI.position = x,y grid coordinates of the NPC
        Player.Position = x,y grid coordinates of the Player
        FaceDirection = Cardinal directions. the way the character is facing

    vars:
        Seen = true or false boolean based on if the player is seen by the ai
        AIVisionCone = cone of vision of the ai for making seen true or false
    Def:
	Function used to detect if the player is within the vision cone of the AI
	"""

	
def touch(self, object):
'''
METHOD of AI, check for for loop with all objects and characters
inputs are the AI(passed in as self) and object to check is the positions of the AI and object are touching
if AI and object touch, then determine if object 
	A) is moving
		return "attacked"
	B) is object owned by AI
		return "selling"
return should checked in main to see what action should be performed with object
	- attacked will cause flee
	- selling will cause the sell action
'''

}
