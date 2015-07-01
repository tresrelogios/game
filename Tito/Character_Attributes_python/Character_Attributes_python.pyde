#<<<<<<<<<<««««««««««==========------------------==========»»»»»»»»»»>>>>>>>>>>#

"""
Ok, got an issue here: It looks like Processing Python won't run any
special function (setup, draw, mouseClicked, etc.) declared in a 
separate tab (file). Furthermore, I am forced to declare my classes,
functions, etc. before they are needed by the code below. As a result,
I have to write all my code in a single tab, which makes developing
something complex with Processing Python a nightmare! What a shame...

Anyways, here are notes for those who are not used to Processing:
  ->  Processing Python uses the Jython implementation of python2.7
  ->  mousePressed, mouseX, mouseY, width, height and most of the
     functions namesthat you see highlighted in blue in the PDE are 
     created by the Processing library
"""

# Uncomment the following line if you prefer the python3 way of printing things
# Note that in Processing you also have the println() function.
#from __future__ import print_function # back from the future

attributes = "size", "attack", "defense", "intelligence", "luck", "stamina"

# GLOBAL: Used by AttributeCustomizer.inc() and dec() methods
remaining_points = 20



################################################################
# GUI stuff                                                    #
################################################################

BTN_SIZE = 25
MARGIN = 25

class SquareButton:
    def __init__(self, x, y, label, onClick=lambda: None):
        self.x, self.y = (x,y)
        self.label = label
        self.onClick = onClick
        
    def isMouseOver(self):
        return (self.x < mouseX < self.x + BTN_SIZE
           and  self.y < mouseY < self.y + BTN_SIZE)
    
    def click(self):
        if self.isMouseOver():
            self.onClick()
    
    def getColor(self):
        if self.isMouseOver():
            if mousePressed:
                return 128
            else:
                return 192
        else:
            return 255
    
    def draw(self):
        fill(self.getColor())
        stroke(0) # Black outline
        strokeWeight(5) # 5px of thickness
        rect(self.x, self.y, BTN_SIZE, BTN_SIZE)
        
        # Let's assume that these buttons only display + or -
        if self.label in "-+":
            # Draw horizontal bar
            line(self.x + 7, self.y + BTN_SIZE/2,
                 self.x + BTN_SIZE - 7, self.y + BTN_SIZE/2) 
            if self.label == "+":
                # Draw vertical bar
                line(self.x + BTN_SIZE/2, self.y+7,
                     self.x + BTN_SIZE/2, self.y + BTN_SIZE-7)


# Gotta get a better name for this
# This is that thing that looks like <name of attribute>[+]10[-]
class AttributeCustomizer:
    
    def __init__(self, attr_name, y_pos, initial_value=10):
        self.label = attr_name
        self.y = y_pos
        self.value = initial_value
        
        self.plus_btn = SquareButton(400-MARGIN-BTN_SIZE, y_pos, "+", self.inc)
        self.minus_btn = SquareButton(400-MARGIN-100, y_pos, "-", self.dec)
        
    def inc(self):
        global remaining_points
        if remaining_points > 0:
            remaining_points -= 1
            self.value += 1
    
    def dec(self):
        global remaining_points
        if self.value > 0:
            remaining_points += 1
            self.value -= 1
        
    def click(self):
        self.plus_btn.click()
        self.minus_btn.click()
    
    def draw(self):
        fill(0)
        textSize(24)
        textAlign(LEFT, TOP)
        text(self.label.capitalize() + ":", MARGIN, self.y)
        
        self.plus_btn.draw()
        self.minus_btn.draw()
        
        fill(0)
        textAlign(CENTER, TOP)
        text(self.value, width-MARGIN-50, self.y)

                


######################################################################
# Some variables and stuff...                                        #  
######################################################################



y = 100
attr_dict = {}

for attr_name in attributes:
    attr_dict[attr_name] = AttributeCustomizer(attr_name, y)
    y += 50


######################################################################
# PROCESSING FUNCTIONS                                               #
######################################################################

# This function is called once when the sketch begins to run, so that
# we can setup some parameters like the window size, frame rate, etc.
# and eventually initialize some variables
def setup():
    size(400, 600)
    
# This function is called once every frame for us to draw stuff
def draw():
    background(192)
    for attribute_customizer in attr_dict.values():
        attribute_customizer.draw()
    
    textSize(28)
    textAlign(CENTER, TOP)
    text("Costumize your character", width/2, 20)
    
    textSize(18)
    textAlign(RIGHT)
    text("Remaining points: %s" % remaining_points, width-20, height-20)
    
# This function is called each time the user clicks. We can know where
# the cursor is with the mouseX and mouseY variables and know which
# mouse button was pressed with mouseButton (which can be set to the
# constants LEFT, RIGHT and CENTER
def mouseClicked():
    for attribute_customizer in attr_dict.values():
        attribute_customizer.click()
