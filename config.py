#from PyQt5.QtWidgets import *

uiButtonTable = []
ledStripLine = []           # Object of Led strip LEDs
myGrapicsScene = 1
mySingleLedShape = 0 #- 0-Rect, 1-Circle
myItemTabHandler = []
#quantuty of LED in strip
myLedInSingleRow = 30       #--== how may LED in one line of strip
myLedRow = 15               #--== how many strip
#Point size and position
myLedWith = 20              #==-- in pix X size on screen
myLedHight = 20             #==-- in pix Y size on screen
myLedDeltaX = 30            #==-- space in pix for 1 Led + 1 break in X
myLedDeltaY = 50            #==-- space in pix for 1 Led + 1 break in Y
#Program parameter
myProgMain = False          # ==-- handler for current program
myLedPointerMain = 0

myColorPrimary = 0x000000
myColorBg = 0xFFFFFF
myDeltaTime = 10
