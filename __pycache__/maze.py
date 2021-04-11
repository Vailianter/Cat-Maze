#создай игру "Лабиринт"!
from pygame import *


class GameSprite(sprite.Sprite):
        def __init__(self,player_image,player_x,player_y,player_speed):
                super().__init__()
                self.image = transform.scale(image.load(player_image),(100,100))
                self.speed = player_speed
                self.direction = "left"
                self.rect = self.image.get_rect()
                self.rect.x = player_x
                self.rect.y = player_y
        def reset(self):
                window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
        def update(self):
                keys_pressed = key.get_pressed()
                if keys_pressed[K_UP]:
                        self.rect.y -= 10
                if keys_pressed[K_DOWN]:
                        self.rect.y += 10
                if keys_pressed[K_LEFT]:
                        self.rect.x -= 10
                if keys_pressed[K_RIGHT]:
                        self.rect.x += 10

class Enemy(GameSprite):
        def update(self):
                if self.rect.x <= 250:
                        self.direction = "right"
                elif self.rect.x >= 400:
                        self.direction = "left"
                
                if self.direction == "left":
                        self.rect.x -= 2
                else:
                        self.rect.x += 2

class Enemy_2(GameSprite):
        def update(self):
                if self.rect.y <= 250:
                        self.direction = "up"
                elif self.rect.y >= 400:
                        self.direction = "down"
                
                if self.direction == "down":
                        self.rect.y -= 2
                else:
                        self.rect.y += 2
        

class Wall(sprite.Sprite):
        def __init__(self,color_1,color_2,color_3,wall_x,wall_y,wall_height,wall_width):
               super().__init__()
               self.color_1 =color_1
               self.color_2 =color_2
               self.color_3 =color_3
               self.width =wall_width
               self.height = wall_height
               self.image = Surface((self.width,self.height))
               self.image.fill((color_1,color_2,color_3))
               self.rect = self.image.get_rect()
               self.rect.x = wall_x
               self.rect.y = wall_y
        def draw_wall(self):
                window.blit(self.image,(self.rect.x,self.rect.y))
        


font.init()
font = font.Font(None, 70)
win_width = 700
win_height = 500

window = display.set_mode((win_width,win_height))

display.set_caption(" Cat Лабиринт")
background = transform.scale(image.load("Bg011.png"),(win_width,win_height))

clock = time.Clock()
FPS = 60

mixer.init()
mixer.music.load("BattleTheme5.ogg")
mixer.music.play()

kick = mixer.Sound("kick.ogg")
money = mixer.Sound("money.ogg")
player = Player("jocat.png",600,50,10)
enemy = Enemy("Boss.png",350,300,10)
enemy_2 = Enemy_2("Boss.png",100,200,10)
food = GameSprite("food.png",50,50,10)

wall_1 = Wall(255,0,0,0,500,300,20)
wall_2 = Wall(255,0,0,350,170,130,20)
wall_3 = Wall(255,0,0,200,300,100,20)
wall_4 = Wall(255,0,0,550,0,300,20)

wall_5 = Wall(255,0,0,500,300,20,100)
wall_6 = Wall(255,0,0,350,150,20,200)
wall_7 = Wall(255,0,0,200,0,300,20)

lose = font.render("YOU LOSE FOOD!", True,(255,100,0))

win = font.render("YOU GET FOOD!", True,(255,215,0))

finish = False
game = True
while game:
        for e in event.get():
                if e.type == QUIT:
                        game = False
        if finish != True:
                if sprite.collide_rect(player,food):
                        finish = True
                        money.play()
                        window.blit(win,(200,200))
                window.blit(background,(0,0))
        
                if sprite.collide_rect(player,enemy) or sprite.collide_rect(player,enemy_2) or sprite.collide_rect(player,wall_1) or sprite.collide_rect(player,wall_2) or sprite.collide_rect(player,wall_3) or sprite.collide_rect(player,wall_4) or sprite.collide_rect(player,wall_5) or sprite.collide_rect(player,wall_6) or sprite.collide_rect(player,wall_7):
                        finish = True
                        kick.play()
                        window.blit(lose,(200,200))

                wall_1.draw_wall()
                wall_2.draw_wall()
                wall_3.draw_wall()
                wall_4.draw_wall()
                wall_5.draw_wall()
                wall_6.draw_wall()
                wall_7.draw_wall()
                player.reset()
                enemy.reset()
                enemy.update()
                enemy_2.reset()
                enemy_2.update()
                player.update()
                food.reset()
                display.update()
                clock.tick(FPS)
