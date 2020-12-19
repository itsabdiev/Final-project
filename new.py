import pygame
import random
from pygame import mixer
import math


pygame.init()
background = pygame.image.load('project back.jpg')
screen = pygame.display.set_mode((1000, 600))
mixer.music.load('RUDE - Eternal Youth(MP3_160K).mp3')
mixer.music.play(-1)        #infinitive music
pygame.mixer.music.set_volume(0.2)


#PLayer
playerImg = pygame.image.load('jumper-1.png')
playerX = 500
playerY = 150
width = 40
height = 60
vel = 7.5
#Enemy
enemyImg = pygame.image.load('ghost.png')
enemyX = 10
enemyY = 560
enemyX_change = 4






#Brilliant
diamondImg = []
diamondX = []
diamondY = []
diamondX_change = []
diamondY_change = []
num_of_diamonds = 1

for k in range(num_of_diamonds):  #добавляем в лист
    diamondImg.append(pygame.image.load('diamond.png'))
    diamondX.append(random.randint(10, 960))
    diamondY.append(random.randint(20, 580))
    diamondX_change.append(0)
    diamondY_change.append(0)


#Platforms
p1 = 450
p2 = 300
p3 = 600
p4 = 200
p5 = 700
p6 = 100
p7 = 800
p8 = 0
p9 = 900
p10 = 450
p11 = 300
p12 = 600
platform1 = p1,500,100,7
platform2 = p2,400,100,7
platform3 = p3,400,100,7
platform4 = p4,300,100,7
platform5 = p5,300,100,7
platform6 = p6,200,100,7
platform7 = p7,200,100,7
platform8 = p8,100,100,7
platform9 = p9,100,100,7
platform10 = p10,200,100,7
platform11 = p11,200,100,7
platform12 = p12,200,100,7



s = 'can'
platforms = [platform1,platform2,platform3,platform4,platform5,platform6,platform7,platform8,platform9,platform10,platform11,platform12]#list of platforms
w = 'process'
isJump = False
jumpCount = 10

score_value = 0
font = pygame.font.Font('kj.ttf',20)  # style of text
textX = 10     #МЕсто скора
textY = 10

over_font = pygame.font.Font('Chopsic.otf',64)


textX = 10     #МЕсто скора
textY = 10

timeX =  550
timeY = 10

pygame.display.set_caption('   | Ninja in Pyjama  |    ') # Название игры
icon = pygame.image.load('icon.png')     #Загружаем иконку
pygame.display.set_icon(icon)
def player(x, y):  # function that is painting player on screen
    screen.blit(playerImg, (x, y))


def isCollision(diamondX,diamondY,shurikenX,shurikenY):
    distance = math.sqrt((math.pow(diamondX-shurikenX,2)) + (math.pow(diamondY-shurikenY,2))) # проверяем РАСТОЯНИЕ МЕЖДУ АЛМАЗОМ И НИНДЗЯ  d = undersquare(((x2-x1)^^2) - ((y2-y1)^^2)) разница между поинтами
    if distance < 50:
        return True
    else:
        return False

def isCollision2(enemyX,enemyY,playerX,playerY):
    distance = math.sqrt((math.pow(enemyX-playerX,2)) + (math.pow(enemyY-playerY,2))) # проверяем РАСТОЯНИЕ МЕЖДУ АЛМАЗОМ И НИНДЗЯ  d = undersquare(((x2-x1)^^2) - ((y2-y1)^^2)) разница между поинтами

    if distance < 35:
        return True
    else:
        return False

def diamond(x, y, k):  # function that is painting diamond on screen
    screen.blit(diamondImg[k], (x, y))


def r():
    for i in platforms:
        pygame.draw.rect(screen, (99, 22, 59), pygame.Rect(i))


def game_over_text():
    over_text = over_font.render("GAME OVER" , True, (199, 0, 57))
    screen.blit(over_text, (250,255))   # SEREDINA EKRANA

def enemy(x, y):  # function that is painting enemy on screen
    screen.blit(enemyImg, (x, y))

def show_score(x,y):
    score = font.render("SCORE  :" +'  '+ str(score_value),True, (99, 22, 59))
    screen.blit(score, (x, y))

def show_timer(x,y):
    scorec = fontc.render("" +''+ str(count),True, (199, 0, 57))
    screen.blit(scorec, (x, y))




run = True

while run:
    pygame.time.delay(25)
    screen.blit(background, (0, 0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False




    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and playerX > vel:
        playerX -= vel
        playerImg = pygame.image.load('jumper-left.png')
    if keys[ord('a')] and playerX > vel:
        playerX -= vel
        playerImg = pygame.image.load('jumper-left.png')
    if keys[pygame.K_RIGHT] and  playerX < 1010 - vel - width:
        playerX += vel
        playerImg = pygame.image.load('jumper-right.png')
    if keys[ord('d')] and playerX < 1010 - vel - width:
        playerX += vel

        playerImg = pygame.image.load('jumper-right.png')
    if not (isJump):


        if keys[pygame.K_SPACE] and s == 'can':
            jumpsound = mixer.Sound('jump.wav')
            jumpsound.play()
            isJump = True
            playerImg = pygame.image.load('jumper-up.png')
        if keys[pygame.K_UP] and s == 'can':
            jumpsound = mixer.Sound('jump.wav')
            jumpsound.play()
            isJump = True
            playerImg = pygame.image.load('jumper-up.png')

        if keys[pygame.K_0]:
            pygame.mixer.music.set_volume(0)
        if keys[pygame.K_9]:
            pygame.mixer.music.set_volume(0.3)




    else:
        if jumpCount >= -10:
            playerY -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1


        else:
            jumpCount = 10
            isJump = False
    if keys[pygame.K_LEFT] and keys[pygame.K_SPACE]:
        playerImg = pygame.image.load('jumper-jleft.png')
    if keys[pygame.K_RIGHT] and keys[pygame.K_SPACE]:
        playerImg = pygame.image.load('jumper-jright.png')



    if event.type == pygame.KEYUP:  # not pressed buttons
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
          # Написали код чтобы ниндзя не двигался когда кнопка нет нажата
            playerImg = pygame.image.load('jumper-1.png')
        if event.key == ord('a') or event.key == ord('d'):
            playerImg = pygame.image.load('jumper-1.png')


        if event.key == pygame.K_SPACE:
            playerImg = pygame.image.load('jumper-1.png')
        if event.key == pygame.K_UP:
            playerImg = pygame.image.load('jumper-1.png')


    if playerX >= 445 and playerX <= 550 and playerY >= 410  and playerY <= 500  :  #Написал код чтобы ниндзя запрыгивал на 1 - блок
        playerY  = 450
    elif playerX >= 295 and playerX <= 400 and playerY >= 310 and playerY <= 400:
        playerY = 350
    elif playerX >= 595  and playerX <= 700 and playerY >= 310 and playerY <= 400:    #600,400,100,7
        playerY = 350
    elif playerX >= 295 and playerX <= 400 and playerY >= 110 and playerY <= 200:  # 300, 200, 100, 7
        playerY = 150
    elif playerX >= 595 and playerX <= 700 and playerY >= 110 and playerY <= 200:  # 300, 200, 100, 7
        playerY = 150


    elif playerX >= 445 and playerX <= 550 and playerY >= 110 and playerY <= 200:     #450,200,100,7
        playerY = 150
    elif playerX >= 195  and playerX <= 300 and playerY >= 210 and playerY <= 300:    #200,300,100,7
        playerY = 250
    elif playerX >= 695  and playerX <= 800 and playerY >= 210 and playerY <= 300:    #700,300,100,7
        playerY = 250
    elif playerX >= -5  and playerX <= 100 and playerY >= 10 and playerY <= 100:    #0,100,100,7
        playerY = 50
    elif playerX >= 895  and playerX <= 1000 and playerY >= 10 and playerY <= 100:    #900,100,100,7
        playerY = 50
    elif playerX >= 95 and playerX <= 200 and playerY >= 110 and playerY <= 200:  # 100,200,100,10
        playerY = 150
    elif playerX >= 795 and playerX <= 900 and playerY >= 110 and playerY <= 200:  # 800,200,100,10
        playerY = 150
    else:
        playerY += vel



#Нужно добавить сюда что- то чтобы он запрыгивал на другие блоки



    if playerY >= 550:        #чТОБЫ НЕ ПРОВАЛИЛСЯ
        playerY = 550

    for k in range(num_of_diamonds):


        diamondX[k] += diamondX_change[k]
        if diamondX[k] <= 0:
            diamondX_change[k] = 0
            diamondY[k] += diamondY_change[k]
        elif diamondX[k] >= 736:
            diamondX_change[k] =  0
            diamondY[k] += diamondY_change[k]


        # Столкновение пули и противника
        collision = isCollision(playerX,playerY,diamondX[k], diamondY[k])
        if collision == True:
            explodesound = mixer.Sound('gem.wav')
            explodesound.play()
            score_value += 1
            diamondX[k] = random.randint(0, 736)  # he receives diamond and the diamond changes its position
            diamondY[k] = random.randint(100, 570 )
            if diamondX[k] == 480 and diamondY[i] == 495:
                diamondX[k] = random.randint(0, 900)  # he receives diamond and the diamond changes its position
                diamondY[k] = random.randint(40, 570)
        collision2 = isCollision2(enemyX,enemyY,playerX,playerY)
        if collision2 == True:
            screen.fill((218, 247, 166))
            game_over_text()
            playerX = 4000
            enemyX = 4000
            enemyX_change = 0
            w = 'over'
            s = 'cant'
            pygame.mixer.music.set_volume(0)
            break
        enemyX += enemyX_change
        if enemyX <=  0:
            enemyX_change =  4
            enemyImg = pygame.image.load('ghost.png')
        if enemyX >= 960:
            enemyX_change = -4
            enemyImg = pygame.image.load('ghost2.png')

        enemy(enemyX,enemyY)

        diamond(diamondX[k], diamondY[k], k)
    player(playerX, playerY)
    if w == 'process':
        r()   # platforms
    show_score(textX, textY)
    pygame.display.update()


