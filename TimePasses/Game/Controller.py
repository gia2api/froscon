'''
Created on 22.04.2015

@author: Zeeshan Islam
'''

class Controller(object):

    def __init__(self):
        self.B_UP = False
        self.B_DOWN = False
        self.B_LEFT = False
        self.B_RIGHT = False
        
        self.B_A = False
        self.B_B = False
        self.B_X = False
        self.B_Y = False
        
        self.B_START = False
        self.B_SECCT = False
        
        self.B_TRIGGER_L = False
        self.B_TRIGGER_R = False
        
        
    def getButtonStates(self, event):
        
        return