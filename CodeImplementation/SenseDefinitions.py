#Hearing 
class hearing:

	'''
	This function allows the NPC to hear with in the world
	
	leftEar() - When the an object makes a noise it will make an a line that grows +2 in each direction then remove its self and if left ear in range return Heard
	
	rightEar() - When the an object makes a noise it will make an a line that grows +2 in each direction then remove its self and if right ear in range return Heard
	
	steroLocate() - Will do ifs and figure out a cardnial direction based off the x and y of the incoming line  
	
	'''
	leftHear = "False"
	rightHear = "False"
	lEar = [x,y]
	rEar = [x,y]
	def leftEar(self,lat,lon):
		'''
		checks if left ear sound detection is in hearing radius   
		lat is the x of the soundline emitted by sound
		lon its the y of the soundline emitted by sound
		'''
		if lat == self.lEar[0]:
			self.leftHear = "True"
		elif lon == self.lEar[1]:
			self.leftHear = "True"
		else:	 
			self.leftHear = "False"
			
	def rightEar(self,lat,lon):
		'''
		checks if right ear sound detection is in hearing radius   
		lat is the x of the soundline emitted by sound
		lon its the y of the soundline emitted by sound
		'''
		if lat == self.rEar[0]:
			self.righttHear = "True"
		elif lon == self.rEar[1]:
			self.rightHear = "True"
		else:	 
			self.rightHear = "False"
	def steroLocate(self,lat,lon):
		'''
		Uses bothe leftEar and rightEar are true then checks direction based off that
		lat is the x of the soundline emitted by sound
		lon its the y of the soundline emitted by sound
		'''
		if self.leftHear and self.rightEar == "True":
			if (lon < 0):
				return Front 
			else:
				return Back
		elif self.leftHear == "False" and self.rightEar == "True":
			return Right
		elif self.leftHclass hearing:

	'''
	This function allows the NPC to hear with in the world
	
	leftEar() - When the an object makes a noise it will make an a line that grows +2 in each direction then remove its self and if left ear in range return Heard
	
	rightEar() - When the an object makes a noise it will make an a line that grows +2 in each direction then remove its self and if right ear in range return Heard
	
	steroLocate() - Will do ifs and figure out a cardnial direction based off the x and y of the incoming line  
	
	'''
	leftHear = "False"
	rightHear = "False"
	lEar = [x,y]
	rEar = [x,y]
	def leftEar(self,lat,lon):
		'''
		checks if left ear sound detection is in hearing radius   
		lat is the x of the soundline emitted by sound
		lon its the y of the soundline emitted by sound
		'''
		if lat == self.lEar[0]:
			self.leftHear = "True"
		elif lon == self.lEar[1]:
			self.leftHear = "True"
		else:	 
			self.leftHear = "False"
			
	def rightEar(self,lat,lon):
		'''
		checks if right ear sound detection is in hearing radius   
		lat is the x of the soundline emitted by sound
		lon its the y of the soundline emitted by sound
		'''
		if lat == self.rEar[0]:
			self.righttHear = "True"
		elif lon == self.rEar[1]:
			self.rightHear = "True"
		else:	 
			self.rightHear = "False"
	def steroLocate(self,lat,lon):
		'''
		Uses bothe leftEar and rightEar are true then checks direction based off that
		lat is the x of the soundline emitted by sound
		lon its the y of the soundline emitted by sound
		'''
		if self.leftHear and self.rightEar == "True":
			if (lon < 0):
				return Front 
			else:
				return Back
		elif self.leftHear == "False" and self.rightEar == "True":
			return Right
		elif self.leftHear == "True" and self.rightEar == "False":
			return Left
		else :
			return NotHeard ear == "True" and self.rightEar == "False":
			return Left
		else :
			return NotHeard 
				
def playerSearch(NPCposition,FaceDirection):
	"""
	Params:
		NPCposition = x,y grid coordinates of the npc
		FaceDirection = Cardinal direction of the face of the bot
	
	this function allows the NPC to sweep a 360 zone around them searching for the player.

	this function decides if the player should use a wider vision for searching or a 
	narrow vision for searching.
	
	
	wideLooks- this is a wider coned vision that isnt long range (distance wise)
	
	narrowLooks- this is a more narrow vision but has a longer range for distance spotting 
	
	Both cover the different fov for the npc so it can see/search
	for the player 
	
	"""
	def DistancetoWall(NPCposition,FaceDirection):
		"""
		checks if there is a wall within a range of 45 degrees to the left and right of the FaceDirection
		gathers the distance of the walls in what direction the wall was spotted.
		Using some complicated math algorithim it then decides whether to use wideLooks or narrowLooks
		
		if the npc is in a house default to wideLooks
		
		
		"""
	def wideLooks(NPCposition,FaceDirection):
		"""
		based on npc Position it activates. Based on the facingdirection and the location
		of the wall infront of the npc, if the wall is in x* meters away or inside a building 
		then this activates.
 		Using a wider vision (which has a short range) the NPC checks for the player. 
		x* is found through DistancetoWalls functions
		"""
	
	def narrowLooks(NPCposition,faceDirection):
		"""
		based on npc Position it activates. Based on the DistancetoWall function this function
		is chosen and gets ran by the npc.
		Using a narrow vision (which is long range) the NPC Checks for the player.
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
