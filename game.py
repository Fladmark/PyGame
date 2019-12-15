import pygame

pygame.init()

screenWidth = 768
screenHeight = 368
widthSprite = 37
heightSprite = 50
item_out_of_range = []
backgroundCounter = 0

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

            self.tics_since_attack = 0

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


class Projectile(object):

    def __init__(self, x, y, width, color, direction):
        self.x = x
        self.y = y
        self.width = width
        self.color = color
        self.direction = direction
        self.vel = 30 * direction
        self.out_of_range = []

    def draw(self, window):
        pygame.draw .line(window, self.color, (round(self.x), round(self.y)), (round(self.x + 20*self.direction), round(self.y)))


def draw_game_window():
    global backgroundCounter
    win.blit(background_frames[backgroundCounter // 2], (0, 0))
    if backgroundCounter == 14:
        backgroundCounter = 0
    else:
        backgroundCounter += 1

    fighter.draw(win)
    for projectile in projectiles:
        projectile.draw(win)
    pygame.display.update()


fighter = Player(50, 315, widthSprite, heightSprite)
run = True
projectiles = []
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for projectile in projectiles:
        if 0 < projectile.x < screenWidth:
            projectile.x += projectile.vel
        else:
            item_out_of_range.append(projectile)

        projectiles = [x for x in projectiles if x not in item_out_of_range]


    if fighter.bowCount == 8:
        if fighter.last_direction == 1:
            arrow = Projectile(round(fighter.x + widthSprite), round(fighter.y + 20), 2, (255, 255, 255), fighter.last_direction)
            projectiles.append(arrow)
        elif fighter.last_direction == -1:
            arrow = Projectile(round(fighter.x), round(fighter.y + 20), 2, (255, 255, 255), fighter.last_direction)
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

    #if not fighter.attack:
    if keys[pygame.K_e] and not fighter.isJump:
        fighter.left = False
        fighter.right = False
        fighter.attack = True
    elif keys[pygame.K_r] and not fighter.isJump:
        fighter.left = False
        fighter.right = False
        fighter.ack = False
        fighter.ranged_attack = True
    elif keys[pygame.K_LEFT] and fighter.x > fighter.vel and not fighter.attack and not fighter.ranged_attack:
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