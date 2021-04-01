class AI:
  def __init__ (self,
                action = None,
                sense = None,
                Position = [0,0],
                FaceDirection = "North",
                Money = 100,
                Inventory = [],
                State = "Rest",
                Sprite = "Defualt.jpg"):
    #if Action == None:
    #  self.Action = Action
    #if Sense == None:
    #  self.Sense = Sense
    self.action = action
    self.sense = sense
    if self.action is None:
      self.action = Action()
    if self.sense is None:
      self.sense = Sense()
      
class Action:
  @staticmethod
  def buy(item,PlayerObject):
    if item in items:
      if item in AI.Inventory:
        PlayerObject.Inventory.append(item)
        Player.Money -= item.price
        AI.money +=item.price
        AI.Inventory.remove(item)

    else:
      return "That is not an item I possess"

  @staticmethod
  def sell()
    if item in items:
      if item in PlayerObject.Inventory:
        AI.Inventory.append(item)
        AI.Money -= item.price
        PlayerObject.money +=item.price
        PlayerObject.inventory.remove(item) 
    else:
      return "That is not an item Ive ever heard of"

  @staticmethod
  def Flee():
  	'''
  	plays flee.jpg 
  	'''
  	holder = AI.sprite
  	AI.sprite = flee.jpg
  	sleep 5sec
  	AI.sprite = holder
 	sys.exit()

  def wave(self):
    	rest = self.sprite
	    if self.state == "waving":
		      self.sprite = "Waving.gif"				 
		      self.sprite = "rest"
  
class Sense:
  def  hearing(x,y):

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
	def leftEar(self,x,y):
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
			
	def rightEar(self,x,y):
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
	def steroLocate(self,x,y):
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
			return NotHeard 
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
    """
    x, y = Ai.position
    AIVisionCone = [[x,y+2],[x,y+3],[x,y+4],
    [x-1,y+1],[x+1,y+1],[x-2,y+2],[x-1,y+2],[x+1,y+2],[x+2,y+2]]
    if Player.Position in AIVisionCone:
      return seen=True
    return seen=False

  
  def touch(self, object):
    '''
    METHOD of AI, check for for loop with all objects and characters
    inputs are the AI(passed in as self) and object to check is the positions of the AI and object are touching
    if AI and object touch, then determine if object 
      A) is moving
        return "attacked"
      B) return "no action"
    return should checked in main to see what action should be performed with object
      - attacked will cause flee
    '''

    if object.position == self.position:
      if object.speed > 0:
        return "Attacked"
    return "no action"

def Give_Directions (self):
Input parameter is DesiredLocation from player, type is string
    Holder = self.FaceDirection
    completed = 0 
    while completed == 0:
        read user input (DesiredLocation)
        Locations = {
            "Church":"North East"
            "Police Station":"North West"
            "Cave":"South West"
        }
        self.FaceDirection = Locations.Get(DesiredLocation, 0)
        if self.FaceDirection == 0:
            print ("Please Select a Location")
            completed = 0
        else:
            completed = 1
    self.FaceDirection = Holder
    return (Locations.Get(DesiredLocation))

def MakePB&J (self):
    Holder = self.sprite
    self.sprite = MakePBandJ.gif
    sleep 5ms
    add self.inventory(PBandJ)
    self.sprite = Holder 
