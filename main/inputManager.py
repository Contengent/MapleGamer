import fileManager as fileM
import vision as roboguy
import interception
import time
import random

# Keybinds (temporary until I implement a better solution lol)
jump = "c"
rope = "b"


class actions:
    '''
    All the player actions, and routine running.
    '''
    def __init__(self, _routine=fileM.inputs):
        interception.auto_capture_devices(keyboard=True)
        self.msVision = roboguy.vision()
        self.msVision.getMinimapLocation()

        self.routine = _routine
        self.heldKeys = []
        
    
    def movePlayer(self, destination=[0,0]):
        while True:
            self.msVision.screenGrab("minimap.png")
            self.msVision.getPlayerCords()
            current = self.msVision.playerCords

            if (destination[0] < current[0]):
                # Move right
                interception.key_up('right')
                interception.key_down('left')

            elif (current[0] < destination[0]):
                # Move left
                interception.key_up('left')
                interception.key_down('right')
            
            else:
                interception.key_up('left')
                interception.key_up('right')
                break

        """ while(destination[1] != current[1]):
            if (destination[1] < current[1]):
                # Move down / hold down and press jump (c)
                interception.key_down('down')
                interception.press(jump)
                interception.key_up('down')
                print("going down")

            elif (current[1] < destination[1]):
                # Move up / use rope
                interception.key_down(rope)
                time.sleep(random.randint(3,5)/10) # :s
                interception.key_up(rope)
                print("going up")
                
        print(f"Current: {current}")
        print(f"Destination: {destination}")  """
       
    def useInput(self, input=list):
        '''
        Use inputted value to preform a keyboard action
        '''

        match ((str(input[0]).lower())):
            case "press":
                interception.press(str(input[1]).lower(), int(input[2]))

            case "hold":
                interception.key_down(str(input[1]).lower())
                time.sleep(int(input[2]))
                interception.key_up(str(input[1]).lower())

            case "down":
                interception.key_down(str(input[1]).lower())
                self.heldKeys.append(str(input[1]).lower())

            case "up":
                interception.key_up(str(input[1]).lower())
                self.heldKeys.remove(str(input[1]).lower())


            case "wait":
                time.sleep(float(input[1]))

            case "move":
                self.movePlayer(destination=[int(input[1]), int(input[2])])
                pass

    def rotation(self, iterations=int):
        '''
        rotate through a given routine a given amount of times
        '''

        try:
            for i in range(iterations):
                for i in range(self.routine.totalLines):
                    self.useInput(self.routine.getNextInput())
        except KeyboardInterrupt:
            print("Returning to menu")
            pass

    

