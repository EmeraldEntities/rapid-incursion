########################################################
# Title:    incursionClasses
#
# Joseph Wang : ICS20G : 21-12-2018
#
# Details: All the classes needed for Rapid Incursion.
########################################################
import pygame, textwrap, time
from math import sqrt, sin, cos, pi, atan2, degrees
from random import randint, randrange

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.mixer.set_num_channels(16)

#-- FUNCTIONS FOR VARIABLES --#
def createFont(font, size):
    #creates a new font
    newFont = pygame.font.SysFont(font, size)
    return newFont

def loadImage(image, locationInImages):
    #loads an image and converts it
    newImage = pygame.image.load("assets/"+locationInImages+"/"+image).convert()
    return newImage

def loadImageTransparent(image, locationInImages):
    #loads a transparent image and converts it
    newImage = pygame.image.load("assets/"+locationInImages+"/"+image).convert_alpha()
    return newImage

def drawNormalText(font, text, colour):
    textSurface = font.render(text, True, colour)
    return textSurface

def loadSound(sound):
    newSound = pygame.mixer.Sound("assets/sounds/" + sound)
    newSound.set_volume(0.5)
    return newSound

def loadMusic(music):
    #loads music
    pygame.mixer.music.load("assets/sounds/music/" + music)
    pygame.mixer.music.play(-1)    

##-- CONSTANTS--##
# These will be used for referencing.
GOLD = 0
WOOD = 1
STONE = 2
DIRT = 3
CHECKPOINT = 4
TENT = 5
STRONGHOLD = 6
cost = [GOLD, WOOD, STONE]

STRENGTH = 3
COOLDOWN = 4
HP = 5
DEFENSE = 6
SPEED = 7
RANGE = 8
stats = [STRENGTH, COOLDOWN, HP, DEFENSE]

WALK = 0
ATTACK = 1
IDLE = 2
JUMP = 3

LEFT = 0
RIGHT = 1

OUTLINE = 0
WIDTH = 800
HEIGHT = 600
CENTER = 400
GROUND = 450
GRAVITY = 2
TOP = 0
TILESIZE = 100
BUILDING_HEIGHT = 200
TOWER_HEIGHT = 300
BUILD_BUTTON_HEIGHT = 515
UNIT_HEIGHT = GROUND - 50
PLAYER_HEIGHT = GROUND - 100
MIN_ORIGIN_X = -1000
MAX_ORIGIN_X = 1000
DEFAULT_STRONGHOLDX = 3000
DEFAULT_TENTX = 0

RED   = (255,  0,  0)
BLACK = (  0,  0,  0)
WHITE = (255,255,255)

gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))

##-- The many image imports used for this game --##
gameBackground = loadImage("backgroundSize.png", "images")
unitImage = loadImage("unit.png", "images")
playerImage = loadImage("test.png", "images")
frontBackdrop = loadImage("backdrop1.png", "images")
backBackdrop = loadImage("backdrop2.png", "images")
groundImage = loadImage("ground.png", "images")
skyImage = loadImage("sky.png", "images")

#- NPC imports
minionImage = loadImage("minion.png", "images/npcs")
overseerImage = loadImage("overseer.png", "images/npcs")
tankwalkerImage = loadImage("tankwalker.png", "images/npcs")
rogueImage = loadImage("rogue.png", "images/npcs")
astralImage = loadImage("astral.png", "images/npcs")
marksmanImage = loadImage("marksman.png", "images/npcs")
spearmanImage = loadImage("spearman.png", "images/npcs")
horsemanImage = loadImage("horseman.png", "images/npcs")

#- General imports
tentImage = loadImageTransparent("tent.png", "images")
strongholdImage = loadImageTransparent("stronghold.png", "images")
bushesImage = loadImageTransparent("bushes.png", "images")
treesImage = loadImageTransparent("trees.png", "images")
rockPileImage = loadImageTransparent("rockPile.png", "images")
goldPileImage = loadImageTransparent("goldPile.png", "images")
checkpointFlagImage = loadImageTransparent("checkpointFlag.png", "images")
bottomBushesImage = loadImageTransparent("bottomBushes.png", "images")
descriptionBoxImage = loadImageTransparent("descriptionBox.png", "images")

#- Tower imports
gunmanHideout1 = loadImageTransparent("gunmanHideout.png", "images/towers")
gunmanHideout2 = loadImageTransparent("gunmanHideout2.png", "images/towers")
gunmanHideout3 = loadImageTransparent("gunmanHideout3.png", "images/towers")
gunmanHideout4 = loadImageTransparent("gunmanHideout4.png", "images/towers")
gunmanHideoutB1 = loadImageTransparent("gunmanHideoutB1.png", "images/towers")
gunmanHideoutB2 = loadImageTransparent("gunmanHideoutB2.png", "images/towers")
gunmanHideoutB3 = loadImageTransparent("gunmanHideoutB3.png", "images/towers")
sharpshooterDen1 = loadImageTransparent("sharpshooterDen.png", "images/towers")
sharpshooterDen2 = loadImageTransparent("sharpshooterDen2.png", "images/towers")
sharpshooterDen3 = loadImageTransparent("sharpshooterDen3.png", "images/towers")
sharpshooterDen4 = loadImageTransparent("sharpshooterDen4.png", "images/towers")
sharpshooterDenB1 = loadImageTransparent("sharpshooterDenB1.png", "images/towers")
sharpshooterDenB2 = loadImageTransparent("sharpshooterDenB2.png", "images/towers")
sharpshooterDenB3 = loadImageTransparent("sharpshooterDenB3.png", "images/towers")
fastshotTower1 = loadImageTransparent("fastshotTower.png", "images/towers")
fastshotTower2 = loadImageTransparent("fastshotTower2.png", "images/towers")
fastshotTower3 = loadImageTransparent("fastshotTower3.png", "images/towers")
fastshotTower4 = loadImageTransparent("fastshotTower4.png", "images/towers")
fastshotTowerB1 = loadImageTransparent("fastshotTowerB1.png", "images/towers")
fastshotTowerB2 = loadImageTransparent("fastshotTowerB2.png", "images/towers")
fastshotTowerB3 = loadImageTransparent("fastshotTowerB3.png", "images/towers")
gteDefender1 = loadImageTransparent("gteDefender.png", "images/towers")
gteDefender2 = loadImageTransparent("gteDefender2.png", "images/towers")
gteDefender3 = loadImageTransparent("gteDefender3.png", "images/towers")
gteDefender4 = loadImageTransparent("gteDefender4.png", "images/towers")
gteDefenderB1 = loadImageTransparent("gteDefenderB1.png", "images/towers")
gteDefenderB2 = loadImageTransparent("gteDefenderB2.png", "images/towers")
gteDefenderB3 = loadImageTransparent("gteDefenderB3.png", "images/towers")
outpost1 = loadImageTransparent("outpost.png", "images/towers")
outpost2 = loadImageTransparent("outpost2.png", "images/towers")
outpost3 = loadImageTransparent("outpost3.png", "images/towers")
outpostB1 = loadImageTransparent("outpostB1.png", "images/towers")
outpostB2 = loadImageTransparent("outpostB2.png", "images/towers")
outpostB3 = loadImageTransparent("outpostB3.png", "images/towers")

gunmanHideoutImages = [gunmanHideout1, gunmanHideout2, gunmanHideout3, gunmanHideout4]
gunmanHideoutBImages = [gunmanHideoutB1, gunmanHideoutB2, gunmanHideoutB3, gunmanHideout1]
sharpshooterDenBImages = [sharpshooterDenB1, sharpshooterDenB2, sharpshooterDenB3, sharpshooterDen1]
sharpshooterDenImages = [sharpshooterDen1, sharpshooterDen2, sharpshooterDen3, sharpshooterDen4]
fastshotTowerBImages = [fastshotTowerB1, fastshotTowerB2, fastshotTowerB3, fastshotTower1]
fastshotTowerImages = [fastshotTower1, fastshotTower2, fastshotTower3, fastshotTower4]
gteDefenderImages = [gteDefender1, gteDefender2, gteDefender3, gteDefender4]
gteDefenderBImages = [gteDefenderB1, gteDefenderB2, gteDefenderB3, gteDefender1]
outpostBImages = [outpostB1, outpostB2, outpostB3, outpost1]
outpostImages = [outpost1, outpost2, outpost3]

#- Icon imports
goldImage = loadImageTransparent("goldOre.png", "images/icons")
woodImage = loadImageTransparent("wood.png", "images/icons")
stoneImage = loadImageTransparent("rock.png", "images/icons")
crosshair = loadImageTransparent("crosshair.png", "images/icons")
axe = loadImageTransparent("axe.png", "images/icons")
pick = loadImageTransparent("pick.png", "images/icons")
playerBullet = loadImageTransparent("goodBullet.png", "images/icons")
towerBullet = loadImageTransparent("towerBullet.png", "images/icons")
enemyBullet = loadImageTransparent("badBullet.png", "images/icons")
pickToolIndicator = loadImageTransparent("pickToolIndicator.png", "images/icons")
axeToolIndicator = loadImageTransparent("axeToolIndicator.png", "images/icons")
rifleToolIndicator = loadImageTransparent("rifleToolIndicator.png", "images/icons")
selectionIndicator = loadImageTransparent("selectionIndicator.png", "images/icons")

#- Button imports
gunmanButtonImage = loadImage("gunmanTower.png", "images/buttons")
sharpshooterButtonImage = loadImage("sharpshooterTower.png", "images/buttons")
fastshotButtonImage = loadImage("fastshotTower.png", "images/buttons")
gteButtonImage = loadImage("gteDefender.png", "images/buttons")
outpostButtonImage = loadImage("outpost.png", "images/buttons")
swordsmanButtonImage = loadImage("swordsman.png", "images/buttons")
spearmanButtonImage = loadImage("spearman.png", "images/buttons")
marksmanButtonImage = loadImage("marksman.png", "images/buttons")
horsemanButtonImage = loadImage("horseman.png", "images/buttons")

playButtonImage = loadImage("playButton.png", "images/buttons")
playButtonSImage = loadImage("playButtonSelect.png", "images/buttons")
controlsButtonImage = loadImage("controlsButton.png", "images/buttons")
controlsButtonSImage = loadImage("controlsButtonSelect.png", "images/buttons")
creditsButtonImage = loadImage("creditsButton.png", "images/buttons")
creditsButtonSImage = loadImage("creditsButtonSelect.png", "images/buttons")
tutorialButtonImage = loadImage("tutorialButton.png", "images/buttons")
tutorialButtonSImage = loadImage("tutorialButtonSelect.png", "images/buttons")
easyButtonImage = loadImage("easyButton.png", "images/buttons")
easyButtonSImage = loadImage("easyButtonSelect.png", "images/buttons")
mediumButtonImage = loadImage("mediumButton.png", "images/buttons")
mediumButtonSImage = loadImage("mediumButtonSelect.png", "images/buttons")
hardButtonImage = loadImage("hardButton.png", "images/buttons")
hardButtonSImage= loadImage("hardButtonSelect.png", "images/buttons")

iconImage = loadImageTransparent("rapidIncursionLogo.png", "images/icons")

#- Screen imports
titleScreenImage = loadImage("titleScreen.png", "images/title")
controls1Image = loadImage("instructions1.png", "images/title")
controls2Image = loadImage("instructions2.png", "images/title")
creditsImage = loadImage("credits.png", "images/title")
tutorial1Image = loadImage("tutorialPage1.png", "images/title")
tutorial2Image = loadImage("tutorialPage2.png", "images/title")
tutorial3Image = loadImage("tutorialPage3.png", "images/title")
tutorial4Image = loadImage("tutorialPage4.png", "images/title")
winScreenImage = loadImage("victoryScreen.png", "images/title")
loseScreenImage = loadImage("gameOverScreen.png", "images/title")

#- Fonts
comicSans10 = createFont("Comic Sans MS", 10)
comicSans12 = createFont("Comic Sans MS", 12)
proximaNova20 = createFont("Proxima Nova", 20)

#- Sound database
harvestSound1 = loadSound("harvestSound1.wav")
harvestSound2 = loadSound("harvestSound2.wav")
harvestSound3 = loadSound("harvestSound3.wav")
gunshotSound = loadSound("gunshot.wav")
upgradeSound = loadSound("upgradeSound.wav")
walkSound = loadSound("walkSound.wav")
buildSound = loadSound("buildSound.wav")
finishedBuildingSound = loadSound("finishedBuilding.wav")
attackSound1 = loadSound("attack.wav")
attackSound2 = loadSound("attack2.wav")
attackSound3 = loadSound("attack3.wav")
gmhoAttack = loadSound("gunmanHideout.wav")
ssdAttack = loadSound("sharpshooterDen.wav")
fstAttack = loadSound("fastshotTower.wav")
gteAttack = loadSound("gteDefender.wav")

#- Music
battleTheme = 'Pulse.ogg'
mainTheme = 'Tintantin.ogg'

waveSound = loadSound("upgradeWave.wav")
enemySpawnSound = loadSound("enemySpawn.wav")
friendlySpawnSound = loadSound("friendlySpawn.wav")

attackSounds = [attackSound1, attackSound2, attackSound3]
harvestSounds = [harvestSound1, harvestSound2, harvestSound3]

#- General variables that will be referenced later
backgroundRect = gameBackground.get_rect()
backgroundW = backgroundRect.width
DEFAULT_ORIGINX = 350
originX = DEFAULT_ORIGINX
movementDirection = None

groundRelToPlayer = 0
previousGroundRel = groundRelToPlayer
playerX = 50

FPS = 60

##-- TOWER COSTS --##
towerTypes = ["Gunman Hideout", "Sharpshooter Den", "Fast-shot Tower", "GTE Defender", "Outpost"]
unitTypes = ["Swordsman", "Spearman", "Horseman",  "Marksman"]

gunmanStats = [float(line.rstrip("\n")) for line in open("assets/towers/stats/gunmanHideout.txt", "r")]
sharpshooterStats = [float(line.rstrip("\n")) for line in open("assets/towers/stats/sharpshooterDen.txt", "r")]
fastshotStats = [float(line.rstrip("\n")) for line in open("assets/towers/stats/fastshotTower.txt", "r")]
gteStats = [float(line.rstrip("\n")) for line in open("assets/towers/stats/gteDefender.txt", "r")]
outpostStats = [float(line.rstrip("\n")) for line in open("assets/towers/stats/outpost.txt", "r")]

swordsmanStats = [float(line.rstrip("\n")) for line in open("assets/units/stats/swordsman.txt", "r")]
spearmanStats = [float(line.rstrip("\n")) for line in open("assets/units/stats/spearman.txt", "r")]
marksmanStats = [float(line.rstrip("\n")) for line in open("assets/units/stats/marksman.txt", "r")]
horsemanStats = [float(line.rstrip("\n")) for line in open("assets/units/stats/horseman.txt", "r")]

minionStats = [float(line.rstrip("\n")) for line in open("assets/enemies/stats/minion.txt", "r")]
overseerStats = [float(line.rstrip("\n")) for line in open("assets/enemies/stats/overseer.txt", "r")]
tankwalkerStats = [float(line.rstrip("\n")) for line in open("assets/enemies/stats/tankwalker.txt", "r")]
rogueStats = [float(line.rstrip("\n")) for line in open("assets/enemies/stats/rogue.txt", "r")]
astralStats = [float(line.rstrip("\n")) for line in open("assets/enemies/stats/astral.txt", "r")]
   ###############
###-- FUNCTIONS --###
   ###############

def calcDistance(x1, x2, y1, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

##-- BUTTONS--##
class Button(object):
    def __init__(self, x, y, picture = None, selectedPicture = None, unit = None, window = None, difficulty = None):
        self.destX = x
        self.destY = y
        self.picture = picture
        self.pictureS = selectedPicture
        self.unitToMake = unit
        self.destWindow = window
        self.difficulty = difficulty
        self.buttonRect = self.picture.get_rect()

    def drawPicture(self, selected = False):
        """ (bool) -> None
            Blits the image onto the window
        """
        if selected:
            pictureRect = gameWindow.blit(self.pictureS, (self.destX, self.destY))
        else:
            pictureRect = gameWindow.blit(self.picture, (self.destX, self.destY))

        self.buttonRect = pictureRect

    def isInside(self):
        """ (None) -> None
            Checks if the mouse is inside the button
        """
        return self.buttonRect.collidepoint(pygame.mouse.get_pos())

    def performHoverAction(self, unit, textLocation, statsLocation, x):
        """ (str, str, str, int) -> None
            Makes a description box above the area needed to be described, gets text
            and blits it.
        """
        text, tidbit = self._determineDescriptionText(textLocation, unit)
        gameWindow.blit(descriptionBoxImage, (x, BUILD_BUTTON_HEIGHT-200))
        
        #- Make the text fit into the box
        adjustedText = textwrap.fill(text, 25)
        descriptionText = adjustedText.split("\n")
        
        tidbitAdjusted = textwrap.fill(tidbit, 35)
        tidbitText = tidbitAdjusted.split("\n")
        
        lineY = BUILD_BUTTON_HEIGHT-190
        x = x + 5
        
        #- Blits every line
        for line in descriptionText:
            textSurface = drawNormalText(proximaNova20, line, WHITE)
            gameWindow.blit(textSurface, (x, lineY))
            lineY = lineY + 15
            
        lineY = lineY + 15
        
        for line in tidbitText:
            tidbitSurface = drawNormalText(comicSans10, line, WHITE)
            gameWindow.blit(tidbitSurface, (x, lineY))
            lineY = lineY + 15
            
        lineY = BUILD_BUTTON_HEIGHT - 40
        
        #- Blits the cost of the items
        unitStats = [float(line.rstrip("\n")) for line in open(statsLocation + "/" + unit + ".txt", "r")]
        cost = unitStats[GOLD:STONE+1]

        for resource in range(len(cost)):
            if resource == GOLD:
                gameWindow.blit(goldImage, (x, lineY))
            elif resource == WOOD:
                gameWindow.blit(woodImage, (x, lineY))
            else:
                gameWindow.blit(stoneImage, (x, lineY))
            x = x + 15
            costText = drawNormalText(comicSans12, ":" + str(int(cost[resource])), WHITE)
            gameWindow.blit(costText, (x, lineY))
            x = x + 35
                            
    def _determineDescriptionText(self, folder, unit):
        """ (str, str) -> str, str
            Gets text from a text file at a specified folder, and returns the text and the tidbit
        """
        with open(folder+"/" + unit + ".txt", "r") as textInFile:
            allText = textInFile.readlines()
            text = allText[0]
            tidbit = allText[1]
        return text, tidbit

#- Creating lists of buttons so that they can be referenced later        
towerButtonList = [
    Button(25 , BUILD_BUTTON_HEIGHT, picture = gunmanButtonImage, unit = "gunmanHideout"),
    Button(125, BUILD_BUTTON_HEIGHT, picture = sharpshooterButtonImage, unit = "sharpshooterDen"),
    Button(225, BUILD_BUTTON_HEIGHT, picture = fastshotButtonImage, unit = "fastshotTower"),
    Button(325, BUILD_BUTTON_HEIGHT, picture = gteButtonImage, unit = "gteDefender"),
    Button(425, BUILD_BUTTON_HEIGHT, picture = outpostButtonImage, unit = "outpost")
]

unitButtonList = [
    Button(25 , BUILD_BUTTON_HEIGHT, picture = swordsmanButtonImage, unit = "swordsman"),
    Button(125, BUILD_BUTTON_HEIGHT, picture = spearmanButtonImage, unit = "spearman"),
    Button(225, BUILD_BUTTON_HEIGHT, picture = horsemanButtonImage, unit = "horseman"),
    Button(325, BUILD_BUTTON_HEIGHT, picture = marksmanButtonImage, unit = "marksman"),
]

resourceIcons = [goldImage, woodImage, stoneImage]

##-- TIMER --##
class Timer(object):
    def __init__(self, disregardDuration, timerDuration):
        self.startTime = int(round(time.time() * 1000))
        self.durationTime = timerDuration
        self.bypassCheck = disregardDuration

    def __str__(self):
        return self.startTime, self.durationTime

    def timeLeft(self):
        #- Checks how much time is left
        currentTime = int(round(time.time() * 1000))
        elapsed = currentTime - self.startTime
        if elapsed >= self.durationTime:
            return 0
        return self.durationTime - elapsed
    
    def durationComplete(self):
        #- Checks if the timer is up
        currentTime = int(round(time.time() * 1000))
        elapsed = currentTime - self.startTime
        if self.bypassCheck or elapsed >= self.durationTime:
            self.bypassCheck = False
            return True
        return False

    def reset(self):
        #- Resets timer
        self.startTime = int(round(time.time() * 1000))
    
    def adjustDurationTime(self, newDurationTime):
        #- Adjusts the duration time of the timer
        self.durationTime = newDurationTime

##-- PROJECTILES --##
class Projectiles(pygame.sprite.Group):
    def __init__(self):
        pygame.sprite.Group.__init__(self)
        
class Bullet(pygame.sprite.Sprite):
    def __init__(self, magnitude, velocity, x, y, originPerson, bulletType, xAndY2):
        pygame.sprite.Sprite.__init__(self)
        self.vectorX = 0
        self.vectorY = 0
        self.vectorAngle = 0
        self.MAGNITUDE = magnitude
        self.VELOCITY = velocity
        self.objectX = x
        self.objectY = y
        self.origin = originPerson
        self.originType = originPerson.allegiance
        self.bulletType = bulletType
        
        self.hitbox = bulletType.get_rect()
        self.hitboxW = self.hitbox.width
        self.hitboxH = self.hitbox.height
        self.hitboxX = self.objectX
        self.hitboxY = self.objectY
        self.bulletRect = pygame.Rect(self.hitboxX, self.hitboxY, self.hitboxW, self.hitboxH)

        self.bulletType = bulletType

        #- The mathy part, calculates the bullet angle
        if (xAndY2[0] - self.objectY) == 0:
            self.objectY = self.objectY + 1
        self.slope = (xAndY2[1] - self.objectY) / (xAndY2[0] - self.objectY)

        self.objectAngle = degrees(atan2(xAndY2[1] - self.objectY, xAndY2[0] - self.objectX))

    def collides(self, bulletEnemies, npcs, player):
        #- Checks for collision with any npc
        for unit in npcs:
            if self.bulletRect.colliderect(unit.hitboxRect) and unit.allegiance == bulletEnemies:
                self.target = unit
                return True
        return False

    def inflictDamage(self):
        #- Deals damage to the target specified
        self.target.hp = self.target.hp - round(self.origin.strength / self.target.defense, 2)
        
    def move(self):
        #- Move the bullet according to the angle specified
        self.objectX = self.objectX + round(self.VELOCITY*cos(self.objectAngle*pi/180))
        self.objectY = self.objectY + round(self.VELOCITY*sin(self.objectAngle*pi/180))

    def draw(self):
        #- Blits the bullet location on screen
        self.hitboxX = self.objectX
        self.hitboxY = self.objectY
        self.bulletRect = pygame.Rect(self.hitboxX, self.hitboxY, self.hitboxW, self.hitboxH)
        gameWindow.blit(self.bulletType, (self.objectX, self.objectY))

##-- TITLE -- ##
class Title(object):
    def __init__(self):
        self.playButton = Button(510, 50, picture = playButtonImage, selectedPicture = playButtonSImage, window = "difficultySelector")
        self.tutorialButton = Button(510, 175, picture = tutorialButtonImage, selectedPicture = tutorialButtonSImage, window = "tutorial")
        self.controlsButton = Button(510, 300, picture = controlsButtonImage, selectedPicture = controlsButtonSImage, window = "controls")
        self.creditsButton = Button(510, 425, picture = creditsButtonImage, selectedPicture = creditsButtonSImage, window = "credits") 
        self.titleButtons = [self.playButton, self.tutorialButton, self.controlsButton, self.creditsButton]
 
    def drawTitleWindow(self):
        """ (None) -> None
            Blits the title window onto the screen.
        """
        pygame.event.clear()
        gameWindow.blit(titleScreenImage, (0,0))
        for button in self.titleButtons:
            if button.isInside():
                button.drawPicture(True)
            else:
                button.drawPicture()

        pygame.display.update()

    def checkForMouseInteraction(self):
        #- Checks if mouse is inside a button
        window = "title"
        for button in self.titleButtons:
            if button.isInside():
                window = button.destWindow
        return window

class DificultySelector(object):
    def __init__(self):
        self.easyButton = Button(510, 50, picture = easyButtonImage, selectedPicture = easyButtonSImage, window = "game", difficulty = "easy")
        self.mediumButton = Button(510, 175, picture = mediumButtonImage, selectedPicture = mediumButtonSImage, window = "game", difficulty = "medium")
        self.hardButton = Button(510, 300, picture = hardButtonImage, selectedPicture = hardButtonSImage, window = "game", difficulty = "hard")

        self.difficultyButtons = [self.easyButton, self.mediumButton, self.hardButton]
    
    def drawDifficultiesWindow(self):
        """ (None) -> None
            Blits the difficulty window onto the screen.
        """
        pygame.event.clear()
        gameWindow.blit(titleScreenImage, (0,0))
        for button in self.difficultyButtons:
            if button.isInside():
                button.drawPicture(True)
            else:
                button.drawPicture()

        pygame.display.update()
    
    def checkForDifficultySelection(self, game):
        #- Checks if mouse is inside a button
        window = "difficultySelector"
        gameToReset = False
        for button in self.difficultyButtons:
            if button.isInside():
                window = "game"
                game.difficulty = button.difficulty
                gameToReset = True
        return window, gameToReset

class Credits(object):
    def __init__(self):
        self.creditsImage = creditsImage

    def drawCreditsWindow(self):
        """ (None) -> None
            Blits the credits window onto the screen.
        """
        pygame.event.clear()
        gameWindow.blit(self.creditsImage, (0,0))

        pygame.display.update()
    
class Controls(object):
    def __init__(self):
        self.allControlPages = [controls1Image, controls2Image]
        self.currentPage = 0
        self.MAX_PAGES = 2

    def drawControlsWindow(self):
        """ (None) -> None
            Blits the controls window onto the screen.
        """
        pygame.event.clear()
        gameWindow.blit(self.allControlPages[self.currentPage], (0,0))

        pygame.display.update()

    def performControlsChange(self):
        #- Makes sure that if the next page doesn't exist, the player is sent back to title
        window = "controls"
        self.currentPage = self.currentPage + 1
        if (self.currentPage + 1) > self.MAX_PAGES:
            window = "title"
            self.currentPage = 0
        return window

class Tutorial(object):
    def __init__(self):
        self.tutorialImages = [tutorial1Image, tutorial2Image, tutorial3Image, tutorial4Image]
        self.currentPage = 0
        self.MAX_PAGES = 4
    
    def drawTutorialWindow(self):
        """ (None) -> None
            Blits the tutorial window onto the screen.
        """
        pygame.event.clear()
        gameWindow.blit(self.tutorialImages[self.currentPage], (0,0))

        pygame.display.update()

    def changeTutorialPage(self):
        #- Makes sure that if the next page doesn't exist, the player is sent back to title
        window = "tutorial"
        self.currentPage = self.currentPage + 1
        if (self.currentPage + 1) > self.MAX_PAGES:
            window = "title"
            self.currentPage = 0
        return window

##-- GAME --##
class Game(object):
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.openBuildMenu = False
        self.openUnitMenu = False
        self.difficulty = "medium"
        self.level = 1
        self.unitLimit = 10
    
    def resetGame(self, originX, player, playerX, npcs, units, enemies):
        #- Resets game
        originX = DEFAULT_ORIGINX
        self.openBuildMenu = False
        self.openUnitMenu = False
        if self.difficulty == "easy":
            startSpawnSpeed = 30000
            startLevelTimer = 120000
        elif self.difficulty == "medium":
            startSpawnSpeed = 12000
            startLevelTimer = 60000
        elif self.difficulty == "hard":
            startSpawnSpeed = 4000
            startLevelTimer = 40000
        self.spawnSpeed = startSpawnSpeed
        self.spawnTimer = Timer(False, self.spawnSpeed)
        self.levelTimer = Timer(False, startLevelTimer)
        self.level = 1
        self.unitLimit = 10
        loadMusic(battleTheme)
        player.inventory = {GOLD: 150, WOOD: 150, STONE: 150}
        player.dead = False
        player.hp = 1000
        playerX = 50 
        units = 0
        enemies = 0
        for npc in npcs:
            npc.kill()
        tiles, tilemap = self.generateNewTilemap()
        return originX, playerX, npcs, units, enemies, tiles, tilemap

    def generateNewTilemap(self):
        """ (None) -> None
            Generates a questionably fair tilemap system for the game. This will include
            at least 1 Wood tile, 1 Stone tile and 1 Gold tile in the player section of the game.
        """
        balancedGen = False
        while not balancedGen:
            originX = DEFAULT_ORIGINX - 350
            tiles = []
            tilemap = [DIRT for tile in range(0, backgroundW, TILESIZE)]
            for tile in range(len(tilemap)):
                randomNumGen = randint(0,30)
                if tile == 9 or tile == 19:
                    if tile == 9:
                        checkpointNumber = 1
                    else:
                        checkpointNumber = 2
                    tilemap[tile] = CHECKPOINT
                    if randomNumGen <= 8:
                        tiles.append(Checkpoint("Wood", WOOD, 2000, checkpointNumber, originX))
                    elif randomNumGen > 8 and randomNumGen <= 16:
                        tiles.append(Checkpoint("Stone", STONE, 2000, checkpointNumber, originX))
                    elif randomNumGen > 16 and randomNumGen <= 25:
                        tiles.append(Checkpoint("Gold", GOLD, 2500, checkpointNumber, originX))
                    else:
                        tiles.append(Checkpoint("Nothing", DIRT, 0, checkpointNumber, originX))
                elif randomNumGen <= 6:
                    tilemap[tile] = WOOD
                    tiles.append(Tile("Wood", WOOD, 1500, originX))
                elif randomNumGen > 6 and randomNumGen <= 12:
                    tilemap[tile] = STONE
                    tiles.append(Tile("Stone", STONE, 1500, originX))
                elif randomNumGen > 12 and randomNumGen <= 18:
                    tilemap[tile] = GOLD
                    tiles.append(Tile("Gold", GOLD, 2000, originX))
                else:
                    tiles.append(Tile("Dirt", DIRT, 0, originX))
                originX = originX + 100
            
            tiles.pop(29)
            tiles.pop(0)
            tilemap.pop(29)
            tilemap.pop(0)
            tiles.insert(0, Tent(DEFAULT_ORIGINX - 350))
            tiles.append(Stronghold(originX))
            tilemap.insert(0, TENT)
            tilemap.append(STRONGHOLD)
            
            playerSegment = tilemap[:9]
                
            balancedGen = True
            
            if not (GOLD in playerSegment):
                balancedGen = False
            if not (STONE in playerSegment):
                balancedGen = False
            if not (WOOD in playerSegment):
                balancedGen = False
        return tiles, tilemap

    def increaseLevel(self):
        #- Increases the unit spawn and the spawnrate according to level
        if self.levelTimer.durationComplete():
            self.level = self.level + 1
            self.levelTimer.reset()
            if not (self.spawnSpeed - self.level*1000) - 500 <= 0:
                self.spawnTimer.adjustDurationTime(self.spawnSpeed - self.level*1000)
                waveSound.play()

    def redrawWindow(self, player, originX, groundRelToPlayer, mousePos, projectiles, npcs, tiles):
        """(object, int, int, tuple, object, object, list) -> None
            Redraws everything that needs to be drawn in the game.
        """
        pygame.event.clear()
        gameWindow.blit(skyImage, (0,0))
        gameWindow.blit(frontBackdrop, (originX-350, 0))
        gameWindow.blit(backBackdrop, (originX+backgroundW, 0))

        refOriginX = originX
        
        for tile in tiles:   #- Draws the generic background pictures
            gameWindow.blit(bushesImage, (originX, GROUND-100))
            gameWindow.blit(groundImage, (originX, GROUND))
            pygame.draw.line(gameWindow, BLACK, (originX, 0), (originX, 600), 1)
                
            originX = originX + 100
        pygame.draw.line(gameWindow, BLACK, (originX, 0), (originX, 600), 1)

        originX = refOriginX
        
        for tile in tiles:  #- Draws all the tiles, and everything on it
            if (tile.tile == "Wood" or tile.bonus == "Wood") and tile.resourceAmount > 0:
                gameWindow.blit(treesImage, (originX-50, GROUND-BUILDING_HEIGHT))
            elif (tile.tile == "Stone" or tile.bonus == "Stone") and tile.resourceAmount > 0:
                gameWindow.blit(rockPileImage, (originX-50, GROUND-BUILDING_HEIGHT))
            elif (tile.tile == "Gold" or tile.bonus == "Gold") and tile.resourceAmount > 0:
                gameWindow.blit(goldPileImage, (originX-50, GROUND-BUILDING_HEIGHT))
                
            if tile.tile == "Checkpoint":
                gameWindow.blit(checkpointFlagImage, (originX, 0))
            elif tile.tile == "Tent":
                gameWindow.blit(tentImage, (originX-100, GROUND-BUILDING_HEIGHT))
            elif tile.tile == "Stronghold":
                gameWindow.blit(strongholdImage, (originX, GROUND-BUILDING_HEIGHT))
        
            if tile.hasTower:
                tile.tower.draw(originX, GROUND-TOWER_HEIGHT)
            
            if tile.tower == player.selectedTower:
                gameWindow.blit(selectionIndicator, (originX, GROUND-TOWER_HEIGHT))

            originX = originX + 100

        for tile in range(0, WIDTH+200, 100):
            gameWindow.blit(bottomBushesImage, (tile - groundRelToPlayer, GROUND+50))

        player.draw()   #- Draws the player

        for unit in npcs:   #- Updates all unit hitboxes
            unit.updateHitbox() 
            unit.draw()

        if self.openBuildMenu:   #- Draws the build menu if it is activated
            pygame.draw.rect(gameWindow, BLACK, (0, 500, WIDTH, 100), 0)
            self._performTowerButtonActions()
            
        if self.openUnitMenu:   #- Draws the unit menu if it is activated
            pygame.draw.rect(gameWindow, BLACK, (0, 500, WIDTH, 100), 0)
            self._performUnitButtonActions()

        for bullet in projectiles:   #- Draws every bullet
            bullet.draw()

        pygame.draw.rect(gameWindow, BLACK, (10, 10, 100, 20), 0)   #- Draw the health bar
        pygame.draw.rect(gameWindow, RED, (10, 10, player.hp / 10, 20), 0)
        if player.dead:
            deadText = drawNormalText(proximaNova20, "DEAD.", RED)
            gameWindow.blit(deadText, (25,14))

        resourceReference = -1
        invX = 500
        for item in player.inventory.values():  #- Draws the inventory
            resourceReference = resourceReference + 1
            itemAmount = drawNormalText(proximaNova20, str(item), BLACK)
            gameWindow.blit(resourceIcons[resourceReference], (invX, 10))
            invX = invX + 15
            gameWindow.blit(itemAmount, (invX, 10))
            invX = invX + 75

        self._drawToolIndicator(player)
        self._checkForMousePic(player, mousePos)
        pygame.display.update()

    def updateClock(self, fps):
        #- Updates the clock
        self.clock.tick(fps)

    def endGame(self, tent, stronghold):
        #- If the game ends, see who won
        window = "game"
        if stronghold.hp <= 0:
            self.victor = "player"
            window = "gameEnd"
            pygame.mouse.set_visible(True)
        elif tent.hp <= 0:
            self.victor = "enemy"
            window = "gameEnd"
            pygame.mouse.set_visible(True)
        else:
            inPlay = True
        return window

    def _performTowerButtonActions(self):
        #- Draws every picture in the tower button list
        for button in towerButtonList:
            button.drawPicture()
            if self.checkIfInsideButton(button):
               button.performHoverAction(button.unitToMake, "assets/towers/descriptions", "assets/towers/stats", button.destX) 
                
        buttonTextX = 25
        for text in towerTypes:
            textSurface = drawNormalText(comicSans10, text, WHITE)
            gameWindow.blit(textSurface, (buttonTextX, 575))
            buttonTextX = buttonTextX + 100

    def _performUnitButtonActions(self):
        #- Draws every unit in the unit button list
        for button in unitButtonList:
            button.drawPicture()
            if self.checkIfInsideButton(button):
               button.performHoverAction(button.unitToMake, "assets/units/descriptions", "assets/units/stats", button.destX) 

        buttonTextX = 25
        for text in unitTypes:
            textSurface = drawNormalText(comicSans10, text, WHITE)
            gameWindow.blit(textSurface, (buttonTextX, 575))
            buttonTextX = buttonTextX + 100

    def checkIfInsideButton(self, button):
        #- Checks if mouse is inside button
        if button.isInside():
            return True
        return False

    def checkIfCanAfford(self, player, cost):
        #- Checks to see if the player can afford something
        if player.inventory[GOLD] >= cost[GOLD] and player.inventory[STONE] >= cost[STONE] and player.inventory[WOOD] >= cost[WOOD]:
            return True
        return False

    def _checkForMousePic(self, player, mousePos):
        #- Adjusts the mouse pic
        if self.openBuildMenu or self.openUnitMenu:
            pygame.mouse.set_visible(True)
        elif player.currentTool == "Rifle":
            pygame.mouse.set_visible(False)
            gameWindow.blit(crosshair, (mousePos[0] - 15, mousePos[1] - 15))
        elif player.currentTool == "Pick":
            pygame.mouse.set_visible(False)
            gameWindow.blit(pick, (mousePos[0] - 15, mousePos[1] - 15))
        elif player.currentTool == "Axe":
            pygame.mouse.set_visible(False)
            gameWindow.blit(axe, (mousePos[0] - 15, mousePos[1] - 15))

    def _drawToolIndicator(self, player):
        #- Draws the tool indicator at the top
        if player.currentTool == "Pick":
            gameWindow.blit(pickToolIndicator, (350, 0))
        elif player.currentTool == "Axe":
            gameWindow.blit(axeToolIndicator, (350, 0))
        elif player.currentTool == "Rifle":
            gameWindow.blit(rifleToolIndicator, (350, 0))

    def adjustTileX(self, tile, playerX):
        #- Adjusts the tile according to player X
        tile.x = tile.x - playerX
        
##-- STRUCTURES --##
class Structures(pygame.sprite.Group):
    def __init__(self):
        pygame.sprite.Group.__init__(self)
        
class Tower(pygame.sprite.Sprite):                                                 #Gunman's hideout, Sharpshooter den, Fast-shot tower, GTE Defenders, Outpost
    def __init__(self, towerType, tStats, towerX, tile): 
        pygame.sprite.Sprite.__init__(self)
        self.canAttackFlying = False
        self.canAttackGround = True

        #- Costs
        self.buildCost = [tStats[GOLD], tStats[WOOD], tStats[STONE]]
        self.stageCost = []
        for resource in range(len(self.buildCost)):
            self.stageCost.append(self.buildCost[resource]/4)
        self.upgradeCost = []
        for resource in range(len(self.stageCost)):
            self.upgradeCost.append(self.stageCost[resource]*3)
        self.totalCost = self.stageCost[:]

        #- Stats
        self.stats = gunmanStats
        self.DEFAULT_STRENGTH = tStats[STRENGTH]
        self.strength = self.DEFAULT_STRENGTH
        self.DEFAULT_COOLDOWN = tStats[COOLDOWN]
        self.cooldown = self.DEFAULT_COOLDOWN
        self.DEFAULT_HP = tStats[HP]
        self.attackRange = tStats[RANGE]
        self.hp = self.DEFAULT_HP
        self.towerX = towerX
        self.x = WIDTH/2
        self.towerType = towerType
        self.tile = tile

        #- Build Status
        self.level = 0
        self.buildStatus = 0
        self.upgradeStats = [self.strength/2, self.cooldown/2, self.hp/2]
        self.MAX_BUILD_LEVELS = 3
        self.MAX_UPGRADE_LEVELS = 3
        self.finishedBuilding = False
        self.maxLevel = False

        self.allegiance = "good"
        self.type = "tower"
        self.cooldownTimer = Timer(True, self.cooldown * 1000)
                       
    def _attack(self, other):
        #- Deals damage to another entity
        damage = float(self.strength) / float(other.defense)
        other.hp = other.hp - damage
        self.attackSound.play()

    def calculateAction(self, npcs, enemies, projectiles):   
        """(object, int, object) -> None
            Checks if there is an enemy within range. If so, attacks it.
        """
        for npc in npcs:
            if npc.allegiance == "bad":
                if (not npc.flying and self.canAttackGround) or (npc.flying and self.canAttackFlying) :
                    if calcDistance(self.x, npc.x, TOWER_HEIGHT + 100, npc.y) <= self.attackRange:
                        if self.cooldownTimer.durationComplete():
                            self._attack(npc)
                            self.cooldownTimer.reset()

    def build(self, player):
        """(object) -> None
            Builds the selected tower, assuming that it can be built.
        """
        self.buildStatus = self.buildStatus + 1
        for resource in cost:
            player.inventory[resource] = player.inventory[resource] - self.stageCost[resource]
        buildSound.play()
        if self.buildStatus == self.MAX_BUILD_LEVELS:
            self.finishedBuilding = True
            finishedBuildingSound.play()

    def upgrade(self, player):
        """(object) -> None
            Upgrades the selected tower, assuming that it can still be upgraded.
        """
        self.level = self.level + 1
        for resource in cost:
            player.inventory[resource] = player.inventory[resource] - self.upgradeCost[resource]
            self.totalCost[resource] = self.totalCost[resource] + self.upgradeCost[resource] 
        self.strength = self.strength + (self.DEFAULT_STRENGTH/2)
        self.hp = self.hp + (self.DEFAULT_HP/2)
        upgradeSound.play()
        if self.level == self.MAX_UPGRADE_LEVELS:
            self.maxLevel = True
    
    def sell(self, player):
        """(object) -> None
            Sells the selected tower for a somewhat fair price.
        """
        if self.finishedBuilding:
            for resource in cost:
                player.inventory[resource] = player.inventory[resource] + (self.totalCost[resource] - (200 * (self.level/2)))
            self.kill()
            self.tile.hasTower = False
            self.tile.towerType = None
            player.selectedTower = "No Tower"
    
    def draw(self, x, y):
        #- Draws the tower onto the screen
        if self.finishedBuilding:
            gameWindow.blit(self.builtImages[self.level], (x, y))
        else:
            gameWindow.blit(self.buildingImages[self.buildStatus], (x, y))

class GunmanHideout(Tower): #- Defines Gunman Hideout
    def __init__(self, towerType, tStats, towerX, tile):
        Tower.__init__(self, towerType, tStats, towerX, tile)
        self.builtImages = gunmanHideoutImages
        self.buildingImages = gunmanHideoutBImages
        self.attackSound = gmhoAttack
        
class SharpshooterDen(Tower): #- Defines Sharpshooter Den
    def __init__(self, towerType, tStats, towerX, tile):
        Tower.__init__(self, towerType, tStats, towerX, tile)
        self.canAttackFlying = True
        self.builtImages = sharpshooterDenImages
        self.buildingImages = sharpshooterDenBImages
        self.attackSound = ssdAttack

class FastshotTower(Tower): #- Defines Fastshot Tower
    def __init__(self, towerType, tStats, towerX, tile):
        Tower.__init__(self, towerType, tStats, towerX, tile)
        self.builtImages = fastshotTowerImages
        self.buildingImages = fastshotTowerBImages
        self.attackSound = fstAttack

class GTEDefender(Tower): #- Defines GTE Defender
    def __init__(self, towerType, tStats, towerX, tile):
        Tower.__init__(self, towerType, tStats, towerX, tile)
        self.canAttackFlying = True
        self.canAttackGround = False
        self.builtImages = gteDefenderImages
        self.buildingImages = gteDefenderBImages
        self.attackSound = gteAttack

class Outpost(Tower): #- Defines Outpost tower
    def __init__(self, towerType, tStats, towerX, tile, tiles):
        Tower.__init__(self, towerType, tStats, towerX, tile)
        self.MAX_UPGRADE_LEVELS = 2
        self.currentTileRef = self.towerX // 100
        self.currentTile = tiles[self.currentTileRef]
        self.canAttackGround = False
        self.canAttackFlying = False
        self.builtImages = outpostImages
        self.buildingImages = outpostBImages
        self.healAmount = 20

    def upgrade(self, player):
        #- Changes the upgrade function to this one, as the Outpost does not attack units.
        self.level = self.level + 1
        for resource in cost:
            player.inventory[resource] = player.inventory[resource] - self.upgradeCost[resource]
        if self.currentTile.tile != "Nothing":
            self.currentTile.resourceAmount = self.currentTile.resourceAmount + 500
        self.healAmount = self.healAmount + 20
        upgradeSound.play()
        if self.level == self.MAX_UPGRADE_LEVELS:
            self.maxLevel = True

##-- PLAYER --##

class Player(object):
    def __init__(self, playerClass):
        #- Player stats
        self.playerClass = playerClass
        self.strength = 550
        self.defense = 5
        self.cooldown = 2
        self.DEFAULT_SPEED = 7
        self.DEFAULT_JUMPSPEED = -25
        self.weapon = "Rifle"
        self.playerImage = playerImage

        #- Spritesheet loads
        self.idleSS = [loadImageTransparent("playerIdleL.png", "images/player"), loadImageTransparent("playerIdle.png", "images/player")]
        self.attackingSS = [loadImageTransparent("playerAttackL.png", "images/player"), loadImageTransparent("playerAttack.png", "images/player")]
        self.walkingSS = [loadImageTransparent("playerRunL.png", "images/player"), loadImageTransparent("playerRun.png", "images/player")]
        self.jumpingSS = [loadImageTransparent("playerJumpL.png", "images/player"), loadImageTransparent("playerJump.png", "images/player")]
        self.numOfImages = [8, 6, 4, 1]
        self.MAXHP = 1000
        self.hp = self.MAXHP
        self.healTimer = Timer(True, 2000)
        self.invincibleTimer = Timer(True, 2000)
        self.speed = self.DEFAULT_SPEED
        self.jumpspeed = self.DEFAULT_JUMPSPEED
        self.playerStep = self.speed
        self.miningCooldown = 1
        self.x = WIDTH/2
        self.y = PLAYER_HEIGHT
        self.Vy = 0

        #- Player tools
        self.tools = ["Pick", "Axe", self.weapon]
        self.selectedTool = 0
        self.currentTool = self.tools[self.selectedTool]
        self.inventory = {GOLD: 150, WOOD: 150, STONE: 150}
        self.selectedTower = "No Tower"
        
        self.dead = False
        self.allegiance = "good"

        #- Player hitbox
        self.hitbox = self.playerImage.get_rect()
        self.hitboxW = self.hitbox.width
        self.hitboxH = self.hitbox.height
        self.hitboxX = self.x
        self.hitboxY = self.y

        self.hitboxRect = pygame.Rect(self.hitboxX, self.hitboxY, self.hitboxW, self.hitboxH)

        self.playerDeadImage = loadImageTransparent("playerDead.png", "images/player")
        self.index = 0
        self.isAttacking = False
        self._loadSprites()
    
    def _loadSprites(self):
        #- Defines the spritesheets and loads all important information
        self.spritesheets = [self.walkingSS, self.attackingSS, self.idleSS, self.jumpingSS]
        self.sheetRect = [[item.get_rect() for item in self.walkingSS], [item.get_rect() for item in self.attackingSS], 
                            [item.get_rect() for item in self.idleSS], [item.get_rect()for item in self.jumpingSS]]
        self.sheetWidth = [[sheet.width for sheet in self.sheetRect[WALK]], [sheet.width for sheet in self.sheetRect[ATTACK]] , 
                            [sheet.width for sheet in self.sheetRect[IDLE]] , [sheet.width for sheet in self.sheetRect[JUMP]]]
        self.facing = RIGHT
        self.selectedSheet = IDLE
        self.rectDelay = Timer(True, 100)
        self.rect = self.spritesheets[self.selectedSheet][self.facing].get_rect()
        self.rect.width = self.sheetWidth[self.selectedSheet][self.facing] / self.numOfImages[self.selectedSheet]
        self.switchedSpritesheet = True
        self.isAttacking = False
        self.updateSprite()
        
    def updateSprite(self):
        #- Updates the sprites
        self.imageSelected = self.spritesheets[self.selectedSheet][self.facing]
        self.rect = pygame.Rect(self.x, self.y, self.rect.width, self.sheetRect[self.selectedSheet][self.facing].height)
        self.imageSelected.set_clip(self.rect.width * self.index, 0, self.rect.width, self.rect.height)
        self.image = self.imageSelected.subsurface(self.imageSelected.get_clip())
    
    def loadNextImage(self):
        #- Loads the next image in the spritesheet
        if self.rectDelay.durationComplete():
            if (self.index + 2) % self.numOfImages[self.selectedSheet] == 0 and self.isAttacking:
                self.isAttacking = False
            
            self.index = (self.index + 1) % self.numOfImages[self.selectedSheet]     
            self.rectDelay.reset()
        self.updateSprite()

    def resetSpritesheet(self):
        #- Resets the spritesheet and gets the new one
        self.index = 0
        self.rect = self.spritesheets[self.selectedSheet][self.facing].get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.rect.width = self.sheetWidth[self.selectedSheet][self.facing] / self.numOfImages[self.selectedSheet] 

    def findCurrentTile(self, playerX, tiles):
        #- Finds the tile relative to the player
        self.currentTileRef = (playerX + 25)//100
        self.currentTile = tiles[self.currentTileRef]
    
    def draw(self):
        #- Blits the player images on
        self.hitboxX = self.x
        self.hitboxY = self.y
        self.hitboxRect = pygame.Rect(self.hitboxX, self.hitboxY, self.hitboxW, self.hitboxH)
        if not self.dead:
            gameWindow.blit(self.image, self.rect)
            self.loadNextImage()
        else:
            gameWindow.blit(self.playerDeadImage, (self.x-25, self.y))

    def move(self, originX, playerX, backgroundW, movementDirection, keys, groundRelToPlayer, previousGroundRel, npcs, structures):
        #- Actually moves the player when the move keys are pressed
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) or (keys[pygame.K_RIGHT] or keys[pygame.K_d]):
            if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and originX < 350:   #- If moving left
                self.selectedTower = "No Tower"
                if movementDirection == "Right":
                    groundRelToPlayer = previousGroundRel
                movementDirection = "Left"
                self.facing = LEFT
                for npc in npcs:
                    npc.x = npc.x + self.playerStep
                for tower in structures:
                    tower.x = tower.x + self.playerStep
                originX = originX + self.playerStep
                playerX = playerX - self.playerStep
                if not keys[pygame.K_RIGHT] and not keys[pygame.K_d]:
                    groundRelToPlayer = groundRelToPlayer - self.playerStep
                if groundRelToPlayer <= 0:
                    groundRelToPlayer = 200
                
            if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and originX - 450 > -backgroundW:   #- If moving right
                self.selectedTower = "No Tower"
                if movementDirection == "Left":
                    groundRelToPlayer = previousGroundRel
                movementDirection = "Right"
                self.facing = RIGHT
                for npc in npcs:
                    npc.x = npc.x - self.playerStep
                for tower in structures:
                    tower.x = tower.x - self.playerStep
                originX = originX - self.playerStep
                playerX = playerX + self.playerStep
                if not keys[pygame.K_LEFT] and not keys[pygame.K_a]:
                    groundRelToPlayer = groundRelToPlayer + self.playerStep
                if groundRelToPlayer >= 200:
                    groundRelToPlayer = 0

            #- Reset spritesheets if needed
            if self.selectedSheet != WALK:
                self.switchedSpritesheet = True
                
            if self.switchedSpritesheet and not self.isAttacking:
                self.selectedSheet = WALK
                self.resetSpritesheet()

        else:
            if self.selectedSheet != IDLE:
                self.switchedSpritesheet = True

            if self.switchedSpritesheet and not self.isAttacking:
                self.selectedSheet = IDLE
                self.resetSpritesheet()
        #- Checks for jumping as that is also moving
        if (keys[pygame.K_UP] or keys[pygame.K_SPACE] or keys[pygame.K_w]) and self.y + 100 >= GROUND:
            if self.selectedSheet != JUMP:
                self.switchedSpritesheet = True
            if self.switchedSpritesheet and not self.isAttacking:
                self.selectedSheet = JUMP
                self.resetSpritesheet()

            self.Vy = self.jumpspeed
        previousGroundRel = groundRelToPlayer
        self.Vy = self.Vy + GRAVITY
        self.y = self.y + self.Vy
        #- Resets the player to the ground level if it reaches it
        if self.y + 100 >= GROUND:
            self.y = GROUND - 100
            self.Vy = 0
        if self.switchedSpritesheet:
            self.switchedSpritesheet = False
        return originX, playerX, movementDirection, groundRelToPlayer, previousGroundRel

    def regenHealth(self):
        #- Heals the player if the player is on a built outpost
        if not self.dead and self.currentTile.hasTower and (self.currentTile.tower.towerType == "outpost" 
                                                            and self.currentTile.tower.finishedBuilding):
            if self.healTimer.durationComplete():
                self.hp = self.hp + self.currentTile.tower.healAmount
                if self.hp >= self.MAXHP:
                    self.hp = self.MAXHP
                self.healTimer.reset()

    def buildTower(self, towerType, playerX, structures, tiles):
        """(str, int, object, list) -> None
            Builds a selected tower if the player can afford it
        """
        if not self.currentTile.hasTower and self.currentTile.tile != "Tent" and (self.currentTile.tile != "Checkpoint" or towerType == "outpost"):
            tStats = [float(line.rstrip("\n")) for line in open("assets/towers/stats/"+towerType+".txt", "r")]
            #- Checks if the player has the resources needed
            if self.inventory[GOLD] >= (tStats[GOLD]/4) and self.inventory[WOOD] >= (tStats[WOOD]/4) and self.inventory[STONE] >= (tStats[STONE]/4):                
                self.currentTile.hasTower = True
                self.currentTile.towerType = towerType
                if towerType == "gunmanHideout":
                    self.currentTile.tower = GunmanHideout(towerType, tStats, playerX, self.currentTile)
                elif towerType == "sharpshooterDen":
                    self.currentTile.tower = SharpshooterDen(towerType, tStats, playerX, self.currentTile)
                elif towerType == "fastshotTower":
                    self.currentTile.tower = FastshotTower(towerType, tStats, playerX, self.currentTile)
                elif towerType == "gteDefender":
                    self.currentTile.tower = GTEDefender(towerType, tStats, playerX, self.currentTile)
                elif towerType == "outpost": 
                    self.currentTile.tower = Outpost(towerType, tStats, playerX, self.currentTile, tiles)
                structures.add(self.currentTile.tower)
                buildSound.play()
                self.selectedTower = self.currentTile.tower
                #- Removes items from player inventory
                for resource in [GOLD, WOOD, STONE]:
                    self.inventory[resource] = self.inventory[resource] - self.currentTile.tower.stageCost[resource]
    
    def recruitUnit(self, unitType, originX, playerX, units, npcs):
        """(str, int, object, int, object) -> None
            Recruits a specified unit if the player can afford it
        """
        #- Recruits specific units
        uStats = [float(line.rstrip("\n")) for line in open("assets/units/stats/"+unitType+".txt", "r")]
        if self.inventory[GOLD] >= uStats[GOLD] and self.inventory[WOOD] >= uStats[WOOD] and self.inventory[STONE] >= uStats[STONE]:
            if unitType == "swordsman":
                npcs.add(Swordsman(swordsmanStats, originX, playerX))
            elif unitType == "spearman":
                npcs.add(Spearman(spearmanStats, originX, playerX))
            elif unitType == "marksman":
                npcs.add(Marksman(marksmanStats, originX, playerX))
            elif unitType == "horseman":
                npcs.add(Horseman(horsemanStats, originX, playerX))
            for resource in cost:
                self.inventory[resource] = self.inventory[resource] - uStats[resource]
            units = units + 1
            friendlySpawnSound.play()
            return units
        return units

    def switchTool(self, event, button):
        #- Switches the player tools 
        if button == 4:
            self.selectedTool = self.selectedTool - 1
            if self.selectedTool < 0:
                self.selectedTool = 2
            self.currentTool = self.tools[self.selectedTool]
        elif button == 5:
            self.selectedTool = (self.selectedTool + 1) % 3
            self.currentTool = self.tools[self.selectedTool]
            
    def harvestResource(self, tiles):
        """ (None) -> None
            Checks if the player has the correct tool for the current tile and if the tile still has resources. 
            If true, runs _addAndRemoveResource().
        """
        if self.currentTool == "Pick" and self.currentTile.resource == GOLD and self.currentTile.resourceAmount > 0:
            self._addAndRemoveResource(GOLD, 25, tiles)
        elif self.currentTool == "Axe" and self.currentTile.resource == WOOD and self.currentTile.resourceAmount > 0:
            self._addAndRemoveResource(WOOD, 50, tiles)
        elif self.currentTool == "Pick" and self.currentTile.resource == STONE and self.currentTile.resourceAmount > 0:
            self._addAndRemoveResource(STONE, 50, tiles)

        sound = randint(0,2)
        harvestSounds[sound].play()
        
    def _addAndRemoveResource(self, resource, amountHarvested, tiles):
        #- Adds the amount specified of the resource specified to the inventory, and 
        #- removes the same amount from the current tile.
        
        self.inventory[resource] = self.inventory[resource] + amountHarvested
        tiles[self.currentTileRef].resourceAmount = tiles[self.currentTileRef].resourceAmount - amountHarvested
    
    def setGhostMode(self, game):
        #- When the player is dead, set him as a ghost
        game.openBuildMenu, game.openUnitMenu = False, False
        self.dead = True
        self.playerStep = 2
        self.jumpspeed = -35
        self.selectedTower = "No Tower"
        self.hp = 0
    
    def setLivingMode(self):
        #- When the player is revived, reset all the debuffs applied to him when ghosted
        self.dead = False
        self.jumpspeed = self.DEFAULT_JUMPSPEED
        self.playerStep = self.DEFAULT_SPEED
        self.hp = 1000
        self.invincibleTimer.reset()
        
##-- NPCS -- ##
class NPCGroup(pygame.sprite.Group):
    def __init__(self):
        pygame.sprite.Group.__init__(self)

class NPC(pygame.sprite.Sprite):
    def __init__(self, uStats, originX):
        pygame.sprite.Sprite.__init__(self)
        #- Stats
        self.hp = uStats[HP]
        self.strength = uStats[STRENGTH]
        self.defense = uStats[DEFENSE]
        self.speed = uStats[SPEED]
        self.cost = [uStats[GOLD], uStats[WOOD], uStats[STONE]]
        self.cooldown = uStats[COOLDOWN]
        self.index = 0

        self.hitbox = self.unitImage.get_rect()
        self.hitboxW = self.hitbox.width
        self.hitboxH = self.hitbox.height
        self.hitboxX = self.x
        self.hitboxY = self.y

        self.hitboxRect = pygame.Rect(self.hitboxX, self.hitboxY, self.hitboxW, self.hitboxH)

        #- Spritesheets loaded in
        self.spritesheets = [self.walkingSS, self.attackingSS, self.idleSS]
        self.sheetRect = [self.walkingSS.get_rect(), self.attackingSS.get_rect(), self.idleSS.get_rect()]
        self.sheetWidth = [self.sheetRect[WALK].width, self.sheetRect[ATTACK].width, self.sheetRect[IDLE].width]

        #- Select certain sheets and find the rect of them
        self.selectedSheet = IDLE
        self.rectDelay = Timer(True, 100)
        self.rect = self.spritesheets[self.selectedSheet].get_rect()
        self.rect.width = self.sheetWidth[self.selectedSheet] / self.numOfImages[self.selectedSheet]
        self.switchedSpritesheet = True
        self.isAttacking = False
        
    def updateSprite(self):
        #- Updates the sprite in accordance to the selected sheet
        self.imageSelected = self.spritesheets[self.selectedSheet]
        self.rect = pygame.Rect(self.x, self.y, self.rect.width, self.sheetRect[self.selectedSheet].height)
        self.imageSelected.set_clip(self.rect.width * self.index, 0, self.rect.width, self.rect.height)
        self.image = self.imageSelected.subsurface(self.imageSelected.get_clip())
    
    def loadNextImage(self):
        #- Loads the next image in from the spritesheet
        if self.rectDelay.durationComplete():
            if (self.index + 1) % self.numOfImages[self.selectedSheet] == 0 and self.isAttacking:
                self.isAttacking = False
            self.index = (self.index + 1) % self.numOfImages[self.selectedSheet]     
            self.rectDelay.reset()
        self.updateSprite()

    def resetSpritesheet(self):
        #- Resets the spritesheet and loads a new one in
        self.index = 0
        self.rect = self.spritesheets[self.selectedSheet].get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.rect.width = self.sheetWidth[self.selectedSheet] / self.numOfImages[self.selectedSheet] 

    def updateHitbox(self):
        #- Update the hitbox location
        self.hitboxX = self.x
        self.hitboxY = self.y
        self.hitboxRect = pygame.Rect(self.hitboxX, self.hitboxY, self.hitboxW, self.hitboxH)

    def isDead(self):
        #- Checks if dead
        if self.hp <= 0:
            return True
        return False

    def attack(self, other):
        #- Deals damage to an opponent
        damage = float(self.strength) / float(other.defense)
        other.hp = other.hp - damage
        attackNum = randint(0,2)
        attackSounds[attackNum].play()

    def draw(self):
        #- Blits the image onto the game screen
        gameWindow.blit(self.image, self.rect)
        self.loadNextImage()

class Unit(NPC):
    def __init__(self, unitType, originX, playerX, uStats):
        self.x = originX + 50
        self.y = UNIT_HEIGHT
        NPC.__init__(self, uStats, originX)
        self.unit = unitType
        self.attackRange = uStats[RANGE]
        self.type = "unit"
        self.allegiance = "good"
        self.canHitFlying = False
        self.flying = False
        self.selectedSheet = IDLE
        self.updateSprite()

    def move(self, direction):
        #- Moves the unit
        if direction == "forwards":
            self.x = self.x + self.speed
        elif direction == "backwards":
            self.x = self.x - self.speed

    def calculateAction(self, npcs, units, enemies, player, stronghold, tent, direction, spritesheetChanged):
        """(object, int, int, object, object, object, str, bool) -> None
            Determines a specific action for the unit to perform, based on distance from enemies.
        """
        if spritesheetChanged:
            self.switchedSpritesheet = True

        if direction == "stationary":
            shouldMove = False
        else:
            shouldMove = True

        if enemies > 0:
            for npc in npcs:
                #- If there is an enemy, attack it
                if (npc.type == "enemy" and npc.flying == False or (npc.flying == True and self.canHitFlying == True)) or self.isAttacking:
                    if calcDistance(self.x, npc.x, self.y, npc.y) <= self.attackRange:
                        shouldMove = False
                        if self.selectedSheet != IDLE:
                            self.switchedSpritesheet = True
                        if self.cooldownTimer.durationComplete():
                            self.attack(npc)
                            self.isAttacking = True
                            self.selectedSheet = ATTACK
                            self.resetSpritesheet()
                            self.switchedSpritesheet = False
                            self.cooldownTimer.reset()

        #- If the stronghold is there, attack it
        if calcDistance(self.x, stronghold.x, self.y, GROUND - 50) <= self.attackRange and direction == "forwards":
            shouldMove = False
            if self.selectedSheet != IDLE:
                self.switchedSpritesheet = True
            if self.unit != "marksman":
                if self.cooldownTimer.durationComplete():
                    self.attack(stronghold)
                    self.isAttacking = True
                    self.selectedSheet = ATTACK
                    self.resetSpritesheet()
                    self.switchedSpritesheet = False
                    self.cooldownTimer.reset()
        #- If you run into the tent, don't attack it
        if calcDistance(self.x, tent.x, self.y, GROUND - 50) <= self.attackRange and direction == "backwards":
            shouldMove = False
            if self.selectedSheet != IDLE:
                self.switchedSpritesheet = True
            self.switchedSpritesheet = True
        #- Switches spritesheets
        if shouldMove:
            if self.switchedSpritesheet:
                self.selectedSheet = WALK
                self.resetSpritesheet()
                self.switchedSpritesheet = False
            self.move(direction)
            
        elif self.switchedSpritesheet and not self.isAttacking:
            self.selectedSheet = IDLE
            self.resetSpritesheet()
            self.switchedSpritesheet = False

class Swordsman(Unit): #- Defines swordsman unit
    def __init__(self, swordsmanStats, originX, playerX):
        self.unitImage = unitImage
        self.walkingSS = loadImageTransparent("swordsmanWalk.png", "images/npcs")
        self.attackingSS = loadImageTransparent("swordsmanAttack.png", "images/npcs")
        self.idleSS = loadImageTransparent("swordsmanIdle.png", "images/npcs")
        self.numOfImages = [10, 4, 4]
        Unit.__init__(self, "swordsman", originX, playerX, swordsmanStats)
        self.cooldownTimer = Timer(True, self.cooldown * 1000)
    
class Marksman(Unit): #- Defines marksman unit
     def __init__(self, marksmanStats, originX, playerX):
        self.unitImage = marksmanImage
        self.walkingSS = loadImageTransparent("marksmanWalk.png", "images/npcs")
        self.attackingSS = loadImageTransparent("marksmanAttack.png", "images/npcs")
        self.idleSS = loadImageTransparent("marksmanIdle.png", "images/npcs")
        self.numOfImages = [12, 8, 4]
        Unit.__init__(self, "marksman", originX, playerX, marksmanStats)
        self.canHitFlying = True
        self.cooldownTimer = Timer(True, self.cooldown * 1000)

class Spearman(Unit): #- Defines spearman unit
     def __init__(self, spearmanStats, originX, playerX):
        self.unitImage = spearmanImage
        self.walkingSS = loadImageTransparent("spearmanWalk.png", "images/npcs")
        self.attackingSS = loadImageTransparent("spearmanAttack.png", "images/npcs")
        self.idleSS = loadImageTransparent("spearmanIdle.png", "images/npcs")
        self.numOfImages = [12, 6, 4]
        Unit.__init__(self, "spearman", originX, playerX, spearmanStats)
        self.cooldownTimer = Timer(True, self.cooldown * 1000)

class Horseman(Unit): #- Defines horseman unit
    def __init__(self, horsemanStats, originX, playerX):
        self.unitImage = horsemanImage
        self.walkingSS = loadImageTransparent("horsemanRun.png", "images/npcs")
        self.attackingSS = loadImageTransparent("horsemanAttack.png", "images/npcs")
        self.idleSS = loadImageTransparent("horsemanIdle.png", "images/npcs")
        self.numOfImages = [8, 6, 11]
        Unit.__init__(self, "horseman", originX, playerX, horsemanStats)
        self.cooldownTimer = Timer(True, self.cooldown * 1000)

class Enemy(NPC):
    def __init__(self, enemyType, originX, enemyStats, stronghold):
        self.x = stronghold.x
        self.y = UNIT_HEIGHT
        NPC.__init__(self, enemyStats, originX)
        self.type = "enemy"
        self.allegiance = "bad"
        self.unit = enemyType
        self.attackRange = enemyStats[RANGE]
        self.updateSprite()
    
    def move(self):
        #- Moves the enemy
        self.x = self.x - self.speed

    def calculateAction(self, npcs, units, enemies, player, stronghold, tent, direction, spritesheetChanged):
        """(object, int, int, object, object, object, str, bool) -> None
            Determines a specific action for the enemy to perform, based on distance from enemies.
        """
        if spritesheetChanged:
            self.switchedSpritesheet = True
            spritesheetChanged = False

        shouldMove = True
        if units > 0:
            for npc in npcs:
                #- If there is a unit, attack it
                if npc.type == "unit":
                    if calcDistance(self.x, npc.x, self.y, npc.y) <= self.attackRange or self.isAttacking:
                        if self.selectedSheet != WALK:
                            self.switchedSpritesheet = True
                        shouldMove = False
                        if self.cooldownTimer.durationComplete():
                            self.attack(npc)
                            self.isAttacking = True
                            self.selectedSheet = ATTACK
                            self.resetSpritesheet()
                            self.switchedSpritesheet = False
                            self.cooldownTimer.reset()
        #- If the player is there, attack it
        if calcDistance(self.x, player.x, self.y, GROUND-50) <= self.attackRange and not player.dead and player.invincibleTimer.durationComplete():
            if self.selectedSheet != WALK:
                self.switchedSpritesheet = True
            shouldMove = False
            if self.cooldownTimer.durationComplete():
                self.attack(player)
                self.isAttacking = True
                self.selectedSheet = ATTACK
                self.resetSpritesheet()
                self.switchedSpritesheet = False
                self.cooldownTimer.reset()
        #- If the tent is there, attack it
        if calcDistance(self.x, tent.x, self.y, GROUND-50) <= self.attackRange:
            if self.selectedSheet != WALK:
                self.switchedSpritesheet = True
            shouldMove = False
            if self.cooldownTimer.durationComplete() and self.unit != "rogue":
                self.attack(tent)
                self.isAttacking = True
                self.selectedSheet = ATTACK
                self.resetSpritesheet()
                self.switchedSpritesheet = False
                self.cooldownTimer.reset()
        #- Loads in new spritesheets
        if shouldMove:
            if self.switchedSpritesheet:
                self.selectedSheet = WALK
                self.resetSpritesheet()
                self.switchedSpritesheet = False
            self.move()
            
        elif self.switchedSpritesheet and not self.isAttacking:
            self.selectedSheet = IDLE
            self.resetSpritesheet()
            self.switchedSpritesheet = False

class Minion(Enemy): #- Defines minion unit
    def __init__(self, minionStats, originX, stronghold):
        self.unitImage = minionImage
        self.walkingSS = loadImageTransparent("minionWalk.png", "images/npcs")
        self.attackingSS = loadImageTransparent("minionAttack.png", "images/npcs")
        self.idleSS = loadImageTransparent("minionIdle.png", "images/npcs")
        self.numOfImages = [8, 4, 1]
        self.flying = False
        Enemy.__init__(self, "minion", originX, minionStats, stronghold)
        self.cooldownTimer = Timer(True, self.cooldown * 1000)

class Overseer(Enemy): #- Defines overseer unit
    def __init__(self, overseerStats, originX, stronghold):
        self.unitImage = overseerImage
        self.walkingSS = loadImageTransparent("overseerWalk.png", "images/npcs")
        self.attackingSS = loadImageTransparent("overseerAttack.png", "images/npcs")
        self.idleSS = loadImageTransparent("overseerIdle.png", "images/npcs")
        self.numOfImages = [4, 4, 1]
        self.flying = False
        Enemy.__init__(self, "overseer", originX, overseerStats, stronghold)
        self.cooldownTimer = Timer(True, self.cooldown * 1000)

class Tankwalker(Enemy): #- Defines tankwalker unit
    def __init__(self, tankwalkerStats, originX, stronghold):
        self.unitImage = tankwalkerImage
        self.walkingSS = loadImageTransparent("tankwalkerWalk.png", "images/npcs")
        self.attackingSS = loadImageTransparent("tankwalkerAttack.png", "images/npcs")
        self.idleSS = loadImageTransparent("tankwalkerIdle.png", "images/npcs")
        self.numOfImages = [4, 8, 2]
        self.flying = False
        Enemy.__init__(self, "tankwalker", originX, tankwalkerStats, stronghold)
        self.cooldownTimer = Timer(True, self.cooldown * 1000)

class Rogue(Enemy): #- Defines rogue unit
    def __init__(self, rogueStats, originX, stronghold):
        self.unitImage = rogueImage
        self.walkingSS = loadImageTransparent("rogueRun.png", "images/npcs")
        self.attackingSS = loadImageTransparent("rogueAttack.png", "images/npcs")
        self.idleSS = loadImageTransparent("rogueIdle.png", "images/npcs")
        self.numOfImages = [6, 6, 1]
        self.flying = False
        Enemy.__init__(self, "rogue", originX, rogueStats, stronghold)
        self.cooldownTimer = Timer(True, self.cooldown * 1000)

class Astral(Enemy): #- Defines astral unit
    def __init__(self, astralStats, originX, stronghold):
        self.unitImage = astralImage
        self.flying = True
        self.walkingSS = loadImageTransparent("astralFly.png", "images/npcs")
        self.attackingSS = loadImageTransparent("astralAttack.png", "images/npcs")
        self.idleSS = loadImageTransparent("astralFly.png", "images/npcs")
        self.numOfImages = [2, 4, 2]
        Enemy.__init__(self, "astral", originX, astralStats, stronghold)
        self.y = 300
        self.cooldownTimer = Timer(True, self.cooldown * 1000)

##-- TILES --##
    
class Tile(object):
    def __init__(self, tileType, resource, amount, originX):
        self.tile = tileType
        self.resource = resource
        self.resourceAmount = amount
        self.bonus = tileType
        self.hasTower = False
        self.tower = None
        self.towerType = None
        self.towerTier = 0
        self.x = originX
        
    def __str__(self):
        return self.tile

class Checkpoint(Tile):
    #- The checkpoint tiles
    def __init__(self, bonus, resource, amount, checkpointNumber, originX):
        self.checkpointNumber = checkpointNumber
        Tile.__init__(self, "Checkpoint", resource, amount, originX)
        self.tile = "Checkpoint"
        self.bonus = bonus

    def __str__(self):
        return self.tile + " - " + self.bonus

class Tent(Tile):
    #- The tent tiles
    def __init__(self,  originX):
        Tile.__init__(self, "Tent", None, None, originX)
        self.hp = 5000
        self.defense = 5
        
class Stronghold(Tile):
    #- The stronghold tiles
    def __init__(self,  originX):
        Tile.__init__(self, "Stronghold", None, None, originX)
        self.hp = 5000
        self.defense = 5
