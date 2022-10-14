# The game of WAR is rather simple as it requires  only the ability to recognize which of two cards has a higher value.
# In this game the value of cards from lowest to highest is:
# 2,3,4,5,6,7,8,9,10,J,Q,K,A
# No suit has a higher value than another.
# Both players take the top card off of their pile (stack) and place it face up in the playing area. 
# The player that played the higher card wins the round and takes both cards. 
# If there is a tie, then both players place the next card down and the 3rd  card up. 
# The winner of the 3rd card wins the round. If the 3rd cards tie, then both players repeat the process until a player has won the hand. 
# When the player runs out of cards, then the player will shuffle the cards from the winning pile (stack). 
# The game will continue until one play player is completely out cards.

#importing pygame into the program
import pygame
from pygame.locals import *
import random

from tkinter import*

pygame.init() # initialize 
pygame.font.init()

# GLOBAL VARIABLES 
clock = pygame.time.Clock() #setting a pygame clock variable to set a framerate for the game
frameRate = 60 #frameRate = Frames per second
screenWidth, screenHeight = 1000, 600   # setting the variables for the screen width and height
font = pygame.font.SysFont('timesnewroman', 36) # setting game fonts
warTimeFont = pygame.font.SysFont('timesnewroman', 200)
countdownFont = pygame.font.SysFont('timesnewroman', 50)

screenDisplay = pygame.display.set_mode((screenWidth, screenHeight))#creating a display screenDisplay at the set width and height

pygame.display.set_caption('WAR GAME!') # set the title for window

gamePlay = 0 # check if user clicked a button, if they started a round or shuffle card
clickedButton = False
roundStart = True
shuffledCard = False

colorWhite = (255,255,255) # defining the different color variables and their levels
colorBlk = (0,0,0)
colorYllw = (255,255,0)
colorBlue = (0,0,255)
colorGrn = (0,255,0)
colorRed = (255,0,0)

mainMenu = True # check if program in in main menu

# setting the images to variables and using the convert_alpha() to make it more smooth
playBackgroundImg = pygame.image.load('greenPokerTable.jpg').convert_alpha()
menuBackgroundImg = pygame.image.load('greenPokerTable.jpg').convert_alpha()
titleImg = pygame.image.load('cardsLogo.png').convert_alpha()
singlePlayerImg = pygame.image.load('startBtn.png').convert_alpha()
singlePlayerHover = pygame.image.load('startBtnHover.png').convert_alpha()
contImg = pygame.image.load('continueBtn.png').convert_alpha()
contImgHover = pygame.image.load('continueBtnHover.png').convert_alpha()
mainMenuImg = pygame.image.load('mainMenuBtn.png').convert_alpha()
mainMenuImgHover = pygame.image.load('mainMenuBtnHover.png').convert_alpha()
mainMenuImg = pygame.transform.scale(mainMenuImg,(309,103)).convert_alpha()
mainMenuImgHover = pygame.transform.scale(mainMenuImgHover,(309,103)).convert_alpha()
cardBackImg = pygame.image.load('BACK.png').convert_alpha()
cardBackImg = pygame.transform.scale(cardBackImg,(150, 200))
warPileImg = pygame.image.load('warGamePile.png').convert_alpha()
AceCardImg =  pygame.image.load('1CARD.png').convert_alpha()
AceCardImg = pygame.transform.scale(AceCardImg,(150, 200))
sevenCardImg =  pygame.image.load('7CARD.png').convert_alpha()
sevenCardImg = pygame.transform.scale(sevenCardImg,(150, 200))
kingCardImg =  pygame.image.load('13CARD.png').convert_alpha()
kingCardImg = pygame.transform.scale(kingCardImg,(150, 200))
jackCardImg =  pygame.image.load('11CARD.png').convert_alpha()
jackCardImg = pygame.transform.scale(jackCardImg,(150, 200))

# creating a function that makes the text on the coord plane
def drawText(text, font, text_col, x, y,):    
    img = font.render(text, True, text_col)  # set variable to render
    screenDisplay.blit(img, (x, y)) # draw the text on the screen
    
class menuButton(): # class to run the menu button

    def __init__(self, x, y, image): # function creates button

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clickedButton = False
 
    def drawCard(self, image, image2):  # function checks for cursor collision
        action = False # return the action 
        mousePos = pygame.mouse.get_pos() # variable to set the mouse pos
        if self.rect.collidepoint(mousePos):
            #if the mouse is on the button, set the image to the hover image
            self.image = image 

            #checks if the mouse is clickedButton and if it isnt already clickedButton
            if pygame.mouse.get_pressed()[0] == 1 and self.clickedButton == False:
                action = True # sets the action to return and that the mouse has been clickedButton as true
                self.clickedButton = True
        
        else: #if mouse if not over button, it will then set the image to the original button image unaltered
            self.image = image2        

        if pygame.mouse.get_pressed()[0] == 0:    #checks if the mouse isn't pressed
            #sets the click variable as false so the computer knows its not pressed
            self.clickedButton = False
        
        screenDisplay.blit(self.image, self.rect) # draw button
        return action # return action 

def roundCountDown(gamePlay): # function to show round countdown
    def gameOverLay(): # function to overlay the game
    
        screenDisplay.blit(pygame.transform.scale(playBackgroundImg,(screenWidth,screenHeight)), (0,0))  # draws the overlay over the game
        screenDisplay.blit(mainMenuImg, (20,475))

        drawText("Round "+str(roundCounter), countdownFont, colorWhite, 40, 20) # draws the countdown number
        drawText('Player 1 Cards: ' +str(len(playerOneDeck)), font, colorBlk, 380, 40) # draws the player one text

        if gamePlay == 1:  # if else to see if user picks single and multiplayer,if 1 then single player
            drawText('Computer Cards: ' +str(len(playerTwoDeck)), font, colorBlk, 360, 540) # draw information for computer
        drawText("Press A to flip", font, colorWhite, 695, 30)

        screenDisplay.blit(pygame.transform.scale(warPileImg,(150, 200)), (100,200))     
        # draw card to left of display
        screenDisplay.blit(pygame.transform.scale(cardBackImg,(150, 200)), (700,70))   # draw deck on the right of display
        screenDisplay.blit(pygame.transform.scale(cardBackImg,(150, 200)), (700,332))

        if len(warPile) > 0: # if statement to see if war file has cards
            screenDisplay.blit(pygame.transform.scale(cardBackImg,(150, 200)), (100,200))

    # run overlay function
    gameOverLay()
    screenDisplay.blit(mainMenuImg, (20,475))
    # display countdown
    drawText("3", countdownFont, colorWhite, 440, 240)
    
   
    pygame.display.update() # update screen
    pygame.time.delay(1000) # set delay
    
    gameOverLay()
    screenDisplay.blit(mainMenuImg, (20,475))

    # draw countdown 2 after the 3
    drawText("2", countdownFont, colorWhite, 480, 240)
    
    pygame.display.update() # update the display for 2
    pygame.time.delay(1000) # time delay
    
    gameOverLay()
    
    drawText("1", countdownFont, colorWhite, 520, 240) # draw countdown for 1 again
    
    pygame.display.update() # update display for countdown 
    pygame.time.delay(1000) #  time delay
    
    gameOverLay()
    screenDisplay.blit(mainMenuImg, (20,475))

    drawText("FLIP!", countdownFont, colorWhite, 435, 290)  # draw for FLIP
    
    pygame.display.update() # update display for flip
    pygame.time.delay(1000)

    gameOverLay()
    screenDisplay.blit(mainMenuImg, (20,475))
    
    if gamePlay == 1: # if one then single player bot

        for x1 in range(0,14): # loop to run through all cards
            if playerTwoDeck[0] == x1:
                screenDisplay.blit(pygame.transform.scale(pygame.image.load(str(x1)+'CARD.png'),(150, 200)), (420,320)) # draw on display
    pygame.display.update()

def shuffleDeck(): # function to shuffle deck
        for x in range(0,52):    # for loop to go through each index and swap it with a random num
            rand = random.randint(x,51) # create random number from x to end
            tempValue = gameDeck[x]     # set temp value
            gameDeck[x] = gameDeck[rand] # set gamedeck at x to rand
            gameDeck[rand] = tempValue  
            # set gamedeck at rand to a temporary value
                                
        # for loop to start from 0 to 26
        for x in range(0,26):
            playerOneDeck.append(gameDeck[2 * x]) # add even number to player 1
            playerTwoDeck.append(gameDeck[2 * x + 1]) # add odd number to player 2

def handCalc(roundCounter, roundStart): # function to handle calculations
    if flippedPileOne[0] > flippedPileTwo[0]: # if statement to check if p1 > p2 pile
        drawText("Round "+str(roundCounter)+" Winner", font, colorGrn, 380, 160) # draws round winner on the screen 
        pygame.display.update()
        pygame.time.delay(2000)
        playerOneDeck.append(flippedPileOne[0]) # adds the cards to Player 1's deck from Player 2
        playerOneDeck.append(flippedPileTwo[0])

        if len(warPile) > 0:  # if statement to check if any card in warpile
            for x3 in range(0,len(warPile)):  # for loop to add all cards from the war pile to Player1's deck
                playerOneDeck.append(warPile[0])  
                warPile.remove(warPile[0]) # remove card from pile
        
        roundCounter += 1 # increment round counter by 1
        roundStart = True # set to true

    if flippedPileOne[0] < flippedPileTwo[0]: # if statement to check if p1 < p2 flipped
        drawText("Round "+str(roundCounter)+" Winner", font, colorGrn, 380, 380) # draw round winner on screen
        pygame.display.update()
        pygame.time.delay(2000)
       
        playerTwoDeck.append(flippedPileOne[0])  # adds the cards to p2s deck from  p1
        playerTwoDeck.append(flippedPileTwo[0])

        if len(warPile) > 0: #checks if there were any cards in the war pile to add
            for x3 in range(0,len(warPile)):
                playerTwoDeck.append(warPile[0])  #adds all cards from the war pile to Player 2's deck
                warPile.remove(warPile[0])

        roundCounter += 1 # increment round counter
        roundStart = True # set round to true
    
    if flippedPileOne[0] == flippedPileTwo[0]: # if statement to check for ties

        drawText("WAR TIME!","impact", colorRed, 140, 160) # draw war time when tied over screen
        pygame.display.update()
        pygame.time.delay(2000)

        warPile.append(flippedPileOne[0]) # add cards from flippedfile and deck to war pile
        warPile.append(flippedPileTwo[0])
        warPile.append(playerOneDeck[0])
        warPile.append(playerTwoDeck[0])
     
        playerOneDeck.remove(playerOneDeck[0]) # remove card from players deck
        playerTwoDeck.remove(playerTwoDeck[0])

        roundCounter += 1
        roundStart = True

    flippedPileOne.remove(flippedPileOne[0]) # remove card from flipped pile
    flippedPileTwo.remove(flippedPileTwo[0])

    return roundStart, roundCounter # returns these values

def handleKeyPress(clickedButton, gamePlay): # function that Handles the key input 
    if gamePlay == 1: # if else statement to check if single or multi, if 1 then single 
        keyPressed = pygame.key.get_pressed()

        # if statement to check if A was presssed, if a button pressed pile
        if keyPressed[pygame.K_a] and clickedButton == False and len(flippedPileOne) == 0:
            for x1 in range(1,14): # loop through 13 cards
                if playerOneDeck[0] == x1:
                    screenDisplay.blit(pygame.transform.scale(pygame.image.load(str(x1)+'CARD.png'),(150, 200)), (420,90))
                    pygame.display.update()

            flippedPileOne.append(playerOneDeck[0]) # move player card to flipped card pile
            playerOneDeck.remove(playerOneDeck[0])
            flippedPileTwo.append(playerTwoDeck[0])
            playerTwoDeck.remove(playerTwoDeck[0])

            clickedButton = True # set button to true
        
        # else if to check button released
        elif keyPressed[pygame.K_a]:

            # set button to False so the user can play another card next round when it is their turn
            clickedButton = False

def instructionsWindow(gamePlay, mainMenu): # function for instruction window
    
    if contBtn.drawCard(contImgHover, contImg):
        gamePlay = 0
        mainMenu = False

    return gamePlay, mainMenu

gameDeck = [] # lists to hold cards
warPile = []
flippedPileOne = []
flippedPileTwo = []

for x in range(1,14): # loop to add the 14 cards
    for z in range(0,4): # loop to add the 4 suits
        gameDeck.append(x)

singlePlayerBtn = menuButton(340, 220, singlePlayerImg) # creating buttons and giving directions with images
contBtn = menuButton(345, 475, contImg)
mainMenuBtn = menuButton(20,475, mainMenuImg)
cardBtnOne = menuButton(75, 75, cardBackImg)
cardBtnTwo = menuButton(75, 350, cardBackImg)
cardBtnThree = menuButton(775, 75, cardBackImg)
cardBtnFour = menuButton(775, 350, cardBackImg)

runGame = True # set rungame to true 
while runGame == True:
    if gamePlay == 0: # runs if gameplay is 0
        screenDisplay.blit(pygame.transform.scale(menuBackgroundImg,(screenWidth,screenHeight)), (0,0)) # print background and other information
        screenDisplay.blit(pygame.transform.scale(titleImg,(400,130)), (310,40))

        mainMenu = True  
        shuffledCard = False
        roundCounter = 1
        clickedButton = False
        roundStart = True

    elif gamePlay == 1: # else if statement to run single player mode
        if mainMenuBtn.drawCard(mainMenuImgHover, mainMenuImg):
            gamePlay = 0

        if shuffledCard == False:
            playerOneDeck = [] # create the card decks for players
            playerTwoDeck = []
            shuffleDeck() # shuffle function
            shuffledCard = True # set to true

        if roundCounter < 101: # checks rounds to prevent game going on too long

            if len(playerTwoDeck) != 52 or len(playerTwoDeck) != 52: # check if deck has 52 cards
            
                    if roundStart == True: # check new round
                        roundCountDown(gamePlay) # countdown called
                        roundStart = False # stops it

                    # if statement to check both players haven't flipped their card
                    if len(flippedPileOne) == 0 and len(flippedPileTwo) == 0 or len(flippedPileOne) == 1 and len(flippedPileTwo) == 0 or len(flippedPileOne) == 0 and len(flippedPileTwo) == 1:
                        handleKeyPress(clickedButton, gamePlay) # checks for button presses to flip cards
                    
                    if len(flippedPileOne) == 1 and len(flippedPileTwo) == 1: # if statement to check if both flipped
                        roundStart, roundCounter = handCalc(roundCounter, roundStart) # function to see who won
        else: # else statment for if the game goes over 100

            screenDisplay.blit(pygame.transform.scale(playBackgroundImg,(screenWidth,screenHeight)), (0,0))
            drawText("Game End","impact", colorRed, 150, 140)
            if playerOneDeck > playerTwoDeck:
                drawText("Player 1 Won!", "timesnewroman", colorGrn, 420, 370)
            if playerOneDeck < playerTwoDeck:
                drawText("Computer Won!", "timesnewroman", colorGrn, 420, 370)
            pygame.display.update()
            pygame.time.delay(5000)
            gamePlay = 0 # gamePlay to 0, user to main menu
         
            
    if mainMenu == True: # if mainMenu is true

        cardBtnOne.drawCard(AceCardImg, cardBackImg) # show card front and back
        cardBtnTwo.drawCard(sevenCardImg, cardBackImg)
        cardBtnThree.drawCard(kingCardImg, cardBackImg)
        cardBtnFour.drawCard(jackCardImg, cardBackImg)

        if singlePlayerBtn.drawCard(singlePlayerHover, singlePlayerImg): # if the singleplayer button was pressed
        
            mainMenu = False # end main menu
            gamePlay = 1 # gameplay to 1 for single
            pygame.time.delay(100)
            screenDisplay.blit(pygame.transform.scale(playBackgroundImg,(screenWidth,screenHeight)), (0,0)) # draws the background image to remove the menu images

    for event in pygame.event.get():   # if the player quit the game           
        if event.type == pygame.QUIT:
            runGame = False

    clock.tick(frameRate) # set fps for game
    pygame.display.update()
       
pygame.quit() # closes the game
