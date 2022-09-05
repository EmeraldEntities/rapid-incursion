########################################################
# Title:   Rapid Incursion V0.1
#
# Joseph Wang : ICS20G : 21-12-2018
#
# Details: My final project for ICS20G, a third person tower defense action game thing!
########################################################
from incursionClasses import *
from random import randint, randrange
import pygame
pygame.init()

#- Make objects from the classes
game = Game()
title = Title()
controls = Controls()
gameCredits = Credits()
tutorial = Tutorial()
difficultySelector = DificultySelector()
player = Player("Gunmaster")
structures = Structures()
projectiles = Projectiles()
units = 0
enemies = 0
npcs = NPCGroup()

#- Variables that we will reference later
direction = "forwards"
switchedSpritesheet = False

harvestCooldown = Timer(True, player.miningCooldown*1000)   
pAttackCooldown = Timer(True, player.cooldown*1000)

window = "title"
inPlay = True
debugMode = False
spawnAdvancedUnits = False

#- Sets display title and icon
pygame.display.set_caption("Rapid Incursion")
pygame.display.set_icon(iconImage)

print("Welcome to Rapid Incursion!")
print("~~~~~~~~~~~~~~~~~~~~")
print("Made by Joseph Wang!")

   #################
### -- MAIN LOOP -- ###
   #################

loadMusic(mainTheme)
while inPlay:
    if window == "title":
        #- If the window is title, draw it and do its actions
        title.drawTitleWindow()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    window = title.checkForMouseInteraction()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    inPlay = False
    
    elif window == "difficultySelector":
        #- If the window is difficulty selector, draw it and do its actions
        difficultySelector.drawDifficultiesWindow()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    window, gameToReset = difficultySelector.checkForDifficultySelection(game)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    window = "title"
    
    elif window == "controls":
        #- If the window is controls, draw it and do its actions
        controls.drawControlsWindow()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    window = controls.performControlsChange()
                if event.key == pygame.K_ESCAPE:
                    window = "title"
                    controls.currentPage = 0
    
    elif window == "credits":
        #- If the window is credits, draw it and do its actions
        gameCredits.drawCreditsWindow()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE:
                    window = "title"
    
    elif window == "tutorial":
        #- If the window is tutorial, draw it and do its actions
        tutorial.drawTutorialWindow()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    window = tutorial.changeTutorialPage()
                if event.key == pygame.K_ESCAPE:
                    window = "title"
                    tutorial.currentPage = 0
    
    elif window == "gameEnd":
        #- If the window is gameEnd, draw it and do its actions
        if game.victor == "player":
            gameWindow.blit(winScreenImage, (0,0))
        elif game.victor == "enemy":
            gameWindow.blit(loseScreenImage, (0,0))
            
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE or event.key == pygame.K_ESCAPE:
                    window = "title"
                    title.screen = "title"
                    game.difficulty = "medium"
                    loadMusic(mainTheme)

    elif window == "game":
        #- If the window is title, draw it and do its actions
        if gameToReset:
            #- Check if the game needs to be reset
            originX, playerX, npcs, units, enemies, tiles, tilemap = game.resetGame(originX, player, playerX, npcs, units, enemies)
            spawnAdvancedUnits = False
            gameToReset = False
        #- Reset the tent to its original place
        tiles[29].x = DEFAULT_STRONGHOLDX + 400
        tiles[0].x = DEFAULT_TENTX + 400
        mousePos = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()
        game.redrawWindow(player, originX, groundRelToPlayer, mousePos, projectiles, npcs, tiles)
        originX, playerX, movementDirection, groundRelToPlayer, previousGroundRel = player.move(originX, 
        playerX, backgroundW, movementDirection, keys, groundRelToPlayer, previousGroundRel, npcs, structures)

        #- Check if the game should end
        window = game.endGame(tiles[0], tiles[29])
        game.increaseLevel()
        game.updateClock(FPS)
        #- Readjust the tent and stronghold position
        game.adjustTileX(tiles[29], playerX)
        game.adjustTileX(tiles[0], playerX)
        
        player.findCurrentTile(playerX, tiles)
        player.regenHealth()

        for event in pygame.event.get():
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4 or event.button == 5:
                    player.switchTool(event, event.button)
                elif event.button == 1:
                    if not player.dead:
                        if game.openBuildMenu:
                            for button in towerButtonList:
                                #- Checks to see if the player clicks a button inside the tower menu
                                if game.checkIfInsideButton(button):
                                    player.buildTower(button.unitToMake, playerX, structures, tiles)
                        elif game.openUnitMenu:
                            for button in unitButtonList:
                                #- Checks to see if the player clicks a button inside the unit menu
                                if game.checkIfInsideButton(button):
                                    if units < game.unitLimit:
                                        units = player.recruitUnit(button.unitToMake, 
                                                                        originX, playerX, units, npcs)
                        elif player.currentTool == player.weapon:
                            if pAttackCooldown.durationComplete():
                                #- Checks to see if the player's attack duration is complete
                                if player.weapon == "Rifle":
                                    projectiles.add(Bullet(100, 20, CENTER, player.y + 50, player, 
                                                            playerBullet, mousePos))
                                    player.isAttacking = True
                                    player.selectedSheet = ATTACK
                                    player.resetSpritesheet()
                                    pAttackCooldown.reset()
                                    gunshotSound.play()

                        elif player.currentTile.towerType == "outpost" or not player.currentTile.hasTower:
                            if harvestCooldown.durationComplete():
                                #- If the harvest cooldown is done, do its actions
                                player.harvestResource(tiles)
                                harvestCooldown.reset()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    if not player.dead:
                        if player.selectedTower != "No Tower":
                            #- Make sure the player selected a tower, then either build or upgrade
                            if not player.selectedTower.finishedBuilding and game.checkIfCanAfford(player, 
                                                                            player.selectedTower.stageCost):
                                player.selectedTower.build(player)
                            elif not player.selectedTower.maxLevel and game.checkIfCanAfford(player, 
                                                                        player.selectedTower.upgradeCost):
                                player.selectedTower.upgrade(player)             
                        else:
                            #- Open build menu
                            game.openUnitMenu = False
                            if game.openBuildMenu:
                                game.openBuildMenu = False
                            else:
                                game.openBuildMenu = True
                        
                if event.key == pygame.K_n:
                    #- Open unit menu
                    game.openBuildMenu = False
                    if game.openUnitMenu:
                        game.openUnitMenu = False
                    else:
                        game.openUnitMenu = True
                
                if event.key == pygame.K_x and player.selectedTower != "No Tower":
                    #- Sells the tower
                    if player.currentTile.hasTower and player.currentTile.tower.finishedBuilding:
                        player.selectedTower.sell(player)

                if event.key == pygame.K_e:
                    #- Selects towers
                    if not player.dead:
                        if player.currentTile.hasTower == True:
                            if player.selectedTower != "No Tower":
                                player.selectedTower = "No Tower"
                            else: 
                                player.selectedTower = player.currentTile.tower
                    else:
                        #- If the player is dead, revive if they are at an outpost in a checkpoint or if they are at the tent
                        if (player.currentTile.towerType == "outpost" and player.currentTile.tile == "Checkpoint") or player.currentTile.tile == "Tent":
                            player.setLivingMode()
                  
                if event.key == pygame.K_g:
                    #- Turn on debug mode
                    if not debugMode:
                        debugMode = True
                        print("debug mode!")
                    else:
                        debugMode = False
                        print("normal mode!")

                if event.key == pygame.K_ESCAPE:
                    if game.openBuildMenu:
                        game.openBuildMenu = False
                    elif game.openUnitMenu:
                        game.openUnitMenu = False
                    else:
                        window = "title"
                        loadMusic(mainTheme)

                if debugMode:   #- All debug stuff to print out certain things, not going to include comments
                    if event.key == pygame.K_1:
                        print(player.inventory)
                            
                    if event.key == pygame.K_2:
                        print(structures.sprites())

                    if event.key == pygame.K_4:
                        print(player.currentTile.hasTower, player.currentTile.towerType)
                    
                    if event.key == pygame.K_5:
                        player.setGhostMode(game)
                    
                    if event.key == pygame.K_6:
                        print(units, npcs)
                    
                    if event.key == pygame.K_7:
                        for unit in npcs:
                            unit.kill()
                    if event.key == pygame.K_8:
                        print(playerX, originX)

                    if event.key == pygame.K_9:
                        print(tiles[0].x, tiles[29].x)

                    if event.key == pygame.K_p:
                        for unit in npcs:
                            print(unit.x, unit.hp, unit.y, tiles[0].x)

                    if event.key == pygame.K_v:
                        for unit in npcs:
                            for tower in structures:
                                print(tower.x, unit.x, TOWER_HEIGHT + 100, unit.y)
                    
                    if event.key == pygame.K_i:
                        print(tiles[0].hp, tiles[29].hp)

                    if event.key == pygame.K_m:
                        npcs.add(Rogue(rogueStats, originX, tiles[29]))
                        enemies = enemies + 1

                    if event.key == pygame.K_SLASH:
                        for resource in cost:
                            player.inventory[resource] = player.inventory[resource] + 1000
                    
                    if event.key == pygame.K_h:
                        print(game.level)

                #- Controls the units and tells them to either stay, attack or defend
                if event.key == pygame.K_l:
                    direction = "forwards"
                    switchedSpritesheet = True
                elif event.key == pygame.K_j:
                    direction = "backwards"
                    switchedSpritesheet = True
                elif event.key == pygame.K_k:
                    direction = "stationary"
                    switchedSpritesheet = True

        if game.spawnTimer.durationComplete():
            #- Randomly spawns units based on level
            if game.level >= 3:   #- If the level is above or equal to 3, advanced units will spawn
                spawnAdvancedUnits = True
            enemyToSpawn = randint(1, 11)
            if enemyToSpawn > 0 and enemyToSpawn <= 2:
                npcs.add(Rogue(rogueStats, originX, tiles[29]))
            elif enemyToSpawn > 2 and enemyToSpawn <= 4:
                npcs.add(Overseer(minionStats, originX, tiles[29]))
            elif enemyToSpawn > 4 and enemyToSpawn <= 6 and spawnAdvancedUnits:
                npcs.add(Tankwalker(tankwalkerStats, originX, tiles[29]))
            elif enemyToSpawn > 6 and enemyToSpawn <= 8 and spawnAdvancedUnits:
                npcs.add(Astral(astralStats, originX, tiles[29]))
            else:
                npcs.add(Minion(minionStats, originX, tiles[29]))
                
            enemies = enemies + 1
            enemySpawnSound.play()
            game.spawnTimer.reset()

        for bullet in projectiles:
            bullet.move()
            if bullet.originType == "good":
                bulletEnemies = "bad"
            elif bullet.originType == "bad":
                bulletEnemies = "good"
            #- Checks to see if the bullet hit anything
            if bullet.collides(bulletEnemies, npcs, player):   #- If so, remove bullet and damage object
                bullet.kill()
                bullet.inflictDamage()
            if (bullet.objectY > GROUND or bullet.objectY < 0) or (bullet.objectX > WIDTH or bullet.objectX < 0):
                bullet.kill()

        if enemies > 0:   #- Calculates the action for every tower assuming there are enemies
            for tower in structures:
                if tower.finishedBuilding:
                    tower.calculateAction(npcs, enemies, projectiles)

        if player.hp <= 0:
            #- If the player is dead, spawn it in ghost mode
            player.setGhostMode(game)

        for unit in npcs:
            #- Calculate the action for every NPC
            unit.calculateAction(npcs, units, enemies, player, tiles[29], tiles[0], direction, switchedSpritesheet)
            if unit.isDead():   #- If it's dead, kill it and remove 1 from the respective counters
                if unit.type == "unit":
                    units = units - 1
                elif unit.type == "enemy":
                    enemies = enemies - 1
                unit.kill()

        #- Resets any spritesheet changes
        switchedSpritesheet = False

pygame.quit()
    
