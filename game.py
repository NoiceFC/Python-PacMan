# Ethan Choo, ec4kj
#ahs5y, Asmir Shaikh

import pygame
import gamebox
import random
camera = gamebox.Camera(800,600)

#pacman sprite sheets
sheet1 = gamebox.load_sprite_sheet("pacmanSprite1.png", 1, 3)
sheet2 = gamebox.load_sprite_sheet("pacmanSprite2.png", 3, 1)
sheet3 = gamebox.load_sprite_sheet("pacmanSprite3.png", 1, 3)
sheet4 = gamebox.load_sprite_sheet("pacmanSprite4.png", 3, 1)
sheet1.append(sheet1[1])
sheet2.append(sheet2[1])
sheet3.append(sheet3[1])
sheet4.append(sheet4[1])
pacman = gamebox.from_image(20, 20, sheet1[1])
pacman.size = [39,39]
pacman.left = 320
pacman.top = 120

#ghost sprite sheets
ghostSheet = gamebox.load_sprite_sheet("ghost.png",1, 1)
ghostSheet.append("scaredGhost.png")
ghost = gamebox.from_image(320,320,ghostSheet[0])
ghost.size = [40,40]
ghost.left = 320
ghost.top = 360


#level 1 creation
map1 = [
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3,
    1, 4, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 4, 1, 3, 3, 3,
    1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 3, 3, 3,
    1, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 1, 3, 3, 3,
    1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 3, 3, 3,
    1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 3, 3, 3,
    1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 3, 3, 3,
    1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 3, 3, 3,
    1, 0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 1, 3, 3, 3,
    1, 0, 1, 1, 0, 1, 0, 1, 3, 1, 0, 1, 0, 1, 1, 0, 1, 3, 3, 3,
    1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 3, 3, 3,
    1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 3, 3, 3,
    1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 3, 3, 3,
    1, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 1, 3, 3, 3,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3,
]
collectibles = []
powerUps = []
wallObjects = []
index = 0
for i in map1:
    if i ==0:
        x = ((index%20)*40)+20
        y = ((index//20)*40)+20
        collectible = gamebox.from_color(x,y, "white", 10,10)
        collectibles.append(collectible)
    if i == 1:
        x = (index%20)*40
        y = (index//20)*40
        wall = gamebox.from_color(x,y,"blue",40,40)
        wall.left = x
        wall.top = y
        wallObjects.append(wall)
    if i == 2:
        x = (index%20)*40
        y = (index//20)*40
        wall = gamebox.from_color(x,y,"green",40,40)
        wall.left = x
        wall.top = y
        wallObjects.append(wall)
    if i == 4:
        x = ((index%20)*40)+20
        y = ((index//20)*40)+20
        powerup = gamebox.from_circle(x,y, "white", 10)
        powerUps.append(powerup)

    index +=1

#level 2 creation
map2 = [
    1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3,
    1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 3, 3, 3,
    1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 3, 3, 3,
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 3, 3,
    1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 3, 3, 3,
    1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 3, 3, 3,
    1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 3, 3, 3,
    1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 3, 3, 3,
    0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3,
    1, 0, 1, 1, 0, 1, 0, 1, 3, 1, 0, 1, 0, 1, 1, 0, 1, 3, 3, 3,
    1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 3, 3, 3,
    1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 3, 3, 3,
    1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 3, 3, 3,
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 3, 3,
    1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3,
]
collectibles2 = []
wallObjects2 = []
for i in map2:
    if i ==0:
        x = ((index%20)*40)+20
        y = ((index//20)*40)+20
        collectible = gamebox.from_color(x,y, "white", 10,10)
        collectibles2.append(collectible)
    if i == 1:
        x = (index%20)*40
        y = (index//20)*40
        wall = gamebox.from_color(x,y,"blue",40,40)
        wall.left = x
        wall.top = y
        wallObjects2.append(wall)
    if i == 2:
        x = (index%20)*40
        y = (index//20)*40
        wall = gamebox.from_color(x,y,"green",40,40)
        wall.left = x
        wall.top = y
        wallObjects2.append(wall)
    index +=1

#initialize variables
game_on = False
ticker = 0
level = 1
start = 'start'
time = 0
collectedLeft = len(collectibles)
maxCollectibles = len(collectibles)
leftTouch = False
rightTouch = False
topTouch = False
bottomTouch = False
ghostTimer = 0
orientation = 'right'
nextMove = ''
powerUpPacman = False
powerUpTimer = 0
startTime = 0
ghostStartPosition = True
speed_x = 0
speed_y = 0
ghost.xspeed = 0
ghost.yspeed = 0
prevGhostMove = ''
pacmanHealh = 3



#main function
def tick(keys):
    '''
    checks for key inputs and collisions between pacman and ghosts and the wall 30 times a second. Arrow keys
    are used to move pacman and the ghost moves randomly. Also checks for pacman picking up collectibles and finishing the level
    :param keys:
    :return:
    '''
    global time
    global start
    global collectedLeft
    global leftTouch
    global rightTouch
    global topTouch
    global bottomTouch
    global speed_x
    global speed_y
    global ghostTimer
    global level
    global orientation
    global nextMove
    global nextX
    global nextY
    global powerUpPacman
    global powerUpTimer
    global startTime
    global ghostStartPosition
    global prevGhostMove
    global pacmanHealh


    #start
    if start == 'ready':
        if pygame.K_RETURN in keys:
            if collectedLeft > 0:
                #reset collectibles
                ghostTimer = 0
                time = 0
                pacman.left = 40
                pacman.top = 40
                ghost.left = 320
                ghost.top = 360
                ghost.xspeed = 0
                ghost.yspeed = 0
            if collectedLeft == 0:
                level +=1
            keys.clear()
    if start == 'ready':
        time += 0.5
        ghostTimer += 1
        if powerUpTimer > 0:
            powerUpPacman = True
            powerUpTimer -= 1
        else:
            powerUpPacman = False
        nextX = pacman.x + speed_x
        nextY = pacman.y + speed_y
        pacman.move_speed()
        ghost.move_speed()


    #ghost image change
    if powerUpPacman:
        ghost.image = ghostSheet[1]
    else:
        ghost.image = ghostSheet[0]


    #pacman and wall collisions
    for wall in wallObjects:
        if pacman.top_touches(wall, -2):
            topTouch = True
            pacman.move_to_stop_overlapping(wall)
            speed_y = 0
            break
        else:
            topTouch = False
    for wall in wallObjects:
        if pacman.bottom_touches(wall, -2):
            bottomTouch = True
            pacman.move_to_stop_overlapping(wall)
            speed_y = 0
            break
        else:
            bottomTouch = False
    for wall in wallObjects:
        if pacman.right_touches(wall, -2):
            rightTouch = True
            pacman.move_to_stop_overlapping(wall)
            speed_x = 0
            break
        else:
            rightTouch = False
    for wall in wallObjects:
        if pacman.left_touches(wall, -2):
            leftTouch = True
            pacman.move_to_stop_overlapping(wall)
            speed_x = 0
            break
        else:
            leftTouch = False

    #ghost and wall collisions
    if not ghostStartPosition:
        for wall in wallObjects:
            if ghost.top_touches(wall):
                ghost.move_to_stop_overlapping(wall)
            if ghost.bottom_touches(wall):
                ghost.move_to_stop_overlapping(wall)
            if ghost.right_touches(wall):
                ghost.move_to_stop_overlapping(wall)
            if ghost.left_touches(wall):
                ghost.move_to_stop_overlapping(wall)



        #ghost movement
        moves = ['up','right','down','left']
        if not ghostStartPosition and ghost.left%40 == 0 and ghost.top%40 ==0:
            for wall in wallObjects:
                if ghost.x-40 == wall.x and ghost.y == wall.y:
                    moves.remove('left')
            for wall in wallObjects:
                if ghost.x+40 == wall.x and ghost.y == wall.y:
                    moves.remove('right')
            for wall in wallObjects:
                if ghost.x == wall.x and ghost.y+40 == wall.y:
                    moves.remove('down')
            for wall in wallObjects:
                if ghost.x == wall.x and ghost.y-40 == wall.y:
                    moves.remove('up')
            if prevGhostMove not in moves:
                if prevGhostMove == 'up':
                    try:
                        moves.remove('down')
                    except:
                        doesntmatter = 'doesntmatter'
                if prevGhostMove == 'down':
                    try:
                        moves.remove('up')
                    except:
                        doesntmatter = 'doesntmatter'
                if prevGhostMove == 'right':
                    moves.remove('left')
                if prevGhostMove == 'left':
                    moves.remove('right')
            ghostMove = moves[random.randrange(0, len(moves))]
            if prevGhostMove in moves:
                ghostMove = prevGhostMove
            if ghostMove == 'up':
               ghost.yspeed = -5
            if ghostMove == 'right':
                ghost.xspeed = 5
            if ghostMove == 'down':
                ghost.yspeed = 5
            if ghostMove == 'left':
                ghost.xspeed = -5
            prevGhostMove = ghostMove


    #pacman orientation sprite change
    if pacman.xspeed == 5:
        if int(time%4) == 0:
            pacman.image = sheet1[0]
        if int(time%4) == 1:
            pacman.image = sheet1[1]
        if int(time%4) == 2:
            pacman.image = sheet1[2]
        if int(time%4) == 3:
            pacman.image = sheet1[3]
    if pacman.yspeed == -5:
        if int(time%4) == 0:
            pacman.image = sheet2[2]
        if int(time%4) == 1:
            pacman.image = sheet2[1]
        if int(time%4) == 2:
            pacman.image = sheet2[0]
        if int(time%4) == 3:
            pacman.image = sheet2[3]
    if pacman.xspeed == -5:
        if int(time%4) == 0:
            pacman.image = sheet3[2]
        if int(time%4) == 1:
            pacman.image = sheet3[1]
        if int(time%4) == 2:
            pacman.image = sheet3[0]
        if int(time%4) == 3:
            pacman.image = sheet3[1]
    if pacman.yspeed == 5:
        if int(time%4) == 0:
            pacman.image = sheet4[0]
        if int(time%4) == 1:
            pacman.image = sheet4[1]
        if int(time%4) == 2:
            pacman.image = sheet4[2]
        if int(time%4) == 3:
            pacman.image = sheet4[3]
    else:
        if orientation == 'right':
            if int(time % 4) == 0:
                pacman.image = sheet1[0]
            if int(time % 4) == 1:
                pacman.image = sheet1[1]
            if int(time % 4) == 2:
                pacman.image = sheet1[2]
            if int(time % 4) == 3:
                pacman.image = sheet1[3]
        if orientation == 'up':
            if int(time % 4) == 0:
                pacman.image = sheet2[2]
            if int(time % 4) == 1:
                pacman.image = sheet2[1]
            if int(time % 4) == 2:
                pacman.image = sheet2[0]
            if int(time % 4) == 3:
                pacman.image = sheet2[3]
        if orientation == 'left':
            if int(time % 4) == 0:
                pacman.image = sheet3[2]
            if int(time % 4) == 1:
                pacman.image = sheet3[1]
            if int(time % 4) == 2:
                pacman.image = sheet3[0]
            if int(time % 4) == 3:
                pacman.image = sheet3[1]
        if orientation == 'down':
            if int(time % 4) == 0:
                pacman.image = sheet4[0]
            if int(time % 4) == 1:
                pacman.image = sheet4[1]
            if int(time % 4) == 2:
                pacman.image = sheet4[2]
            if int(time % 4) == 3:
                pacman.image = sheet4[3]

    #pacman movemnt inputs
    if pygame.K_UP in keys:
        orientation = 'up'
        nextMove = 'up'
        keys.clear()
    if pygame.K_DOWN in keys:
        orientation = 'down'
        nextMove = 'down'
        keys.clear()
    if pygame.K_RIGHT in keys:
        orientation = 'right'
        nextMove = 'right'
        keys.clear()
    if pygame.K_LEFT in keys:
        orientation = 'left'
        nextMove = 'left'
        keys.clear()

    #pacman movement
    if nextMove == 'right' and not rightTouch:
        speed_x = 5
    if nextMove == 'left' and not leftTouch:
        speed_x = -5
    if nextMove == 'up' and not topTouch:
        speed_y = -5
    if nextMove == 'down' and not bottomTouch:
        speed_y = 5


    pacman.xspeed = speed_x
    pacman.yspeed = speed_y


    #add second level


    #pacman death/kill ghost
    if pacman.touches(ghost,-5):
        if powerUpPacman:
            ghost.left = 320
            ghost.top = 360
            startTime = ghostTimer
            powerUpTimer = 0
        else:
            pacmanHealh -= 1
            start = 'injured'

    if start == 'injured':
        ghostTimer = 0
        time = 0
        pacman.left = 320
        pacman.top = 120
        ghost.left = 320
        ghost.top = 360
        ghost.xspeed = 0
        ghost.yspeed = 0
        if pygame.K_RETURN in keys:
            keys.clear()
            start = 'ready'




    #ghost start code
    if ghost.left == 320 and ghost.top == 360:
        ghostStartPosition = True
    if startTime == ghostTimer:
        ghost.xspeed = 0
        ghost.yspeed = 0
    if 47+startTime > ghostTimer > 30+startTime:
        ghost.yspeed = -5
    if ghostTimer > 47+startTime:
        ghostStartPosition = False


    #powerup code
    for i in powerUps:
        if pacman.touches(i):
            powerUps.remove(i)
            powerUpTimer = 200


    #win condition
    if collectedLeft == 0:
        start = 'win'



    #collectible code
    for i in collectibles:
        if pacman.touches(i):
            collectibles.remove(i)
            collectedLeft -= 1

    if start == 'start' and pygame.K_RETURN in keys:
        keys.clear()
        start = 'instructions'

    if start == 'instructions' and pygame.K_RETURN in keys:
        keys.clear()
        start = 'ready'

    if (start == 'win' or start == 'loss') and pygame.K_RETURN in keys:
        keys.clear()
        collectedLeft = 120
        start = 'start'

    if pacmanHealh == 0:
        start = 'loss'


    startDisplay = [gamebox.from_text(400, 75, 'PAC MAN', 72, 'yellow', True, True),
                    gamebox.from_text(400, 120, 'By Asmir Shaikh (ahs5y) and Ethan Choo (ec4kj)', 36, 'yellow', True, True),
                    gamebox.from_text(400, 525, 'Press \'Return\' to continue', 72, 'yellow', True, True)]

    instructions = [gamebox.from_text(400, 75, 'You must collect all the bites', 72, 'blue'),
                    gamebox.from_text(400, 125, 'while avoiding the ghosts!', 72, 'blue'),
                    gamebox.from_text(400, 175, 'Touch a ghost 3 times', 72, 'blue'),
                    gamebox.from_text(400, 225, 'and you lose!', 72, 'blue'),
                    gamebox.from_text(400, 325, 'Collect the large bites to kill', 72, 'blue'),
                    gamebox.from_text(400, 375, 'ghosts when you touch them!', 72, 'blue'),
                    gamebox.from_text(400, 555, 'Use the arrow keys to move', 72, 'blue')]

    loseDisplay = [gamebox.from_text(400, 75, 'You Lost!', 72, 'yellow'),
                   gamebox.from_text(400, 525, 'Better Luck Next Time!', 72, 'yellow')]
    winDisplay = [gamebox.from_text(400, 75, 'You Won!', 72, 'yellow'),
                  gamebox.from_text(400, 525, 'Great Job!', 72, 'yellow')]

    injuredDisplay = [gamebox.from_text(400, 225, 'You lost a life!', 72, 'yellow'),
                      gamebox.from_text(400, 275, 'You have ' + str(pacmanHealh) + ' lives left!', 72,'yellow'),
                      gamebox.from_text(400, 325, 'Press Return to Continue', 72, 'yellow')]

    camera.clear("black")

    camera.draw(gamebox.from_text(740, 50, 'Lives: ' + str(pacmanHealh), 50, "Red"))
    camera.draw(gamebox.from_text(740, 500, str(collectedLeft), 50, "Red"))
    camera.draw(gamebox.from_text(740, 550, 'Left', 50, "Red"))


    if start == 'start':
        imag = gamebox.from_image(400, 300, 'https://cdn.dribbble.com/users/4467/screenshots/1612059/pacman.jpg')
        camera.draw(imag)
        for i in startDisplay:
            camera.draw(i)

    if start == 'instructions':
        bground = gamebox.from_image(400, 300, 'beige-background.jpg')
        camera.draw(bground)
        for i in instructions:
            camera.draw(i)

    if start == 'win':
        img = gamebox.from_image(400, 300, 'https://cdn.dribbble.com/users/4467/screenshots/1612059/pacman.jpg')
        camera.draw(img)
        for i in winDisplay:
            camera.draw(i)

    if start == 'loss':
        img = gamebox.from_image(400, 300, 'https://cdn.dribbble.com/users/4467/screenshots/1612059/pacman.jpg')
        camera.draw(img)
        for i in loseDisplay:
            camera.draw(i)

    if start == 'ready' or start == 'injured':
        for wall in wallObjects:
            camera.draw(wall)
        for collectible in collectibles:
            camera.draw(collectible)
        for powerUp in powerUps:
            camera.draw(powerUp)


        camera.draw(pacman)
        camera.draw(ghost)
        if not start:
            if time == 0:
                camera.draw(startDisplay)
            if collectedLeft == 0:
                camera.draw(winDisplay)
            elif time > 0:
                camera.draw(endDisplay)

    if start == 'injured':
        for i in injuredDisplay:
            camera.draw(i)
    camera.display()



gamebox.timer_loop(30, tick)


#Bibliography
#“Pac-Man and the Ghosts.” Dribbble, dribbble.com/shots/1612059-Pac-Man-and-the-Ghosts.
#“SILK BEIGE.” Stratum Natural Stone, stratumstone.com/collection/silk-beige-natural-stone/.