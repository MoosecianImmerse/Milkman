#Import Modules
import pygame
import math
from pygame.locals import *

#Initialize Pygame
pygame.init()

#Setup
clock = pygame.time.Clock()
fps = 60
screen_width = 1280
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('The Milkman')

#define game variables

#Show Hitboxes
hitbox = True
#Size of Border Tiles
tile_size = 20
#Function Variables for Player and NPC
game_over = 0
engame_over = 0
#Speed of Playyer
speed = 3
#Angle of NPC Based on Player
npcangle = 0
playerRectx = 0
playerDirection = -2
playerRecty= 0
npcRectx = 0
npcRecty= 0
playerRect = pygame.Rect(0, 0, 30, 30)
npcRect = pygame.Rect(0, 0, 30, 30)
#Talk Suggestion With NPC
CommuneQueue = False
#Communication Suggestion
Space = pygame.image.load('img/CommuneIcon.png')
#Turns one when space pressed. Turns two after. Allows animation.
PressedWait = 0
#Tutorial
tut = pygame.image.load('img/tutorial.png')

#load images

bg_img = pygame.image.load('img/ground.png')
bg_img = pygame.transform.scale(bg_img, (1280, 640))


class Player():
        def __init__(self, x, y):
                self.images_right = []
                self.images_righto = []
                self.images_left = []
                self.images_lefto = []
                self.images_attack = []
                self.images_battack = []
                self.images_lattack = []
                self.images_rattack = []
                self.images_block = []
                self.images_blockl=[]
                self.images_blockr = []
                self.images_blockb = []
                self.index = 0
                self.counter = 0
                img_right = pygame.image.load('img/guy.png')
                for num in range(1, 5):
                        img_right = pygame.image.load('img/guy.png')
                        img_right = pygame.transform.scale(img_right, (30, 30))
                        img_left = pygame.transform.rotate(img_right,180)
                        img_lefto = pygame.transform.rotate(img_right,90)
                        img_righto = pygame.transform.rotate(img_right,270)
                        self.images_right.append(img_right)
                        self.images_righto.append(img_righto)
                        self.images_left.append(img_left)
                        self.images_lefto.append(img_lefto)
                self.image = self.images_right[self.index]
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                self.width = self.image.get_width()
                self.height = self.image.get_height()
                self.vel_y = 0
                self.jumped = False
                self.direction = 0

        def update(self, game_over):
                #globalize neccesary variables
                global event
                global playerRectx
                global playerRecty
                global playerRect
                global engame_over
                global hitbox
                global speed
                global eqa
                global terminate
                global npcRecty
                global npcRectx
                global CommuneQueue
                global PressedWait
                global Space
                plcol = True
                dx = 0
                dy = 0
                (mouseX, mouseY) = pygame.mouse.get_pos()
                walk_cooldown = 5
                

                if game_over == 0:
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        run = False
                        #get keypresses
                        key = pygame.key.get_pressed()
                        event = pygame.event.get()
                        if key[pygame.K_UP]:
                                dy -= speed
                                self.counter += 1
                                self.direction = -2
                                self.vel_y = -1
                                self.image = self.images_right[self.index]
                        if key[pygame.K_DOWN]:
                                dy += speed
                                self.counter += 1
                                self.direction = -1
                                self.vel_y = 1
                                self.image = self.images_left[self.index]
                        if key[pygame.K_LEFT]:
                                dx -= speed
                                self.counter += 1
                                self.direction = 2
                                self.image = self.images_lefto[self.index]
                        if key[pygame.K_RIGHT]:
                                dx += speed
                                self.counter += 1
                                self.direction = 1
                                self.image = self.images_righto[self.index]
                        if key[pygame.K_LEFT] and key[pygame.K_LSHIFT]:
                                dx -= speed * 2
                                self.counter += 1
                                self.direction = 2
                                self.image = self.images_lefto[self.index]
                        if key[pygame.K_RIGHT] and key[pygame.K_LSHIFT]:
                                dx += speed * 2
                                self.counter += 1
                                self.direction = 1
                                self.image = self.images_righto[self.index]
                        if key[pygame.K_UP] and key[pygame.K_LSHIFT]:
                                dy -= speed * 2
                                self.counter += 1
                                self.direction = -2
                                self.vel_y = -1
                                self.image = self.images_right[self.index]
                        if key[pygame.K_DOWN] and key[pygame.K_LSHIFT]:
                                dy += speed * 2
                                self.counter += 1
                                self.direction = -1
                                self.vel_y = 1
                                self.image = self.images_left[self.index]
                        if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False and key[pygame.K_DOWN] and key[pygame.K_UP] :
                                self.counter = 0
                                self.index = 0
                                if self.direction == 1:
                                        self.image = self.images_righto[self.index]
                                if self.direction == -1:
                                        self.image = self.images_left[self.index]
                                if self.direction == -2:
                                        self.image = self.images_left[self.index]
                                if self.direction == 2:
                                        self.image = self.images_lefto[self.index]
                        
                                        

                        #check for collision
                        for tile in world.tile_list:
                                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height) or tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                                        #check for collision in x direction
                                        if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                                                dx = 0
                                        #check for collision in y dircetion
                                        if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                                                dy = 0
                                        #check for border in x and y direction
                                        if self.rect.x + dx > 640:
                                                dx = 0

                        if npcRect.colliderect(self.rect.x + dx, self.rect.y + dy, self.width, self.height):
                                 screen.blit(Space,(npcRectx-30,npcRecty-135))
                                 CommuneQueue = True
                                 dx = 0
                                 dy = 0
                                 key = pygame.key.get_pressed()
                                 if CommuneQueue  == True and key[pygame.K_SPACE]:
                                        Space = pygame.image.load('img/CommunePressed.png')
                                        PressedWait = 1
                                 else:
                                        Space = pygame.image.load('img/CommuneIcon.png')
                                        if PressedWait == 1:
                                                PressedWait = 2

                                                


                        #update player coordinates
                        self.rect.x += dx
                        self.rect.y += dy

                        
                        
                #details what to do once player dies
                if game_over == -1:
                        #creates game over scene
                        screen.fill((0,0,1))
                        pygame.draw.rect(screen, (255, 255,255), pygame.Rect(0, 320, 6000000, 6000))
                        draw_text('GAME OVER!', font, white, (screen_width // 2) - 200, screen_height // 2 - 100)
                        if engame_over == 0:
                                draw_text('Take The L And Search Up A Walkthrough!', font_score, blue, (screen_width // 2)-450, screen_height // 2 + 100)
                        if engame_over == 1:
                                draw_text('Take The L & Search Up A Walkthrough! Or Just Dont Kill', font_score, blue, 0, screen_height // 2 + 100)
                        if self.rect.y > 150:
                                self.rect.y -= 5
                
                                        
                                


                #draw player onto screen
                screen.blit(self.image, self.rect)



                #create global variables for player location
                playerRect = self.rect
                playerRecty = self.rect.y
                playerRectx = self.rect.x
                playerDirection = self.direction
                

                return game_over
                



        
class Npc():
        def __init__(self, x, y):
                global npcangle
                self.images_right = []
                self.images_righto = []
                self.images_left = []
                self.images_lefto = []
                self.images_nw = []
                self.images_ne = []
                self.index = 0
                self.counter = 0
                img_right = pygame.image.load('img/npc.png')
                for num in range(1, 5):
                        img_right = pygame.image.load('img/npc.png')
                        img_right = pygame.transform.scale(img_right, (30, 30))
                        img_left = pygame.transform.rotate(img_right, 180)
                        img_lefto = pygame.transform.rotate(img_right, 270)
                        img_righto = pygame.transform.rotate(img_right, 90)
                        self.images_right.append(img_right)
                        self.images_left.append(img_left)
                        self.images_lefto.append(img_lefto)
                        self.images_righto.append(img_righto)                        
                self.image = self.images_right[self.index]
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                self.width = self.image.get_width()
                self.height = self.image.get_height()
                self.vel_y = 0
                self.jumped = False
                self.direction = 0

        def update(self, engame_over):
                global playerRecty
                global playerRectx
                global playerRect
                global npcangle
                global npcRecty
                global npcRectx
                global npcRect
                
                if engame_over == 0:
                        #calculate angle of view
                        angx = abs(self.rect.x - playerRectx)
                        angy = abs(self.rect.y - playerRecty)
                        hypotnuse = math.sqrt(angy**2+ angx**2)
                        if hypotnuse > 0:
                                npcangle = math.degrees(math.atan(angy/hypotnuse))



                        if playerRecty > npcRecty and npcangle > 22:
                                self.image = self.images_left[self.index]
                        if playerRecty < npcRecty and npcangle > 22:
                                self.image = self.images_right[self.index]
                        if playerRectx > npcRectx and npcangle < 22:
                                self.image = self.images_lefto[self.index]
                        if playerRectx < npcRectx and npcangle < 22:
                                self.image = self.images_righto[self.index]
                 
                        #draw player onto screen
                        screen.blit(self.image, self.rect)
                        npcRect = self.rect
                        npcRecty = self.rect.y
                        npcRectx = self.rect.x
                return engame_over




white = (255, 255, 255)
blue = (101, 137, 255)

font = pygame.font.SysFont('Bauhaus 93', 70)
font_score = pygame.font.SysFont('Bauhaus 93', 50)
font_stats = pygame.font.SysFont('inkfree', 20)

def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

        


class World():
        def __init__(self, data):
                self.tile_list = []
                global hitbox

                #load images
                dirt_img = pygame.image.load('img/stone.png')     

                row_count = 0
                for row in data:
                        col_count = 0
                        for tile in row:
                                if tile == 1:
                                        img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                                        img_rect = img.get_rect()
                                        img_rect.x = col_count * tile_size
                                        img_rect.y = row_count * tile_size
                                        tile = (img, img_rect)
                                        self.tile_list.append(tile)
                                col_count += 1
                        row_count += 1

        def draw(self):
                for tile in self.tile_list:
                        screen.blit(tile[0], tile[1])
                        if hitbox == True:
                                pygame.draw.rect(screen, (255, 0, 0), tile[1], 2)
                                        
                                






world_data = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

world = World(world_data)

#Start of Game
playerFromStart = Player(640, 280)

#SuperMarket


#Housing Districter


#Factory


#Office


#Natural Pasture


#Emissions Farm


#NPC
npc = Npc(670, 560)

#Controls Scene
land = 1
        
def scene1():
        global fps
        global world
        global worlddirection
        global playerRect
        global eagame_over
        global poof
        global game_over
        global playerRectx
        global playerRecty
        global hitbox
        global run
        global npc
        global player
        global event
        global world
        global runn
        global engame_over
        global npcRectx
        global npcRecty
        global PressedWait
        global land
        
        SMCR = pygame.Rect(10, 370, 250, 250)
        HDCR = pygame.Rect(720, 290, 150, 100)
        NPCR = pygame.Rect(1000, 10, 300, 200)
        EFCR = pygame.Rect(720, 10, 270, 200)
        FCR = pygame.Rect(10, 190, 160, 105)
        OCR = pygame.Rect(500, 365, 70, 135)
        
        clock.tick(fps)
        (mouseX, mouseY) = pygame.mouse.get_pos()
        screen.blit(bg_img, (0, 0))
        world.draw()

        if hitbox == True:
                pygame.draw.rect(screen, (255, 255, 255), playerRect, 2)
                pygame.draw.rect(screen, (255, 255, 255), npcRect, 2)

                #Buildings

                #SuperMarket
                pygame.draw.rect(screen, (0,0,255), SMCR, 2)

                #Housing
                pygame.draw.rect(screen, (0,0,255), HDCR, 2)

                #Natural Pasture
                pygame.draw.rect(screen, (0,0,255), NPCR, 2)

                #Emmisions Farm
                pygame.draw.rect(screen, (0,0,255), EFCR, 2)

                #Factory
                pygame.draw.rect(screen, (0,0,255), FCR, 2)

                #Office
                pygame.draw.rect(screen, (0,0,255), OCR, 2)

        if PressedWait == 2:
                land = 2
       
        engame_over = npc.update(engame_over)
        game_over = playerFromStart.update(game_over)

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False

        pygame.display.update()

def tutorial():
        global fps
        global event
        global land
        global tut
        global run
        global PressedWait
        
        clock.tick(fps)
        (mouseX, mouseY) = pygame.mouse.get_pos()
        PressedWait= 0
        
        for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and 70>mouseX >0 and 70 >mouseY> 0:
                        land = 1

        screen.blit(tut,(0,0))
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False

        pygame.display.update()
        
run = True
while run:
        print (land)
        if land == 1:
                scene1()
        if land == 2:
                tutorial()
        if land == 100:
                pygame.quit()
pygame.quit()
