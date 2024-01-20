import pygame
import time
import math
import os
import random
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 60
screen_width = 1280
screen_height = 640

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('The Last of Febreeze')

#define game variables
hitbox = False
tile_size = 20
game_over = 0
engame_over = 0
scene = 0
speed = 3
playerDirection = 0
npcangle = 0
score = 0
playerRectx = 0
playerDirection = -2
playerRecty= 0
npcRectx = 0
npcRecty= 0
playerRect = pygame.Rect(0, 0, 20, 20)
npcRect = pygame.Rect(0, 0, 20, 20)


#load images

bg_img = pygame.image.load('img/ground.png')


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
                        img_block = pygame.image.load('img/guyb.png')
                        img_blockb = pygame.transform.rotate(img_block,180)
                        img_blockl = pygame.transform.rotate(img_block,90)
                        img_blockr = pygame.transform.rotate(img_block,270)
                        img_right = pygame.transform.scale(img_right, (40, 40))
                        img_left = pygame.transform.rotate(img_right,180)
                        img_attack = pygame.image.load('img/guya.png')
                        img_battack = pygame.transform.rotate(img_attack,180)
                        img_lattack = pygame.transform.rotate(img_attack,90)
                        img_rattack = pygame.transform.rotate(img_attack,270)
                        img_lefto = pygame.transform.rotate(img_right,90)
                        img_righto = pygame.transform.rotate(img_right,270)
                        self.images_block.append(img_block)
                        self.images_blockr.append(img_blockr)
                        self.images_blockl.append(img_blockl)
                        self.images_blockb.append(img_blockb)
                        self.images_right.append(img_right)
                        self.images_attack.append(img_attack)
                        self.images_battack.append(img_battack)
                        self.images_lattack.append(img_lattack)
                        self.images_rattack.append(img_rattack)
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
                plcol = True
                dx = 0
                dy = 0
                (mouseX, mouseY) = pygame.mouse.get_pos()
                walk_cooldown = 5
                

                if game_over == 0:
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

                                                


                        #update player coordinates
                        if dx > 0:
                                chasex = self.rect.x -50
                        if dy > 0:
                                chasey = self.rect.y -50
                        if dx < 0:
                                chasex = self.rect.x +50
                        if dy < 0:
                                chasey = self.rect.y +50
                        if dx == 0:
                                chasex = self.rect.x
                        if dy == 0:
                                chasey = self.rect.y
                        if dx == 0 and dy == 0:
                                chasey = 30000
                        
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
                        img_left = pygame.transform.rotate(img_right, 180)
                        img_lefto = pygame.transform.rotate(img_right, 270)
                        img_righto = pygame.transform.rotate(img_right, 90)
                        img_right = pygame.transform.scale(img_right, (40, 40))
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
                global scene
                global hitbox

                #load images
                dirt_img = pygame.image.load('img/stone.png')
                grass_img = pygame.image.load('img/wood.png')
                roof_img = pygame.image.load('img/roof.png')               

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
                                if tile == 2:
                                        img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                                        img_rect = img.get_rect()
                                        img_rect.x = col_count * tile_size
                                        img_rect.y = row_count * tile_size
                                        tile = (img, img_rect)
                                        self.tile_list.append(tile)
                                if tile == 3:
                                        img = pygame.transform.scale(roof_img, (tile_size, tile_size))
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
                                pygame.draw.rect(screen, (255, 255, 255), tile[1], 2)
                                        
                                






world_data = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 4, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 0, 0, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
player = Player(1200, 280)
npc = Npc(300, 250)
npc2 = Npc(860, 340)
npc1 = Npc(860, 340)
player2 = Player (10, 280)
player4 = Player(20, 280)
player6 = Player(20, 280)
player7 = Player(20, 280)
player8 = Player(20, 280)
player9 = Player(20, 280)


world = World(world_data)


        

                        
#If approach is from:
#Top, then direction = 1
#Bottom, then direction = 2
#Right side side, then direction = 3
#Left side, then direction = 4
# Refrence to the destination, not point of origin

player = Player(1200, 280)
npc = Npc(280, 260)
        
def scene1():
        global scene
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
        global npc
        global player
        global event
        global score
        global world
        global runn
        global eqa
        global engame_over
        clock.tick(fps)
        scene = 1
        (mouseX, mouseY) = pygame.mouse.get_pos()
        screen.blit(bg_img, (0, 0))
        world.draw()
        
        if hitbox == True:
                pygame.draw.rect(screen, (255, 255, 255), playerRect, 2)
                pygame.draw.rect(screen, (255, 255, 255), npcRect, 2)


                        
        engame_over = npc.update(engame_over)
        game_over = player.update(game_over)

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False

        pygame.display.update()




run = True
while run:
        scene1()
pygame.quit()
