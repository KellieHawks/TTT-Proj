"""
    Authors: Noah Palmer, Holly Hardin, Isaac Lance
    Date: 03/10/2019
    CIS 422
    GoalTracker
"""
#System Imports
from datetime import datetime, timedelta
import copy

class TTTModel:
    """CONSTRUCTOR FOR MODEL"""
    def __init__(self, wins, losses, ties):

        self.wins = wins #list of goal objects
        self.losses = losses #integer
        self.ties = ties #integer

        self.topleft = ""
        self.topmiddle = ""
        self.topright = ""
        self.middleleft = ""
        self.middlemiddle = ""
        self.middleright = ""
        self.bottomleft = ""
        self.bottommiddle = ""
        self.bottomright = ""

    def get_wins(self):
        return self.wins

    def get_losses(self):
        return self.losses

    def get_ties(self):
        return self.ties

    def get_topleft(self):
        return self.topleft

    def get_topmiddle(self):
        return self.topmiddle

    def get_topright(self):
        return self.topright

    def get_middleleft(self):
        return self.middleleft

    def get_middlemiddle(self):
        return self.middlemiddle

    def get_middleright(self):
        return self.middleright

    def get_bottomleft(self):
        return self.bottomleft

    def get_bottommiddle(self):
        return self.bottommiddle

    def get_bottomright(self):
        return self.bottomright


