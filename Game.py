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
pygame.display.set_caption('Mooventure')

#define game variables
#Cursor Variables
CursorRect = (0, 0, 20, 20)
CursorRecty = 0
CursorRectx = 0
#If False, Robe, If True, Suit
Suit = False
#Show Hitboxes
hitbox = False
#Checks for SPace
clicked = True
#CursorCount Counts and Disappears Cursor
CursCon = 0
#Running
Running = True
#Cursor BVariable
came_over = 0
#Spot
Spot = 0
#Size of Border Tiles
tile_size = 20
#Function Variables for Player and NPC
game_over = 0
engame_over = 0
#Speed of Playyer
speed = 2.5
#Angle of NPC Based on Player
npcangle = 0
playerRectx = 0
playerDirection = -2
playerRecty= 0
npcRectx = 0
npcRecty= 0
playerRect = pygame.Rect(0, 0, 35, 35)
npcRect = pygame.Rect(0, 0, 35, 35)
#Talk Suggestion With NPC
CommuneQueue = False
#Calculation Variables
EmmisionDeals = 0
NaturalDeals = 0
EmmisionRates = 30
NaturalRates = 30
Workers = 0
Houses = 2
LayedOff = 0
AssemblyLines = 0
#Money 
Money = 0
#Communication Suggestion
Space = pygame.image.load('img/CommuneIcon.png')
#Turns one when space pressed. Turns two after. Allows animation.
PressedWait = 0
#Tutorial
tut = pygame.image.load('img/tutorial.png')

#load images

bg_img = pygame.image.load('img/BackG.jpg')
bg_img = pygame.transform.scale(bg_img, (1280, 640))

Stopo = False



class Cursor():
        def __init__(self, x, y):
                self.images_right = []
                self.images_righto = []
                self.images_left = []
                self.images_lefto = []
                self.index = 0
                self.counter = 0
                img_right = pygame.image.load('img/Cursor.png')
                for num in range(1, 5):
                        img_right = pygame.image.load('img/Cursor.png')
                        img_left = pygame.image.load('img/CursorClick.png')
                        self.images_right.append(img_right)
                        self.images_left.append(img_left)
                self.image = self.images_right[self.index]
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                self.width = self.image.get_width()
                self.height = self.image.get_height()
                self.vel_y = 0
                self.jumped = False
                self.direction = 0

        def update(self, came_over):
                #globalize neccesary variables
                global event
                global hitbox
                global CursorRect
                global CursorRecty
                global CursorRectx
                global clicked
                global run
                global CursCon
                cursorspeed = 5
                dx = 0
                dy = 0
                (mouseX, mouseY) = pygame.mouse.get_pos()
                

                if came_over == 0:
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        run = False
                        #get keypresses
                        key = pygame.key.get_pressed()
                        event = pygame.event.get()
                        if key[pygame.K_UP]:
                                dy -= cursorspeed
                                self.counter += 1
                                self.direction = -2
                                self.vel_y = -1
                                CursCon = 0
                        if key[pygame.K_DOWN]:
                                dy += cursorspeed
                                self.counter += 1
                                self.direction = -1
                                self.vel_y = 1
                                CursCon = 0
                        if key[pygame.K_LEFT]:
                                dx -= cursorspeed
                                self.counter += 1
                                self.direction = 2
                                CursCon = 0
                        if key[pygame.K_RIGHT]:
                                dx += cursorspeed
                                self.counter += 1
                                self.direction = 1
                                CursCon = 0
                        if key[pygame.K_SPACE]:
                                self.image = self.images_left[self.index]
                                clicked = True
                                CursCon = 0
                        else:
                                self.image = self.images_right[self.index]
                                clicked = False
                        if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False and key[pygame.K_DOWN] == False and key[pygame.K_UP] == False:
                                CursCon += 1
                        

                        #update player coordinates
                        self.rect.x += dx
                        self.rect.y += dy
                
                                        
                                

                if CursCon < 600:
                        #draw player onto screen
                        screen.blit(self.image, self.rect)



                #create global variables for player location
                CursorRect = self.rect
                CursorRecty = self.rect.y
                CursorRectx = self.rect.x
                CursorDirection = self.direction
                

                return came_over





class Player():
        def __init__(self, x, y):
                self.images_right = []
                self.images_righto = []
                self.images_left = []
                self.images_lefto = []
                self.index = 0
                self.counter = 0
                if Suit:
                        img_right = pygame.image.load('img/Back.png')
                else: 
                        img_right = pygame.image.load('img/BackBusi.png')
                for num in range(1, 5):
                        if Suit:
                                img_right = pygame.image.load('img/FrontBusi.png')
                                img_left = pygame.image.load('img/BackBusi.png')
                                img_lefto = pygame.image.load('img/SideBusi.png')
                        else:
                                img_right = pygame.image.load('img/Front.png')
                                img_left = pygame.image.load('img/Back.png')
                                img_lefto = pygame.image.load('img/Side.png')
                        img_righto = pygame.transform.flip(img_lefto,True,False)
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
                global npcRecty
                global npcRectx
                global CommuneQueue
                global PressedWait
                global Space
                global run
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
                        if key[pygame.K_w]:
                                dy -= speed
                                self.counter += 1
                                self.direction = -2
                                self.vel_y = -1
                                self.image = self.images_right[self.index]
                        if key[pygame.K_s]:
                                dy += speed
                                self.counter += 1
                                self.direction = -1
                                self.vel_y = 1
                                self.image = self.images_left[self.index]
                        if key[pygame.K_a]:
                                dx -= speed
                                self.counter += 1
                                self.direction = 2
                                self.image = self.images_lefto[self.index]
                        if key[pygame.K_d]:
                                dx += speed
                                self.counter += 1
                                self.direction = 1
                                self.image = self.images_righto[self.index]
                        if key[pygame.K_d] == False and key[pygame.K_a] == False and key[pygame.K_s] and key[pygame.K_w] :
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
black = (0,0,0)
blue = (101, 137, 255)

font = pygame.font.Font('Fonts/Alphakind.ttf', 32)
font_score = pygame.font.SysFont('Fonts/Alphakind.ttf', 50)
font_stats = pygame.font.SysFont('Fonts/Alphakind.ttf', 24)

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
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

        

def night():
        global EmmisionDeals 
        global NaturalDeals
        global EmmisionRates
        global NaturalRates
        global Workers
        global Houses
        global LayedOff
        global AssemblyLines
        MilkDeals = EmmisionDeals + NaturalDeals
        MilkPay = (EmmisionDeals * EmmisionRates) + (NaturalDeals * NaturalRates)
        if Workers/1000 > Houses:
                LayedOff = (Houses*1000) - Workers
                Workers = Workers - LayedOff
        while AssemblyLines < Workers/1000:
                AssemblyLines = AssemblyLines - 1
        




world = World(world_data)

curse = Cursor(640,320)
#Start of Game
playerFromStart = Player(625, 280)

#SuperMarket


#Housing Districter


#Factory


#Office


#Natural Pasture


#Emissions Farm


#NPC
npc = Npc(670, 560)

#Controls Scene
land = 0

set = pygame.image.load('Img/Settings.png')
Sole = False
Gol = False

def title():
        global set
        global fps
        global event
        global Sole
        global Gol
        global land
        global run
        global Spot
        global Money
        global came_over
        global CursorRect
        global CursorRectx
        global CursorRecty
        global Clicked
        backgr = pygame.image.load('img/titlest.jpg')
        screen.blit(backgr, (0, 0))
        
        clock.tick(fps)
        (mouseX, mouseY) = pygame.mouse.get_pos()
        white = (255, 255, 255)
        black = (0,0,0)
        blue = (101, 137, 255)

        font = pygame.font.Font('Fonts/Alphakind.ttf', 72)
        font2 = pygame.font.Font('Fonts/Alphakind.ttf', 152)

        draw_text('Mooventure', font2, white, 190, -10)
        draw_text('Play', font, white, 545, 435)
        PlayRect = pygame.Rect(520, 420, 200, 120)
        pygame.draw.rect(screen, (255, 255, 255), PlayRect, 2)
        screen.blit(set,(1200,560))
        

        for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and 720> mouseX >520 and 540>mouseY> 420:
                        land = 1
                if event.type == pygame.QUIT:
                        run = False
                if 720> CursorRectx >520 and 540>CursorRecty> 420 and clicked == True:
                        land = 1
                if 1280> CursorRectx >1200 and 640>CursorRecty> 560 and clicked == True:
                        set = pygame.transform.rotate(set,90)
                        Gol = True
                if event.type == pygame.MOUSEBUTTONDOWN and 1280> mouseX >1200 and 640>mouseY> 560:
                        set = pygame.transform.rotate(set,90)
                        Gol =True

                if Sole == True:
                        land = 1
                        Sole = False
                if Gol:
                        Sole = True
                        Gol = False
        came_over = curse.update(came_over)

        pygame.display.update()  
        
def scene1():
        global fps
        global world
        global playerRect
        global game_over
        global playerRectx
        global playerRecty
        global hitbox
        global run
        global npc
        global Stopo
        global event
        global world
        global engame_over
        global npcRectx
        global npcRecty
        global PressedWait
        global land
        global came_over
        global Spot
        global playerFromStart

        font = pygame.font.Font('Fonts/Alphakind.ttf', 72)
        font2 = pygame.font.Font('Fonts/Alphakind.ttf', 132)
        font3 = pygame.font.Font('Fonts/Alphakind.ttf', 57)

        if Spot == 2:
                playerFromStart = Player(580,400)
                Spot = 0
        elif Spot == 3:
                playerFromStart = Player(260,480)
                Spot = 0
        SMCR = pygame.Rect(10, 370, 250, 250)
        HDCR = pygame.Rect(710, 290, 150, 100)
        NPCR = pygame.Rect(1000, 10, 300, 200)
        EFCR = pygame.Rect(720, 10, 270, 200)
        FCR = pygame.Rect(10, 190, 160, 105)
        OCR = pygame.Rect(500, 365, 70, 135)
        
        clock.tick(fps)
        (mouseX, mouseY) = pygame.mouse.get_pos()
        screen.blit(bg_img, (0, 0))
        Stop = pygame.image.load('img/Stop.png')
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False
                if key[pygame.K_ESCAPE]:
                        Stopo = True
        if Stopo:
                screen.blit(Stop,(0,0))
                draw_text('Title', font, white, 545, 435)
                draw_text('Resume', font3, white, 521, 245)
                draw_text('Paused', font2, white, 400, 35)
                PlayRect = pygame.Rect(520, 420, 200, 120)
                PlayRect2 = pygame.Rect(520, 220, 200, 120)
                pygame.draw.rect(screen, (255, 255, 255), PlayRect, 2)
                pygame.draw.rect(screen, (255, 255, 255), PlayRect2, 2)
                key = pygame.key.get_pressed()
                for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN and 720> mouseX >520 and 540>mouseY> 420:
                                Stopo = False
                                land = 0
                        if event.type == pygame.MOUSEBUTTONDOWN and 720> mouseX >520 and 340>mouseY> 220:
                                Stopo = False
                        if 720> CursorRectx >520 and 540>CursorRecty> 420 and clicked == True:
                                Stopo = False
                                land = 0
                        if 720> CursorRectx >520 and 340>CursorRecty> 220 and clicked == True:
                                Stopo = False
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
        if Stopo == False:
                engame_over = npc.update(engame_over)
                game_over = playerFromStart.update(game_over)

        if PressedWait == 2:
                land = 2

        if playerRect.colliderect(OCR):
                land = 3
        if playerRect.colliderect(SMCR):
                land = 4

        came_over = curse.update(came_over)



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
                if event.type == pygame.QUIT:
                        run = False

        screen.blit(tut,(0,0))
        


        pygame.display.update()

run = True
while run:
        if land == 0:
                title()
        if land == 1:
                scene1()
        if land == 2:
                tutorial()
        if land == 100:
                pygame.quit()
pygame.quit()
