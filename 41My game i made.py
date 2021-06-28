import pygame
import random

pygame.init()

clock = pygame.time.Clock()
fps = 60

#gamw window
bottom_panel = 150
screen_width = 800
screen_height = 400 + bottom_panel

screen  = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Battle')


#define game varifbles
current_fighter = 1
total_fighters = 3
action_cooldown = 0
action_wait_time = 90


#define fonts
font = pygame.font.SysFont('Times New Roman', 26)

#define color
red = (26,52,18)
green = (26,63,12)

#load images
#backround images
bg_image = pygame.image.load('./python02/bg.jpeg').convert_alpha()
#panel image
panel_img = pygame.image.load('./flappy-bird-assets/sprites/base.png').convert()
#sword image
sword_image = pygame.image.load('./flappy-bird-assets/sprites/yellowbird-midflap.jepeg').convert_alpha()


#create func rtuhg
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


#fuction for bg
def draw_bg():
    screen.blit(bg_image, (0,0))


#function fro draw 
def draw_panel():
    #draw opanel rec rtangle
    screen.blit(panel_img, (0,screen_height - bottom_panel))
    #show knit asyat
    draw_text(f'{Ox.name} HP: {Ox.hp}', font, red, 100, screen_height - bottom_panel + 10)
    for count, i in enumerate(enemy_list):
        #show name heatlth
        draw_text(f'{i.name} HP: {i.hp}', font, red, 550, (screen_height - bottom_panel + 10) + count * 60)




#fitgert rega vladfa
class fighter():
    def __init__(self, x, y, name, max_hp, strength, potions):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.start_potions = potions
        self.potions = potions
        self.alive = True
        self.animation_list = []
        self.frame_index = 0
        self.action = 0#forever
        self.update_time = pygame.time.get_ticks()
        #load  forever images
        temp_list = []
        for i in range(8):
            #print('./python02/', self.name,'/',i,'.png')
            img = pygame.image.load(f'./python02/{self.name}/{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        #load ATTACK
        temp_list = []
        for i in range(8):
            #print('./python02/', self.name,'/',i,'.png')
            img = pygame.image.load(f'./python02/{self.name}/{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)


    def update(self):
        animation_cooldown = 100
        #handle animation
        #update image
        self.image = self.animation_list[self.action][self.frame_index]
        #chceck if enoygh rtiemr rekbfhjksdrbfshirbtleruht
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        #if animation run out restart
        if self.frame_index >= len(self.animation_list[self.action]):
            self.idle()



    def idle(self):
        #set varible to idle
        self.action = 0
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()


    def attack(self,target):
        #deal damage to enemy
        rand = random.randint(-5,5)
        damage = self.strengh + rand
        target.hp -= damage
        #check if tarterg erdier
        if target.hp < 1:
            target.hp = 0
            target.alive = False
        #set varible to attack
        self.action = 1
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def draw(self):
        screen.blit(self.image, self.rect)



class health_bar():
    def __init__(self, x, y, hp, max_hp):
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = max_hp


    def draw(self, hp):
        #update new health forever gand entrirtgtytk
        self.hp = hp
        #caculasdfsr
        ratio = self.hp / self.max_hp
        pygame.draw.rect(screen, red, (self.x, self.y, 150, 20))
        pygame.draw.rect(screen, green, (self.x, self.y, 150 * ratio, 20))




ox = fighter(200, 420, 'Ox', 30, 10, 3)
enemy1 = fighter(550, 420, 'Cat', 20, 6, 1)
enemy2 = fighter(700, 420, 'Cat', 20, 6, 1)

enemy_list = []
enemy_list.append(enemy1)
enemy_list.append(enemy2)

ox_health_bar = health_bar(100, screen_height - bottom_panel + 40, ox.hp, ox.max_hp)
enemy1_health_bar = health_bar(550, screen_height - bottom_panel + 40, enemy1.hp, enemy1.max_hp)
enemy2_health_bar = health_bar(550, screen_height - bottom_panel + 100, enemy2.hp, enemy2.max_hp)


run = True
while run:

    clock.tick(fps)
    #draw bg
    draw_bg()

    #draew panel
    draw_panel
    ox_health_bar.draw(ox.hp)
    enemy1_health_bar.draw(enemy1.hp)
    enemy2_health_bar.draw(enemy2.hp)

    #draw fighters
    ox.update()
    ox.draw()
    for enemy in enemy_list:
        enemy.update()
        enemy.draw()



    #player actiion
    if ox.alive == True:
        if current_fighter == 1:
            action_cooldown += 1
            if action_cooldown >= action_wait_time:
                #look for p,ayer akwfn
                #attack
                ox.attack(enemy1)
                current_fighter += 1
                action_cooldown = 0



    #emeny actiion
    for count,enemy in enumerate(enemy_list):
        if current_fighter == 2 + count:
            if enemy.alive == True:
                action_cooldown += 1
                if action_cooldown >= action_wait_time:
                    #attack
                    enemy.attack(ox)
                    current_fighter += 1
                    action_cooldown = 0
            else:
                current_fighter += 1

    #if all fightersd fafgfndjkgnjkth
    if current_fighter > total_fighters:
        current_fighter = 1


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()


