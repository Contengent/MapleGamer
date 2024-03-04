import cv2
import numpy as np
import pyautogui
import pygetwindow
import time


# TODO:
# incorperate
# make asychronous func - probably?

class vision:
    def __init__(self, thresholdIn=0.84, dimensionsIn=[0,0,1920,1080]):
        self.subjectIMG = ""        # cv2.image :sob:
        self.templatePoints = []    # list of points if valid :3
        self.playerCords = []       # player's current cordinates

        self.threshold = thresholdIn
        self.grabDimensions = dimensionsIn

        self.templateFound = False  
        self.minimapCalibrated = False



    def screenGrab(self, cachedName="missing.png"):
        '''
        Take a screenshot and save it to 'imgcache' folder.
        '''
        pyautogui.screenshot(f"imgcache/{cachedName}", self.grabDimensions)
        self.subjectIMG = cv2.imread(f"imgcache/{cachedName}")


    def findTemplate(self, templateName):
        '''
        Compare template to a sample and attempt to find it within the sample.
        Returns bool to 'self.templateFound' whenever it is run.
        '''

        templateImage = cv2.imread(f'assets/{templateName}')
        self.template_H, self.template_W = templateImage.shape[:-1]

        templateRes = cv2.matchTemplate(self.subjectIMG, templateImage, cv2.TM_CCOEFF_NORMED)
        templateLoc = np.where(templateRes >= self.threshold)
        
        self.templatePoints = []
        self.templatePoints = list(zip(*templateLoc[::-1])) # remember that this is a reversed list of all the points this template was found.

        try:
            self.templatePoints[0][0] # check if templatePoints has any values
            self.templateFound = True # if doesn't error out, template has been found (relative to 1920x1080)
        except:
            self.templateFound = False


    def windowGrab(self, windowName):
        '''
        For grabbing the specific program's displaying window.
        '''
        window = pygetwindow.getWindowsWithTitle(windowName)[0]
        
        up = window.top
        down = window.bottom
        left = window.left
        right = window.right

        self.grabDimensions = [left, up,  right - left, down - up] # This is weird.

        # This function is kinda useless until really later on :sob:


    def getMinimapLocation(self):
        '''
        Locates minimap and changes dimensions to fit only the minimap within screengrab.
        '''
        # This is relative to the 'self.windowGrab()' function written above.
        # If this seems to be broken, there might be an issue with that function.

        # Calibrating map cords
        if (self.minimapCalibrated != True):
            minimapTemplates = ["minimap_tl_template.png", "minimap_br_template.png"]
            minimapFound = True
            minimapCords = []

            self.screenGrab("calibrateMinimap.png") # Grab screen,

            for template in minimapTemplates:
                self.findTemplate(template) # Find minimap by templates
                if(self.templateFound):
                    minimapCords.append(self.templatePoints[0])
                else:
                    print("Couldn't find minimap...")
                    minimapFound = False
                
            # Set grabbing dimensions for minimap
            if(minimapFound):
                self.grabDimensions = [minimapCords[0][0], minimapCords[0][1],  minimapCords[1][0] - minimapCords[0][0] + 38, minimapCords[1][1] - minimapCords[0][1] + 25] # so fucking scuffed lmao
                self.minimapCalibrated = True
        pass


    def getPlayerCords(self):
        '''
        Locates player on minimap.
        Uses 'self.minimap()' ouput as it's source image.
        '''
        if(self.minimapCalibrated):
            self.findTemplate("player_template.png")
            if(self.templateFound):
                self.playerCords = [int(self.templatePoints[0][0]+5), int(self.templatePoints[0][1]+5)]

                print(f"Player(x, y): {str(self.playerCords[0])}, {str(self.playerCords[1])}")

            else:
                print("couldn't find player...")

        else:
            print("Please calibrate minimap :<")
            exit(0)
        

        


if __name__ == "__main__":
    awssdawd = vision()

    awssdawd.getMinimapLocation()

    while(True):
        awssdawd.screenGrab("minimap.png")
        awssdawd.getPlayerCords()
        time.sleep(0.2)
