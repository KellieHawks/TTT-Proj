"""
    Authors: Kellie Hawks
    Date: 04/14/2019
    CIS 407
    Tic Tac Toe Bot
    Cite: Rules for tictactoe - http://www.cyberoculus.com/tic-tac-toe.asp?Action=Rules
"""
#System Imports
import sys
import random
import time
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from datetime import datetime, timedelta
from Model import TTTModel

# Global variable for storing UI files
UI_PATHS = {"MainWindow": "../UI/MainWindow.ui", "RuleWindow": "../UI/rules.ui"}

class rule_window(QDialog):
    def __init__(self, model):
        super(rule_window, self).__init__()#Call super of QDialog
        loadUi(UI_PATHS["RuleWindow"], self) #Load the correct ui (and therefore all it's elements)
        self.m = model         #The model is passed from the MainView so that the dialog can have the model save user data.

class MainWindow(QMainWindow):
    def __init__(self):

        super(MainWindow, self).__init__() #Initializes parent constructor
        loadUi(UI_PATHS["MainWindow"], self) # Load the Main Window UI

        #Class Variables
        self.movebuttons.setExclusive(False) #makes it so each button can be pressed individually
        self.m = TTTModel(0,0,0) #create an instance of the model
        self.setWindowTitle('Tic Tac Toe Bot') #update the windows title
        self.yourplayer = None
        self.otherplayer = None
        self.movenumber = 0
        self.playagain = False

        self.AIturn = None
        self.gofirst() #decides who goes first

        self.AImoves = [] #creates a array to keep track of AImoves
        for i in range(9):
            self.AImoves.append(None)

        #Connect Buttons
        self.giveupbutton.clicked.connect(self.giveup)
        self.resetbutton.clicked.connect(self.reset)
        self.rulesbutton.clicked.connect(self.rules)

        for button in self.movebuttons.buttons(): #deals with clicking any on the 3x3 buttons to make a move
            button.clicked.connect(lambda: self.gamebutton(self.yourplayer))

        self.refresh() #refeshes score and board

    def refresh(self):
        self.wincheck(1) #check if user won
        self.wincheck(0) #check if AI won
        self.tiecheck() #check if there is a tie

        self.winnum.setText(str(self.m.wins)) #reset number of wins to accurate num
        self.lossnum.setText(str(self.m.losses)) #reset number of losses to accurate num
        self.tienum.setText(str(self.m.ties)) #reset number of ties to accurate num

        self.updateboard() #update board

        if (self.AIturn == True and self.playagain == False):
            self.AImovefunc() #AI makes move if opponent did not win with last move
        
        self.wincheck(0) #check if win codnitions for AI succeeded
        if (self.playagain == False):
            self.tiecheck() #not sure if needed maybe can be in another piece of code

        return

    @pyqtSlot()
    def gofirst(self): #checks who will go first
        start = random.randint(1, 10) #randomly generates number between 1 and 10
        if start % 2 == 1: #if number is odd
            self.yourplayer = "X" #you go first
            self.otherplayer = "O"
            self.playername.setText("X") #set text to "X"
            self.AIturn = False #toggle whos turn it is
            print("You go first...")

            self.movenumber += 1
            print("Move Number: " + str(self.movenumber))

        if start % 2 == 0: #if your number is even
            self.yourplayer = "O" #AI goes first
            self.otherplayer = "X"
            self.playername.setText("0") #set text to "O"
            self.AIturn = True #toggle whose turn it is
            print("Computer goes first...")

        return

    @pyqtSlot()
    def gamebutton(self, yourplayer):

        abstract_button = self.sender() #get sender
        button = abstract_button.objectName() #get buttonname

        print("You made the move: " + str(button))

        if (button == "topleft"):           #locate which button, and then assign as your player
            self.yourplayer = yourplayer
            self.m.topleft = yourplayer
        if (button == "topmiddle"):
            self.yourplayer = yourplayer
            self.m.topmiddle = yourplayer
        if (button == "topright"):
            self.yourplayer = yourplayer
            self.m.topright = yourplayer
        if (button == "middleleft"):
            self.yourplayer = yourplayer
            self.m.middleleft = yourplayer
        if (button == "middlemiddle"):
            self.yourplayer = yourplayer
            self.m.middlemiddle = yourplayer
        if (button == "middleright"):
            self.yourplayer = yourplayer
            self.m.middleright = yourplayer
        if (button == "bottomleft"):
            self.yourplayer = yourplayer
            self.m.bottomleft = yourplayer
        if (button == "bottommiddle"):
            self.yourplayer = yourplayer
            self.m.bottommiddle = yourplayer
        if (button == "bottomright"):
            self.yourplayer = yourplayer
            self.m.bottomright = yourplayer

        abstract_button.setEnabled(False) #turn that button off
        self.AIturn = True
        self.refresh() #refesh to update text
        return

    @pyqtSlot()
    def placemoveincorner(self, number): #function that places a move in a corner
        
        ret = ""
        fmove = random.randint(1,4) #gets random number from 1-4

        if (number == 1):           #based on what number, place a x in that position, set button as disabled and update movelist
            if fmove == 1:
                self.m.topleft = self.otherplayer
                self.topleft.setEnabled(False)
                self.AImoves[0] = "topleft"
            if fmove == 2:
                self.m.topright = self.otherplayer
                self.topright.setEnabled(False)
                self.AImoves[0] = "topright"
            if fmove == 3:
                self.m.bottomleft = self.otherplayer
                self.bottomleft.setEnabled(False)
                self.AImoves[0] = "bottomleft"
            if fmove == 4:
                self.m.bottomright = self.otherplayer
                self.bottomright.setEnabled(False)
                self.AImoves[0] = "bottomright"

        if (number == 2):
            if fmove == 1:
                self.m.topleft = self.otherplayer
                self.topleft.setEnabled(False)
                self.AImoves[1] = "topleft"
            if fmove == 2:
                self.m.topright = self.otherplayer
                self.topright.setEnabled(False)
                self.AImoves[1] = "topright"
            if fmove == 3:
                self.m.bottomleft = self.otherplayer
                self.bottomleft.setEnabled(False)
                self.AImoves[1] = "bottomleft"
            if fmove == 4:
                self.m.bottomright = self.otherplayer
                self.bottomright.setEnabled(False)
                self.AImoves[1] = "bottomright"

        return 

    @pyqtSlot()
    def wincheck(self, number): #checks two things if called with 1 or 2, checks if user meets win conditions. increments/decrements score accordingly
        if (number == 1):
            playerpiece = self.yourplayer
        else:
            playerpiece = self.otherplayer

        if (self.m.topleft == playerpiece and self.m.topmiddle == playerpiece and self.m.topright == playerpiece or
            self.m.middleleft == playerpiece and self.m.middlemiddle == playerpiece and self.m.middleright == playerpiece or
            self.m.bottomleft == playerpiece and self.m.bottommiddle == playerpiece and self.m.bottomright == playerpiece or
            self.m.topleft == playerpiece and self.m.middleleft == playerpiece and self.m.bottomleft == playerpiece or
            self.m.topmiddle == playerpiece and self.m.middlemiddle == playerpiece and self.m.bottommiddle == playerpiece or
            self.m.topright == playerpiece and self.m.middleright == playerpiece and self.m.bottomright == playerpiece or
            self.m.topleft == playerpiece and self.m.middlemiddle == playerpiece and self.m.bottomright == playerpiece or
            self.m.topright == playerpiece and self.m.middlemiddle == playerpiece and self.m.bottomleft == playerpiece):
            if self.yourplayer == playerpiece: #if your piece is the playerpiece
                self.m.wins += 1 #increment wins
                print("YOU HAVE WON!!") #you win!
                self.playagain = True #set playagain variable to true to toggle button use

            else:
                self.m.losses += 1 #increment losses
                print("YOU HAVE LOST! :(") #you lose
                self.playagain = True #set playagain variable to true to toggle button use
                
            if (self.playagain == True): #if playagain is true, diable all buttons and wait for "playagain" button press
                self.topleft.setEnabled(False)
                self.topmiddle.setEnabled(False)
                self.topright.setEnabled(False)
                self.middleleft.setEnabled(False)
                self.middlemiddle.setEnabled(False)
                self.middleright.setEnabled(False)
                self.bottomleft.setEnabled(False)
                self.bottommiddle.setEnabled(False)
                self.bottomright.setEnabled(False)

                self.giveupbutton.setText("Play Again?") #change text of give-up button

            self.winnum.setText(str(self.m.wins)) #reset number of wins to accurate num
            self.lossnum.setText(str(self.m.losses)) #reset number of losses to accurate num
            self.tienum.setText(str(self.m.ties)) #reset number of ties to accurate num

            #self.updateboard()
            #self.clearboard()

        return

    @pyqtSlot()
    def tiecheck(self): #if these is a piece in all positions and win condition not met, increment tie
        if (self.m.topleft != "" and
            self.m.topmiddle != "" and
            self.m.topright != "" and
            self.m.middleleft != "" and
            self.m.middlemiddle != "" and
            self.m.middleright != "" and
            self.m.bottomleft != "" and
            self.m.bottommiddle != "" and
            self.m.bottomright != ""):

            self.m.ties += 1 #increment number of ties
            print("CATS GAME - TIE")

            self.playagain = True #set playagain variable to true to toggle button use
            
            self.topleft.setEnabled(False) #disable all buttons and wait for signal from playagain button
            self.topmiddle.setEnabled(False)
            self.topright.setEnabled(False)
            self.middleleft.setEnabled(False)
            self.middlemiddle.setEnabled(False)
            self.middleright.setEnabled(False)
            self.bottomleft.setEnabled(False)
            self.bottommiddle.setEnabled(False)
            self.bottomright.setEnabled(False)

            self.giveupbutton.setText("Play Again?") #update text

            self.winnum.setText(str(self.m.wins)) #reset number of wins to accurate num
            self.lossnum.setText(str(self.m.losses)) #reset number of losses to accurate num
            self.tienum.setText(str(self.m.ties)) #reset number of ties to accurate num

            #self.clearboard() #clearboard for new game

        return

    @pyqtSlot()
    def AImovefunc(self): #AIMovefunc has several base moves that are hard coded to include randomness,
                          #after base moves have been established, winning moves, blocking moves and then random moves are done.
        self.movenumber += 1
        print("Move Number: " + str(self.movenumber))

        if (self.canwincheck(self.otherplayer, 0) != 0): #checks if the AI can win in one move
            self.updateboard()
            self.AIturn = False #sets AI turn to false, so user can play
            return

        if (self.canwincheck(self.otherplayer, 1) != 0): #checks if the AI can place a move to block
            self.updateboard()
            self.AIturn = False #sets AI turn to false, so user can play
            print("Your move... ")
            self.movenumber += 1 #increment move
            print("Move Number: " + str(self.movenumber))
            return  

        if self.otherplayer == "X": #if comp is the first to move            
            if (self.movenumber == 1):
                self.placemoveincorner(1) #place x in random corner

            if (self.movenumber == 3):
                tmove = random.randint(1,2)
                bmove = random.randint(1,2)
                if (self.m.middlemiddle == "O"): #if an x is placed in center, find diagonal of first placed piece and place new piece there
                    if (tmove == 1):
                        if(self.AImoves[0] == "topleft"):
                            self.m.bottomright = "X"
                            self.bottomright.setEnabled(False)
                            self.AImoves[2] = "bottomright"
                        if(self.AImoves[0] == "topright"):
                            self.m.bottomleft = "X"
                            self.bottomleft.setEnabled(False)
                            self.AImoves[2] = "bottomleft"
                        if(self.AImoves[0] == "bottomright"):
                            self.m.topleft = "X"
                            self.topleft.setEnabled(False)
                            self.AImoves[2] = "topleft"
                        if(self.AImoves[0] == "bottomleft"):
                            self.m.topright = "X"
                            self.topright.setEnabled(False)
                            self.AImoves[2] = "topright"
                    if (tmove == 2):
                        if (self.AImoves[0] == "topleft"):
                            if (bmove == 1):
                                self.m.middleright = "X"
                                self.middleright.setEnabled(False)
                                self.AImoves[2] = "middleright"
                            else:
                                self.m.bottommiddle = "X"
                                self.bottommiddle.setEnabled(False)
                                self.AImoves[2] = "bottommiddle"
                        if (self.AImoves[0] == "topright"):
                            if (bmove == 1):
                                self.m.middleleft = "X"
                                self.middleleft.setEnabled(False)
                                self.AImoves[2] = "middleleft"
                            else:
                                self.m.bottommiddle = "X"
                                self.bottommiddle.setEnabled(False)
                                self.AImoves[2] = "bottommiddle"
                        if (self.AImoves[0] == "bottomright"):
                            if (bmove == 1):
                                self.m.topmiddle = "X"
                                self.topmiddle.setEnabled(False)
                                self.AImoves[2] = "topmiddle"
                            else:
                                self.m.middleleft = "X"
                                self.middleleft.setEnabled(False)
                                self.AImoves[2] = "middleleft"
                        if (self.AImoves[0] == "bottomleft"):
                            if (bmove == 1):
                                self.m.middleright = "X"
                                self.middleright.setEnabled(False)
                                self.AImoves[2] = "middleright"
                            else:
                                self.m.topmiddle = "X"
                                self.topmiddle.setEnabled(False)
                                self.AImoves[2] = "topmiddle"
                                #movenotmadeyet = False

                else: #if other player did not put a O in the center:
                    if (self.AImoves[0] == "topleft"):
                        resnum = self.check("topleft")
                        rannum = random.randint(0,len(resnum)-1)
                        btn = resnum[rannum]
                        self.buttonsetup(btn)
                    if (self.AImoves[0] == "topright"):
                        resnum = self.check("topright")
                        rannum = random.randint(0,len(resnum)-1)
                        btn = resnum[rannum]
                        self.buttonsetup(btn)
                    if (self.AImoves[0] == "bottomleft"):
                        resnum = self.check("bottomleft")
                        rannum = random.randint(0,len(resnum)-1)
                        btn = resnum[rannum]
                        self.buttonsetup(btn)
                    if (self.AImoves[0] == "bottomright"):
                        resnum = self.check("bottomright")
                        rannum = random.randint(0,len(resnum)-1)
                        btn = resnum[rannum]
                        self.buttonsetup(btn)

                    self.AImoves[2] = btn #third move

        if self.otherplayer == "O": #if computer is second player...
            if (self.movenumber == 2):
                if (self.m.middlemiddle == "X"): #if the first player placed an X in center...
                    self.placemoveincorner(2)
                elif(self.m.middlemiddle == ""): #if there is nothing in middle square, place piece there
                    self.m.middlemiddle = self.otherplayer
                    self.middlemiddle.setEnabled(False)
                    self.AImoves[1] = "middlemiddle"

            if (self.movenumber == 4):
                if (self.m.middlemiddle == "X"): #if an x is placed in center, find diagonal of first placed piece and place new piece there
                    if(self.AImoves[0] == "topleft"):
                        self.bottomright = "O"
                    if(self.AImoves[0] == "topright"):
                        self.bottomleft = "O"
                    if(self.AImoves[0] == "bottomright"):
                        self.topleft = "O"
                    if(self.AImoves[0] == "bottomleft"):
                        self.topright = "O"

        #if there has been no move done yet, and a random move is possible, complete random move
        if (self.AImoves[(self.movenumber-1)] == None and self.randommove(self.otherplayer, self.movenumber) == 1):
            #print("random" + str(self.AImoves))
            self.updateboard()
            self.AIturn = False #sets AI turn to false, so user can play
            print("Your move...")
            self.movenumber += 1 #increment move
            print("Move number: " + str(self.movenumber))
            return

        #print(self.AImoves)
        print("Computer made move: " + str(self.AImoves[self.movenumber-1]))

        self.updateboard() 
        self.AIturn = False #sets AI turn to false, so user can play
        print("Your move...")
        self.movenumber += 1 #increment move
        print("Move number: " + str(self.movenumber))
        return

    @pyqtSlot()
    def check(self, checkedspace): #fuction is special subroutine to check for a particular situation arising, 
                                   #returns spots AI can/should place moves based on desired behavior
        arrayofgoodspots = []
        if (checkedspace == "topleft"):
            arrayofgoodspots.append("bottomright")
            if (self.m.middleleft != "O"):
                arrayofgoodspots.append("bottomleft")
            if (self.m.topmiddle != "O"):
                arrayofgoodspots.append("topright")

        if (checkedspace == "topright"):
            arrayofgoodspots.append("bottomleft")
            if (self.m.topmiddle != "O"):
                arrayofgoodspots.append("topleft")
            if (self.m.middleright != "O"):
                arrayofgoodspots.append("bottomright")

        if (checkedspace == "bottomleft"):
            arrayofgoodspots.append("topright")
            if (self.m.middleleft != "O"):
                arrayofgoodspots.append("topleft")
            if (self.m.bottommiddle != "O"):
                arrayofgoodspots.append("bottomright")

        if (checkedspace == "bottomright"):
            arrayofgoodspots.append("topleft")
            if (self.m.middleright != "O"):
                arrayofgoodspots.append("topright")
            if (self.m.bottommiddle != "O"):
                arrayofgoodspots.append("bottomleft")
        #print(arrayofgoodspots)

        return arrayofgoodspots

    @pyqtSlot()
    def buttonsetup(self, btn): #more subroutines
        if ("topleft" == btn):
            self.m.topleft = "X"
            self.topleft.setEnabled(False)
        if ("topright" == btn):
            self.m.topright = "X"
            self.topright.setEnabled(False)
        if ("bottomleft" == btn):
            self.m.bottomleft = "X"
            self.bottomleft.setEnabled(False)
        if ("bottomright" == btn):
            self.m.bottomright = "X"
            self.bottomright.setEnabled(False)  

    @pyqtSlot()
    def randommove(self, playerpiece, movenum): #function for AI to complete random move
        #print("In random move function")
        selectedmove = "" #return variable
        movelist = [] #array of available moves

        if (self.m.topleft == ""):
            movelist.append("topleft")
        if (self.m.topmiddle == ""):
            movelist.append("topmiddle")
        if (self.m.topright == ""):
            movelist.append("topright")
        if (self.m.middleleft == ""):
            movelist.append("middleleft")
        if (self.m.middlemiddle == ""):
            movelist.append("middlemiddle")
        if (self.m.middleright == ""):
            movelist.append("middleright")
        if (self.m.bottomleft == ""):
            movelist.append("bottomleft")
        if (self.m.bottommiddle == ""):
            movelist.append("bottommiddle")
        if (self.m.bottomright == ""):
            movelist.append("bottomright")

        #print(movelist)

        fmove = random.randint(1,len(movelist)) #get random number
        selectedmove = movelist[fmove-1]        #from ran number select matching move
        print("Computer made move: " + selectedmove)

        if (selectedmove != ""): #diable selected button, update board in model
            if (selectedmove == "topleft"):
                self.m.topleft = self.otherplayer
                self.topleft.setEnabled(False)
            if (selectedmove == "topmiddle"):
                self.m.topmiddle = self.otherplayer
                self.topmiddle.setEnabled(False)
            if (selectedmove == "topright"):
                self.m.topright = self.otherplayer
                self.topright.setEnabled(False)
            if (selectedmove == "middleleft"):
                self.m.middleleft = self.otherplayer
                self.middleleft.setEnabled(False)
            if (selectedmove == "middlemiddle"):
                self.m.middlemiddle = self.otherplayer
                self.middlemiddle.setEnabled(False)
            if (selectedmove == "middleright"):
                self.m.middleright = self.otherplayer
                self.middleright.setEnabled(False)
            if (selectedmove == "bottomleft"):
                self.m.bottomleft = self.otherplayer
                self.bottomleft.setEnabled(False)
            if (selectedmove == "bottommiddle"):
                self.m.bottommiddle = self.otherplayer
                self.bottommiddle.setEnabled(False)
            if (selectedmove == "bottomright"):
                self.m.bottomright = self.otherplayer
                self.bottomright.setEnabled(False)

            self.AImoves[movenum - 1] = selectedmove #update move made in movelist

            return 1

        return 0


    @pyqtSlot()
    def canwincheck(self, playerpiece, num): #0 for check for yourself, 1 for check for other player      

        if (num == 0):
            if (playerpiece == "X"):
                otherplayerpiece = "O"
            else:
                otherplayerpiece = "X"
        if (num == 1):
            if (playerpiece == "X"):
                otherplayerpiece = "X"
                playerpiece = "O"
            else:
                otherplayerpiece = "O"
                playerpiece = "X"

        winspot = ""

        #if all pieces are not other players pieces, there is a potential for a win or a stop, get winspot
        if (self.m.topleft != otherplayerpiece and self.m.topmiddle != otherplayerpiece and self.m.topright != otherplayerpiece):
            if (self.m.topleft == playerpiece and self.m.topmiddle == playerpiece):
                winspot = "topright"
            if (self.m.topleft == playerpiece and self.m.topright == playerpiece):
                winspot = "topmiddle"
            if (self.m.topmiddle == playerpiece and self.m.topright == playerpiece):
                winspot = "topleft"
        
        if (self.m.middleleft != otherplayerpiece and self.m.middlemiddle != otherplayerpiece and self.m.middleright != otherplayerpiece):
            if (self.m.middleleft == playerpiece and self.m.middlemiddle == playerpiece):
                winspot = "middleright"
            if (self.m.middleleft == playerpiece and self.m.middleright == playerpiece):
                winspot = "middlemiddle"
            if (self.m.middlemiddle == playerpiece and self.m.middleright == playerpiece):
                winspot = "middleleft"

        if (self.m.bottomleft != otherplayerpiece and self.m.bottommiddle != otherplayerpiece and self.m.bottomright != otherplayerpiece):
            if (self.m.bottomleft == playerpiece and self.m.bottommiddle == playerpiece):
                winspot = "bottomright"
            if (self.m.bottomleft == playerpiece and self.m.bottomright == playerpiece):
                winspot = "bottommiddle"
            if (self.m.bottommiddle == playerpiece and self.m.bottomright == playerpiece):
                winspot = "bottomleft"

        if (self.m.topleft != otherplayerpiece and self.m.middleleft != otherplayerpiece and self.m.bottomleft != otherplayerpiece):
            if (self.m.topleft == playerpiece and self.m.middleleft == playerpiece):
                winspot = "bottomleft"
            if (self.m.topleft == playerpiece and self.m.bottomleft == playerpiece):
                winspot = "middleleft"
            if (self.m.middleleft == playerpiece and self.m.bottomleft == playerpiece):
                winspot = "topleft"

        if (self.m.topmiddle != otherplayerpiece and self.m.middlemiddle != otherplayerpiece and self.m.bottommiddle != otherplayerpiece):
            if (self.m.topmiddle == playerpiece and self.m.middlemiddle == playerpiece):
                winspot = "bottommiddle"
            if (self.m.topmiddle == playerpiece and self.m.bottommiddle == playerpiece):
                winspot = "middlemiddle"
            if (self.m.middlemiddle == playerpiece and self.m.bottommiddle == playerpiece):
                winspot = "topmiddle"

        if (self.m.topright != otherplayerpiece and self.m.middleright != otherplayerpiece and self.m.bottomright != otherplayerpiece):
            if (self.m.topright == playerpiece and self.m.middleright == playerpiece):
                winspot = "bottomright"
            if (self.m.topright == playerpiece and self.m.bottomright == playerpiece):
                winspot = "middleright"
            if (self.m.middleright == playerpiece and self.m.bottomright == playerpiece):
                winspot = "topright"

        if (self.m.topleft != otherplayerpiece and self.m.middlemiddle != otherplayerpiece and self.m.bottomright != otherplayerpiece):
            if (self.m.topleft == playerpiece and self.m.middlemiddle == playerpiece):
                winspot = "bottomright"
            if (self.m.topleft == playerpiece and self.m.bottomright == playerpiece):
                winspot = "middlemiddle"
            if (self.m.middlemiddle == playerpiece and self.m.bottomright == playerpiece):
                winspot = "topleft"

        if (self.m.topright != otherplayerpiece and self.m.middlemiddle != otherplayerpiece and self.m.bottomleft != otherplayerpiece):
            if (self.m.topright == playerpiece and self.m.middlemiddle == playerpiece):
                winspot = "bottomleft"
            if (self.m.topright == playerpiece and self.m.bottomleft == playerpiece):
                winspot = "middlemiddle"
            if (self.m.middlemiddle == playerpiece and self.m.bottomleft == playerpiece):
                winspot = "topright"

        #check what value gotten from winspot, make move there
        if (winspot != ""):
            if (winspot == "topleft"):
                self.m.topleft = self.otherplayer
                self.topleft.setEnabled(False)
            if (winspot == "topmiddle"):
                self.m.topmiddle = self.otherplayer
                self.topmiddle.setEnabled(False)
            if (winspot == "topright"):
                self.m.topright = self.otherplayer
                self.topright.setEnabled(False)
            if (winspot == "middleleft"):
                self.m.middleleft = self.otherplayer
                self.middleleft.setEnabled(False)
            if (winspot == "middlemiddle"):
                self.m.middlemiddle = self.otherplayer
                self.middlemiddle.setEnabled(False)
            if (winspot == "middleright"):
                self.m.middleright = self.otherplayer
                self.middleright.setEnabled(False)
            if (winspot == "bottomleft"):
                self.m.bottomleft = self.otherplayer
                self.bottomleft.setEnabled(False)
            if (winspot == "bottommiddle"):
                self.m.bottommiddle = self.otherplayer
                self.bottommiddle.setEnabled(False)
            if (winspot == "bottomright"):
                self.m.bottomright = self.otherplayer
                self.bottomright.setEnabled(False)
            
            self.AImoves[self.movenumber-1] = winspot
            print("Computer made move: " + str(self.AImoves[self.movenumber-1]))
            #print(self.AImoves)

            return 1

        return 0

    @pyqtSlot()
    def updateboard(self): #updates board from model
        self.topleft.setText(str(self.m.topleft))
        self.topmiddle.setText(str(self.m.topmiddle))
        self.topright.setText(str(self.m.topright))
        self.middleleft.setText(str(self.m.middleleft))
        self.middlemiddle.setText(str(self.m.middlemiddle))
        self.middleright.setText(str(self.m.middleright))
        self.bottomleft.setText(str(self.m.bottomleft))
        self.bottommiddle.setText(str(self.m.bottommiddle))
        self.bottomright.setText(str(self.m.bottomright))

        return

    @pyqtSlot()
    def clearboard(self): #clears the entire board and variables, also sets up which user starts next game
            self.playagain = False
            self.m.topleft = ""
            self.m.topmiddle = ""
            self.m.topright = "" 
            self.m.middleleft = "" 
            self.m.middlemiddle = "" 
            self.m.middleright = "" 
            self.m.bottomleft = "" 
            self.m.bottommiddle = "" 
            self.m.bottomright = "" 

            self.topleft.setEnabled(True)
            self.topmiddle.setEnabled(True)
            self.topright.setEnabled(True)
            self.middleleft.setEnabled(True)
            self.middlemiddle.setEnabled(True)
            self.middleright.setEnabled(True)
            self.bottomleft.setEnabled(True)
            self.bottommiddle.setEnabled(True)
            self.bottomright.setEnabled(True)

            self.movenumber = 0
            self.updateboard()

            for i in range(9):
                self.AImoves[i] = None

            print("~ * ~ NEW GAME ~ * ~")
            self.gofirst()
            self.refresh()

    @pyqtSlot()
    def reset(self): #sets all win, lose and tie text fields to zero
        self.m.wins = 0 
        self.m.losses = 0
        self.m.ties = 0

        self.refresh() #refesh to update text
        self.clearboard()#clears board

        return

    @pyqtSlot() #wont be able to test for a while
    def giveup(self): #checks if all spaces are empty while giveup button is pressed, if not, wont increment a loss
        if (self.playagain == True): #if playagain is true, that means "playagain" text is on current button
                                     #and we want it to habe different behavior than normal.
            self.clearboard()        #clear the board
            self.giveupbutton.setText("Give Up") #reset giveup button text.

        else:
            if (self.m.topleft == "" and
                self.m.topmiddle == "" and
                self.m.topright == "" and
                self.m.middleleft == "" and
                self.m.middlemiddle == "" and
                self.m.middleright == "" and
                self.m.bottomleft == "" and
                self.m.bottommiddle == "" and
                self.m.bottomright == ""):

                self.refresh()
                return

            else:
                self.clearboard() #else, actually give up
                self.m.losses += 1 #increment losses

        self.refresh() #refresh to update text
        return

    @pyqtSlot()
    def rules(self):
        self.ruleswindow()
        self.refresh() #refresh to update text
        return

    def ruleswindow(self):
        addDialog = rule_window(self.m)
        if addDialog.exec():
            return(True)
        return False
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec_())