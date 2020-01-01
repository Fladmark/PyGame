import pygame
from random import *
import sys

pygame.init()

screenWidth = 768
screenHeight = 368
widthSprite = 37
heightSprite = 50
item_out_of_range = []
item_hit = []
backgroundCounter = 0
create_counter = 0
marked_item = []
list_of_dummies = []

win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Adventure")
background = pygame.image.load(f"pictures/forest.png")
background = pygame.transform.flip(background, True, False)

background_frames = [
    pygame.image.load("gif/frame_0_delay-0.11s.png"),
    pygame.image.load("gif/frame_1_delay-0.11s.png"),
    pygame.image.load("gif/frame_2_delay-0.11s.png"),
    pygame.image.load("gif/frame_3_delay-0.11s.png"),
    pygame.image.load("gif/frame_4_delay-0.11s.png"),
    pygame.image.load("gif/frame_5_delay-0.11s.png"),
    pygame.image.load("gif/frame_6_delay-0.11s.png"),
    pygame.image.load("gif/frame_7_delay-0.11s.png")
]

walkRight = [
    pygame.image.load("character/adventurer-run3-00.png"),
    pygame.image.load("character/adventurer-run3-01.png"),
    pygame.image.load("character/adventurer-run3-02.png"),
    pygame.image.load("character/adventurer-run3-03.png"),
    pygame.image.load("character/adventurer-run3-04.png"),
    pygame.image.load("character/adventurer-run3-05.png")
]
walkLeft = []
for item in walkRight:
    x = pygame.transform.flip(item, True, False)
    walkLeft.append(x)

still_right = [
    pygame.image.load("character/adventurer-idle-2-00.png"),
    pygame.image.load("character/adventurer-idle-2-01.png"),
    pygame.image.load("character/adventurer-idle-2-02.png"),
    pygame.image.load("character/adventurer-idle-2-03.png")
]
still_left = []
for item in still_right:
    x = pygame.transform.flip(item, True, False)
    still_left.append(x)

attack_right = [
    pygame.image.load("character/adventurer-attack1-00.png"),
    pygame.image.load("character/adventurer-attack1-01.png"),
    pygame.image.load("character/adventurer-attack1-02.png"),
    pygame.image.load("character/adventurer-attack1-03.png"),
    pygame.image.load("character/adventurer-attack1-04.png"),
    pygame.image.load("character/adventurer-attack2-00.png")
]
attack_left = []
for item in attack_right:
    x = pygame.transform.flip(item, True, False)
    attack_left.append(x)

attack_right_1 = [
    pygame.image.load("character/adventurer-attack2-00.png"),
    pygame.image.load("character/adventurer-attack2-01.png"),
    pygame.image.load("character/adventurer-attack2-02.png"),
    pygame.image.load("character/adventurer-attack2-03.png"),
    pygame.image.load("character/adventurer-attack2-04.png"),
    pygame.image.load("character/adventurer-attack2-05.png")
]
attack_left_1 = []
for item in attack_right_1:
    x = pygame.transform.flip(item, True, False)
    attack_left_1.append(x)

attack_right_2 = [
    pygame.image.load("character/adventurer-attack3-00.png"),
    pygame.image.load("character/adventurer-attack3-01.png"),
    pygame.image.load("character/adventurer-attack3-02.png"),
    pygame.image.load("character/adventurer-attack3-03.png"),
    pygame.image.load("character/adventurer-attack3-04.png"),
    pygame.image.load("character/adventurer-attack3-05.png")
]
attack_left_2 = []
for item in attack_right_2:
    x = pygame.transform.flip(item, True, False)
    attack_left_2.append(x)

jump_right = [
    pygame.image.load("character/adventurer-jump-00.png"),
    pygame.image.load("character/adventurer-jump-01.png"),
    pygame.image.load("character/adventurer-jump-02.png"),
    pygame.image.load("character/adventurer-jump-03.png")
]
jump_left = []
for item in jump_right:
    x = pygame.transform.flip(item, True, False)
    jump_left.append(x)

spin_right = [
    pygame.image.load("character/adventurer-smrslt-00.png"),
    pygame.image.load("character/adventurer-smrslt-01.png"),
    pygame.image.load("character/adventurer-smrslt-02.png"),
    pygame.image.load("character/adventurer-smrslt-03.png")
]
spin_left = []
for item in spin_right:
    x = pygame.transform.flip(item, True, False)
    spin_left.append(x)

fall_right = [
    pygame.image.load("character/adventurer-fall-00.png"),
    pygame.image.load("character/adventurer-fall-01.png")
]
fall_left = []
for item in fall_right:
    x = pygame.transform.flip(item, True, False)
    fall_left.append(x)

bow_right = [
    pygame.image.load("character/adventurer-bow-00.png"),
    pygame.image.load("character/adventurer-bow-01.png"),
    pygame.image.load("character/adventurer-bow-02.png"),
    pygame.image.load("character/adventurer-bow-03.png"),
    pygame.image.load("character/adventurer-bow-04.png"),
    pygame.image.load("character/adventurer-bow-05.png"),
    pygame.image.load("character/adventurer-bow-06.png"),
    pygame.image.load("character/adventurer-bow-07.png"),
    pygame.image.load("character/adventurer-bow-08.png"),
    pygame.image.load("character/adventurer-bow-01.png"),
    pygame.image.load("character/adventurer-bow-00.png")
]
bow_left = []
for item in bow_right:
    x = pygame.transform.flip(item, True, False)
    bow_left.append(x)

golem_right = [
    pygame.image.load("pictures/golem/tile000.png"),
    pygame.image.load("pictures/golem/tile001.png"),
    pygame.image.load("pictures/golem/tile002.png"),
    pygame.image.load("pictures/golem/tile003.png"),
    pygame.image.load("pictures/golem/tile004.png"),
    pygame.image.load("pictures/golem/tile005.png"),
    pygame.image.load("pictures/golem/tile006.png")
]
golem_left = []
for item in golem_right:
    x = pygame.transform.flip(item, True, False)
    golem_left.append(x)

dummy_frames_left = [
    # pygame.image.load("character/dummy(8).png"),
    # pygame.image.load("character/dummy(7).png"),
    pygame.image.load("character/dummy(6).png"),
    pygame.image.load("character/dummy(7).png"),
    pygame.image.load("character/dummy(7).png"),
    pygame.image.load("character/dummy(8).png"),
    pygame.image.load("character/dummy(8).png")
]

dummy_frames_right = [
    # pygame.image.load("character/dummy(8).png"),
    # pygame.image.load("character/dummy(1).png"),
    pygame.image.load("character/dummy(2).png"),
    pygame.image.load("character/dummy(1).png"),
    pygame.image.load("character/dummy(1).png"),
    pygame.image.load("character/dummy(8).png"),
    pygame.image.load("character/dummy(8).png")
]
dummy_frame_still = [
    pygame.image.load("character/dummy(8).png")
]
hp_bar_frame = pygame.image.load("pictures/hpbar.png")

clock = pygame.time.Clock()


class Player(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.vel = 7
        self.isJump = False
        self.jumpCount = 8
        self.left = False
        self.right = False
        self.attack = False
        self.ranged_attack = False
        self.walkCount = 0
        self.stillCount = 0
        self.attackCount = 0
        self.bowCount = 0
        self.last_direction = 1
        self.next_attack = 0
        self.tics_since_attack = 0
        self.attacked_normal = False
        self.attacked_power = False
        self.sword_hit = False

    def draw(self, window):
        if self.walkCount + 1 >= 18:
            self.walkCount = 0
        if self.stillCount + 1 >= 16:
            self.stillCount = 0
        if self.attackCount + 1 >= 12:
            self.attackCount = 0
        if self.bowCount + 1 >= 10:
            self.bowCount = 0

        if self.isJump:
            if self.last_direction == -1 and self.jumpCount <= -4:
                window.blit(fall_left[abs(self.jumpCount) % 2], (self.x, self.y))
            elif self.last_direction == 1 and abs(self.jumpCount) <= -4:
                window.blit(fall_right[abs(self.jumpCount) % 2], (self.x, self.y))
            elif self.last_direction == -1 and abs(self.jumpCount) < 4:
                window.blit(spin_left[abs(self.jumpCount) % 4], (self.x, self.y))
            elif self.last_direction == 1 and abs(self.jumpCount) < 4:
                window.blit(spin_right[abs(self.jumpCount) % 4], (self.x, self.y))
            elif self.last_direction == -1:
                window.blit(jump_left[abs(self.jumpCount) % 4], (self.x, self.y))
            elif self.last_direction == 1:
                window.blit(jump_right[abs(self.jumpCount) % 4], (self.x, self.y))

        elif self.attack:
            if self.next_attack == 0:
                if self.last_direction == -1:
                    window.blit(attack_left_1[self.attackCount // 2], (self.x, self.y))
                elif self.last_direction == 1:
                    window.blit(attack_right_1[self.attackCount // 2], (self.x, self.y))

                self.attackCount += 1

            elif self.next_attack == 1:
                if self.last_direction == -1:
                    window.blit(attack_left[self.attackCount // 2], (self.x, self.y))
                elif self.last_direction == 1:
                    window.blit(attack_right[self.attackCount // 2], (self.x, self.y))
                self.attackCount += 1

            elif self.next_attack == 2:
                if self.last_direction == -1:
                    window.blit(attack_left_2[self.attackCount // 2], (self.x, self.y))
                elif self.last_direction == 1:
                    window.blit(attack_right_2[self.attackCount // 2], (self.x, self.y))
                self.attackCount += 1

            if self.attackCount == 11:
                self.attack = False
                if self.next_attack == 2:
                    self.next_attack = 0
                else:
                    self.next_attack += 1

            if self.attackCount == 6:
                self.sword_hit = True
            else:
                self.sword_hit = False

            self.tics_since_attack = 0
            self.bowCount = 0

        elif self.ranged_attack:
            if self.last_direction == -1:
                window.blit(bow_left[self.bowCount // 1], (self.x, self.y))
            if self.last_direction == 1:
                window.blit(bow_right[self.bowCount // 1], (self.x, self.y))
            self.bowCount += 1

            if self.bowCount == 9:
                self.ranged_attack = False



        elif self.left:
            window.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            window.blit(walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            if self.last_direction == -1:
                window.blit(still_left[self.stillCount // 4], (self.x, self.y))
            elif self.last_direction == 1:
                window.blit(still_right[self.stillCount // 4], (self.x, self.y))
            self.stillCount += 1

# Avoid combo attacks if set time since last attack
        self.tics_since_attack += 1
        if self.tics_since_attack > 15:
            self.next_attack = 0
            self.tics_since_attack = 0

class Golem(object):

    def __init__(self, x, y, boss=False):
        self.x = x
        self.y = y
        self.width = 128
        self.height = 128
        self.speed = 1
        self.walkCount = 0
        self.left = False
        self.right = True
        self.last_direction = 1
        self.boss = boss

    def draw(self, window):
        bar_width = 406
        bar_height = 56
        red_width = 400
        red_height = 50
        red_hp_width = red_width
        if self.walkCount == 28:
            self.walkCount = 0

        if fighter.x + fighter.width/2 > self.x + self.width/2:
            self.right = True
            self.left = False
        elif fighter.x + fighter.width/2 <= self.x + self.width/2:
            self.left = True
            self.right = False

        if self.left:
            window.blit(golem_left[self.walkCount // 4], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            window.blit(golem_right[self.walkCount // 4], (self.x, self.y))
            self.walkCount += 1

        if self.left:
            self.x -= self.speed
        elif self.right:
            self.x += self.speed

        if self.boss:
            window.blit(hp_bar_frame,(screenWidth/2 - bar_width/2, 50))
            pygame.draw.rect(window, (255,255,255), (screenWidth/2 + (bar_width-red_width)/2 - bar_width/2,
                                                     (bar_height-red_height)/2 + red_height, red_hp_width, red_height))




class Projectile(object):

    def __init__(self, x, y, width, color, direction, character_width=48):
        self.x = x
        self.y = y
        self.width = width
        self.color = color
        self.direction = direction
        self.vel = 30 * direction
        self.out_of_range = []
        self.character_width = character_width

    def draw(self, window):
        pygame.draw.line(window, self.color, (round(self.x) + self.character_width/2, round(self.y)),
                        (round(self.x + self.character_width/2 + self.width*self.direction), round(self.y)), 2)


class Button(object):

    def __init__(self, x, y, width, height, centered=False, text=""):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.centered = centered
        self.boarder = 2
        self.counter = 0


    def draw(self, window):
        global menu
        global run
        global pause
        if self.centered:
            self.x = screenWidth/2 - self.width/2

        pygame.draw.rect(window, (0, 0, 0), (self.x - self.boarder, self.y - self.boarder,
                                             self.width + self.boarder * 2, self.height + self.boarder * 2))
        pygame.draw.rect(window, (180,191,109), (self.x, self.y, self.width, self.height))

        if self.x < pygame.mouse.get_pos()[0] < self.x + self.width and self.y < pygame.mouse.get_pos()[1] < self.y + self.height:
            pygame.draw.rect(window, (68,135,0), (self.x, self.y, self.width, self.height))
            if (pygame.mouse.get_pressed()[0] == 1) and self.text == "START":
                menu = False
            elif (pygame.mouse.get_pressed()[0] == 1) and self.text == "EXIT":
                sys.exit()
            elif (pygame.mouse.get_pressed()[0] == 1) or self.counter == 1 and self.text == "CONTINUE":
                pause = False


        font = pygame.font.SysFont('papyrus', 30)
        text = font.render(self.text, 1, (0, 0, 0))
        win.blit(text, (self.x + (self.width - text.get_rect().width)/2, self.y + (self.height - text.get_rect().height)/2, self.width, self.height))





# list of buttons below
b = Button(100, 100, 200, 75, True, "START")
c = Button(100, 200, 200, 75, True, "EXIT")
d = Button(100, 100, 250, 75, True, "CONTINUE")


class Dummy(object):

    def __init__(self, x, y, width=48, height=48):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hit_left = False
        self.hit_right = False
        self.hitCounter = 0
        self.clicked = False
        self.clicked_list = [0, 0]
        self.fall = 1
        self.marked = False

    def draw(self, window):
        global marked_item

        if self.hit_left:
            window.blit(dummy_frames_left[self.hitCounter // 1], (self.x, self.y))
        elif self.hit_right:
            window.blit(dummy_frames_right[self.hitCounter // 1], (self.x, self.y))
        else:
            window.blit(dummy_frame_still[0], (self.x, self.y))

        if self.hit_right or self.hit_left:
            self.hitCounter += 1
            if self.hitCounter == 5:
                self.hit_left = False
                self.hit_right = False
                self.hitCounter = 0

        if (pygame.mouse.get_pressed()[0] == 1):
            self.clicked_list.append(1)
        else:
            self.clicked_list.append(0)
        if (self.clicked_list[0] == 0 and self.clicked_list[1] == 1 and self.clicked == False and self.x <
           pygame.mouse.get_pos()[0] < self.x + self.width and self.y < pygame.mouse.get_pos()[1] < self.y + self.width):
            self.clicked = True
            marked_item.append(self)
        elif self.clicked_list[0] == 0 and self.clicked_list[1] == 1 and self.clicked:
            self.clicked = False
            marked_item = []

        if len(self.clicked_list) == 3:
            self.clicked_list.pop(0)

        if self.clicked and len(marked_item) > 0:
            if marked_item[0] == self:
                self.marked = True
                self.x = pygame.mouse.get_pos()[0] - 24
                self.y = pygame.mouse.get_pos()[1] - 24
        else:
            self.marked = False
            if self.y < 290:
                self.y += self.fall
                self.fall += 3
            else:
                self.y = 305
                self.fall = 1

        for projectile in projectiles:
            if fighter.x + fighter.width/2 > self.x + self.width/2:
                if (self.x + self.width/2 - 16 < projectile.x < self.x + self.width/2 + 15 and
                   self.y < projectile.y < self.y + self.height):
                    self.hit_right = True
                    item_hit.append(projectile)
            elif fighter.x + fighter.width/2  < self.x + self.width/2:
                if (self.x + self.width/2 - 16 < projectile.x  + 20 < self.x + self.width/2 + 15 and
                   self.y < projectile.y < self.y + self.height):
                    self.hit_left = True
                    item_hit.append(projectile)

        # if fighter.sword_hit:
        #     print(fighter.x + fighter.width/2)
        #     print(self.x + self.width/2)
        #     if fighter.x + fighter.width/2 > self.x + self.width/2:
        #         if (fighter.x + fighter.width/2 > self.x + self.width/2 > (fighter.x + fighter.width/2) + ((fighter.width)*fighter.last_direction) and
        #                 fighter.y < self.y + self.height/2 < fighter.y + fighter.height):
        #             self.hit_right = True
        #     elif fighter.x + fighter.width/2 < self.x + self.width / 2:
        #         if (fighter.x + fighter.width/2 < self.x + self.width/2 < (fighter.x + fighter.width/2) + ((fighter.width)*fighter.last_direction) and
        #                 fighter.y < self.y + self.height/2 < fighter.y + fighter.height):
        #             self.hit_left = True

        if fighter.sword_hit:
            print(fighter.x + fighter.width/2)
            print(self.x + self.width/2)
            if fighter.x > self.x:
                if (fighter.x + fighter.width/2 > self.x + self.width/2 > (fighter.x + fighter.width/2) + ((fighter.width)*fighter.last_direction) and
                        fighter.y < self.y + self.height/2 < fighter.y + fighter.height):
                    self.hit_right = True
            elif fighter.x < self.x:
                if (fighter.x + fighter.width/2 < self.x + self.width/2 < (fighter.x + fighter.width/2) + ((fighter.width)*fighter.last_direction) and
                        fighter.y < self.y + self.height/2 < fighter.y + fighter.height):
                    self.hit_left = True

def none():
    pass

def create_dummies():
    global list_of_dummies
    global create_counter
    if create_counter == 0:
        x = Dummy(pygame.mouse.get_pos()[0] - 24, pygame.mouse.get_pos()[1] - 24)
        list_of_dummies.append(x)
        create_counter += 1
    elif create_counter == 20:
        create_counter = 0
    else:
        create_counter += 1

def delete_dummy():
    global list_of_dummies
    dummies_deleted = []
    for dummy in list_of_dummies:
        if dummy.marked == True:
            dummies_deleted.append(dummy)
    list_of_dummies = [x for x in list_of_dummies if x not in dummies_deleted]

def mass_delete():
    global list_of_dummies
    dummies_deleted = []
    for dummy in list_of_dummies:
        dummies_deleted.append(dummy)
    list_of_dummies = [x for x in list_of_dummies if x not in dummies_deleted]


def draw_game_window():
    global backgroundCounter
    win.blit(background_frames[backgroundCounter // 3], (0, 0))

    if backgroundCounter == 21:
        backgroundCounter = 0
    else:
        backgroundCounter += 1
    for dummy in list_of_dummies:
        dummy.draw(win)
    fighter.draw(win)
    for projectile in projectiles:
        projectile.draw(win)
    g.draw(win)
    pygame.display.update()

g = Golem(screenWidth + 20, 270, True)
fighter = Player(20, 315, widthSprite, heightSprite)
run = True
projectiles = []
menu = True
pause = False
while run:
    while menu:
        clock.tick(30)
        win.blit(background_frames[backgroundCounter // 3], (0, 0))
        b.draw(win)
        c.draw(win)

        if backgroundCounter == 21:
            backgroundCounter = 0
        else:
            backgroundCounter += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
    while pause:
        clock.tick(30)
        d.draw(win)
        c.draw(win)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()

    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for projectile in projectiles:
        if 0 < projectile.x < screenWidth:
            projectile.x += projectile.vel
        else:
            item_out_of_range.append(projectile)

        projectiles = [x for x in projectiles if x not in item_out_of_range and x not in item_hit]

    if fighter.bowCount == 8:
        if fighter.last_direction == 1:
            arrow = Projectile(round(fighter.x + widthSprite), round(fighter.y + 20), 20, (randint(100,255), randint(100,255), randint(100,255)), fighter.last_direction)
            #arrow = Projectile(round(fighter.x + widthSprite), round(fighter.y + 20), 20, (255, 255, 255), fighter.last_direction)
            projectiles.append(arrow)
        elif fighter.last_direction == -1:
            arrow = Projectile(round(fighter.x), round(fighter.y + 20), 20, (randint(100,255), randint(100,255), randint(100,255)), fighter.last_direction)
            #arrow = Projectile(round(fighter.x), round(fighter.y + 20), 20, (255, 255, 255), fighter.last_direction)
            projectiles.append(arrow)


# if cheat
    # if fighter.bowCount == 18 or fighter.bowCount == 15 or fighter.bowCount == 12:
    #     if fighter.last_direction == 1:
    #         arrow = Projectile(round(fighter.x + widthSprite), round(fighter.y + 20), 2, (255, 255, 255), fighter.last_direction)
    #         projectiles.append(arrow)
    #     elif fighter.last_direction == -1:
    #         arrow = Projectile(round(fighter.x), round(fighter.y + 20), 2, (255, 255, 255), fighter.last_direction)
    #         projectiles.append(arrow)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        create_dummies()
    else:
        create_counter = 0
    if keys[pygame.K_DELETE]:
        delete_dummy()
    if keys[pygame.K_DELETE] and keys[pygame.K_m]:
        mass_delete()
    if keys[pygame.K_e] and not fighter.isJump:
        fighter.left = False
        fighter.right = False
        fighter.attack = True
        fighter.ranged_attack = False
    if keys[pygame.K_p]:
        pause = True
    elif keys[pygame.K_r] and not fighter.isJump:
        fighter.left = False
        fighter.right = False
        fighter.attack = False
        fighter.ranged_attack = True
    elif keys[pygame.K_LEFT] and fighter.x + fighter.width/2 > fighter.vel and not fighter.attack and not fighter.ranged_attack:
        fighter.x -= fighter.vel
        fighter.left = True
        fighter.right = False
        #fighter.ranged_attack = False
        fighter.last_direction = -1
    elif keys[pygame.K_RIGHT] and fighter.x < screenWidth - fighter.width - fighter.vel and not fighter.attack and not fighter.ranged_attack:
        fighter.x += fighter.vel
        fighter.left = False
        fighter.right = True
        #fighter.ranged_attack = False
        fighter.last_direction = 1
    else:
        fighter.left = False
        fighter.right = False
        #fighter.ranged_attack = False
        fighter.walkCount = 0

    if not fighter.isJump:
        if keys[pygame.K_SPACE]:
            fighter.isJump = True
            fighter.left = False
            fighter.right = False
            fighter.ranged_attack = False
            fighter.attack = False
            fighter.bowCount = 0
            fighter.attackCount = 0
            fighter.walkCount = 0
    else:
        if fighter.jumpCount >= -8:
            fighter.y -= (fighter.jumpCount * abs(fighter.jumpCount)) * 0.5
            fighter.jumpCount -= 1
        else:
            fighter.isJump = False
            fighter.jumpCount = 8

    draw_game_window()

pygame.quit()