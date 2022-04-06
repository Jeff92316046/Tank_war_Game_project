import pygame
import time
import random
screen_width = 1300
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.bullets = ['bull.png']
        self.direction_x, self.direction_y = 0, -1
        self.bullet = pygame.image.load(self.bullets[0])
        self.bullet = pygame.transform.scale(self.bullet, (10, 10))
        self.rect = self.bullet.get_rect()
        self.rect.left, self.rect.top = 0, 0
        self.speed = 20
        self.being = True
        self.time = 0
        self.push = False

    def move(self, direction_x, direction_y):
        self.direction_x, self.direction_y = direction_x, direction_y

    def draw(self):
        if self.time == 20:
            self.being = False
            self.rect.left, self.rect.top = -50, 0
            self.push = False
        else:
            self.time = self.time + 1

        if self.being:
            self.rect = self.rect.move(
                self.speed*self.direction_x, self.speed*self.direction_y)
            screen.blit(self.bullet, (self.rect.left, self.rect.top))


class my_tank(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10

        self.direction_x, self.direction_y = 0, -1

        self.tanks = ['tank-up.png', 'tank-right.png',
                      'tank-down.png', 'tank-left.png']

        self.tank = pygame.image.load(self.tanks[1]).convert_alpha()
        self.tank = pygame.transform.scale(self.tank, (50, 50))
        self.rect = self.tank.get_rect()

        self.rect.left, self.rect.top = 50, 50

        self.bullet = Bullet()
        self.invincible = True
        self.Heart = heart_counter()
        self.money = money_counter()
        self.speed_counter = speed_counter()
        self.power_counter = power_counter()
        self.Heart.total_heart = 10
        self.Heart.left_heart = 10
        self.money.word_save = 0
        self.speed_counter.word_save = int(self.speed / 10)
        self.speedlv = 1
        self.score = score()

    def update_skin(self):
        if(self.Heart.left_heart <= 3):
            self.tanks = ['broken_tank-up.png', 'broken_tank-right.png',
                          'broken_tank-down.png', 'broken_tank-left.png']
        if(self.Heart.left_heart > 3):
            self.tanks = ['tank-up.png', 'tank-right.png',
                          'tank-down.png', 'tank-left.png']

    def update_heart(self):
        self.Heart.write_screen1()
        self.Heart.draw_screen1()

    def update_score(self):
        self.score.draw_screen1()

    def update_money(self):
        self.money.write()
        self.money.draw()

    def update_speed(self):
        self.speed_counter.write_screen1()
        self.speed_counter.draw_screen1()

    def update_power(self):
        self.power_counter.write_screen1()
        self.power_counter.draw_screen1()

    def move_up(self):
        self.direction_x, self.direction_y = 0, -1
        self.rect = self.rect.move(
            self.speed*self.direction_x, self.speed*self.direction_y)
        self.tank = pygame.image.load(self.tanks[0]).convert_alpha()
        self.tank = pygame.transform.scale(self.tank, (50, 50))
        if self.rect.top < 0:
            self.rect = self.rect.move(
                self.speed*-self.direction_x, self.speed*-self.direction_y)

    def move_down(self):
        self.direction_x, self.direction_y = 0, 1
        self.rect = self.rect.move(
            self.speed*self.direction_x, self.speed*self.direction_y)
        self.tank = pygame.image.load(self.tanks[2]).convert_alpha()
        self.tank = pygame.transform.scale(self.tank, (50, 50))
        if self.rect.bottom > screen_height:
            self.rect = self.rect.move(
                self.speed*-self.direction_x, self.speed*-self.direction_y)

    def move_right(self):
        self.direction_x, self.direction_y = 1, 0
        self.rect = self.rect.move(
            self.speed*self.direction_x, self.speed*self.direction_y)
        self.tank = pygame.image.load(self.tanks[1]).convert_alpha()
        self.tank = pygame.transform.scale(self.tank, (50, 50))
        if self.rect.right > screen_width - 50:
            self.rect = self.rect.move(
                self.speed*-self.direction_x, self.speed*-self.direction_y)

    def move_left(self):
        self.direction_x, self.direction_y = -1, 0
        self.rect = self.rect.move(
            self.speed*self.direction_x, self.speed*self.direction_y)
        self.tank = pygame.image.load(self.tanks[3]).convert_alpha()
        self.tank = pygame.transform.scale(self.tank, (50, 50))
        if self.rect.left < 0:
            self.rect = self.rect.move(
                self.speed*-self.direction_x, self.speed*-self.direction_y)

    def shoot(self):
        if self.bullet.push == False:
            if self.direction_x == 0 and self.direction_y == -1:
                self.bullet.rect.left = self.rect.left + 20
                self.bullet.rect.bottom = self.rect.top + 20
            elif self.direction_x == 0 and self.direction_y == 1:
                self.bullet.rect.left = self.rect.left + 20
                self.bullet.rect.top = self.rect.bottom - 20
            elif self.direction_x == -1 and self.direction_y == 0:
                self.bullet.rect.right = self.rect.left
                self.bullet.rect.top = self.rect.top + 22
            elif self.direction_x == 1 and self.direction_y == 0:
                self.bullet.rect.left = self.rect.right
                self.bullet.rect.top = self.rect.top + 22
            self.bullet.push = True
            self.bullet.being = True
            self.bullet.time = 0
            self.bullet.move(self.direction_x, self.direction_y)

    def draw(self):
        screen.blit(self.tank, (self.rect.left, self.rect.top))
        self.bullet.draw()

    def hit(self, bullet_x, bullet_y):
        if bullet_x >= self.rect.left and bullet_x <= self.rect.right and bullet_y >= self.rect.top and bullet_y <= self.rect.bottom:
            if self.invincible == True:
                self.Heart.left_heart -= 0
            else:
                self.Heart.left_heart -= 1
            return True
        else:
            return False


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('wall.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = x, y

    def hit(self, tank_x, tank_y, keys):
        if tank_x + 50 == self.rect.left and tank_y < self.rect.bottom and tank_y > self.rect.top - 50 and keys[pygame.K_RIGHT]:
            return False
        if tank_x == self.rect.right and tank_y < self.rect.bottom and tank_y > self.rect.top - 50 and keys[pygame.K_LEFT]:
            return False
        if tank_y + 50 == self.rect.top and tank_x > self.rect.left - 50 and tank_x < self.rect.right and keys[pygame.K_DOWN]:
            return False
        if tank_y == self.rect.bottom and tank_x > self.rect.left - 50 and tank_x < self.rect.right and keys[pygame.K_UP]:
            return False
        else:
            return True

    def bullet_hit(self, bullet_x, bullet_y):
        if bullet_x + 10 > self.rect.left and bullet_x < self.rect.right and bullet_y > self.rect.top and bullet_y + 10 < self.rect.bottom:
            return False
        else:
            return True

    def ai_hit(self, ai_x, ai_y, ai_direction_x, ai_direction_y):
        if ai_direction_x == 0 and ai_direction_y == 1:
            if ai_y + 50 == self.rect.top and ai_x > self.rect.left - 50 and ai_x < self.rect.right:
                ai_direction_x, ai_direction_y = -1, 0
        if ai_direction_x == 0 and ai_direction_y == -1:
            if ai_y == self.rect.bottom and ai_x > self.rect.left - 50 and ai_x < self.rect.right:
                ai_direction_x, ai_direction_y = 1, 0
        if ai_direction_x == 1 and ai_direction_y == 0:
            if ai_x + 50 == self.rect.left and ai_y > self.rect.top - 50 and ai_y < self.rect.bottom:
                ai_direction_x, ai_direction_y = 0, 1
        if ai_direction_x == -1 and ai_direction_y == 0:
            if ai_x == self.rect.right and ai_y > self.rect.top - 50 and ai_y < self.rect.bottom:
                ai_direction_x, ai_direction_y = 0, -1
        return ai_direction_x, ai_direction_y


class enemy_tank(pygame.sprite.Sprite):
    def __init__(self, x, y, hp, n):
        pygame.sprite.Sprite.__init__(self)
        self.tank1 = ['enemy_tank-up.png', 'enemy_tank-right.png',
                      'enemy_tank-down.png', 'enemy_tank-left.png']
        self.tank2 = ['tank2-up.png', 'tank2-right.png',
                      'tank2-down.png', 'tank2-left.png']
        self.image = pygame.image.load(self.tank1[1]).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = x, y
        self.bullet = Bullet()
        self.speed = 10
        self.direction_x, self.direction_y = 1, 0
        self.bullet = Bullet()
        self.Atk = False
        self.health = hp
        self.num = n

    def hit(self):
        if self.rect.left < 0:
            self.rect = self.rect.move(
                self.speed*-self.direction_x, self.speed*-self.direction_y)
            self.direction_x, self.direction_y = 0, -1
        if self.rect.right > screen_width - 50:
            self.rect = self.rect.move(
                self.speed*-self.direction_x, self.speed*-self.direction_y)
            self.direction_x, self.direction_y = 0, 1
        if self.rect.bottom > screen_height:
            self.rect = self.rect.move(
                self.speed*-self.direction_x, self.speed*-self.direction_y)
            self.direction_x, self.direction_y = -1, 0
        if self.rect.top < 0:
            self.rect = self.rect.move(
                self.speed*-self.direction_x, self.speed*-self.direction_y)
            self.direction_x, self.direction_y = 1, 0

    def update(self):
        if self.num == 1:
            if self.direction_x == 0 and self.direction_y == 1:
                self.image = pygame.image.load(self.tank1[2]).convert_alpha()
                self.image = pygame.transform.scale(self.image, (50, 50))
            if self.direction_x == 0 and self.direction_y == -1:
                self.image = pygame.image.load(self.tank1[0]).convert_alpha()
                self.image = pygame.transform.scale(self.image, (50, 50))
            if self.direction_x == 1 and self.direction_y == 0:
                self.image = pygame.image.load(self.tank1[1]).convert_alpha()
                self.image = pygame.transform.scale(self.image, (50, 50))
            if self.direction_x == -1 and self.direction_y == 0:
                self.image = pygame.image.load(self.tank1[3]).convert_alpha()
                self.image = pygame.transform.scale(self.image, (50, 50))
        elif self.num == 2:
            if self.direction_x == 0 and self.direction_y == 1:
                self.image = pygame.image.load(self.tank2[2]).convert_alpha()
                self.image = pygame.transform.scale(self.image, (50, 50))
            if self.direction_x == 0 and self.direction_y == -1:
                self.image = pygame.image.load(self.tank2[0]).convert_alpha()
                self.image = pygame.transform.scale(self.image, (50, 50))
            if self.direction_x == 1 and self.direction_y == 0:
                self.image = pygame.image.load(self.tank2[1]).convert_alpha()
                self.image = pygame.transform.scale(self.image, (50, 50))
            if self.direction_x == -1 and self.direction_y == 0:
                self.image = pygame.image.load(self.tank2[3]).convert_alpha()
                self.image = pygame.transform.scale(self.image, (50, 50))
        self.bullet.draw()
        self.rect = self.rect.move(
            self.speed*self.direction_x, self.speed*self.direction_y)

    def killed(self, bullet_x, bullet_y):
        if bullet_x <= self.rect.right and bullet_x >= self.rect.left and bullet_y >= self.rect.top and bullet_y <= self.rect.bottom:
            return True
        else:
            return False

    def atk(self, player_x, player_y):
        if self.rect.top == player_y:
            if player_x < self.rect.left:
                self.direction_x, self.direction_y = -1, 0
            elif player_x > self.rect.right:
                self.direction_x, self.direction_y = 1, 0
            self.Atk = True

        if self.rect.left == player_x:
            if player_y < self.rect.top:
                self.direction_x, self.direction_y = 0, -1
            elif player_y > self.rect.bottom:
                self.direction_x, self.direction_y = 0, 1
            self.Atk = True

        if self.Atk == True:
            self.Atk = False
            if self.bullet.push == False:
                if self.direction_x == 0 and self.direction_y == -1:
                    self.bullet.rect.left = self.rect.left + 20
                    self.bullet.rect.bottom = self.rect.top + 20
                elif self.direction_x == 0 and self.direction_y == 1:
                    self.bullet.rect.left = self.rect.left + 20
                    self.bullet.rect.top = self.rect.bottom - 20
                elif self.direction_x == -1 and self.direction_y == 0:
                    self.bullet.rect.right = self.rect.left
                    self.bullet.rect.top = self.rect.top + 22
                elif self.direction_x == 1 and self.direction_y == 0:
                    self.bullet.rect.left = self.rect.right
                    self.bullet.rect.top = self.rect.top + 22
                self.bullet.push = True
                self.bullet.time = 0
                self.bullet.being = True
                self.bullet.move(self.direction_x, self.direction_y)


class heart_counter(pygame.sprite.Sprite):
    def __init__(self):
        self.total_heart = 0
        self.left_heart = 0
        self.heart_image = pygame.image.load('heart.png')
        self.heart_image = pygame.transform.scale(self.heart_image, (50, 50))
        self.heart_image_2 = pygame.image.load('heart.png')
        self.heart_image_2 = pygame.transform.scale(
            self.heart_image_2, (200, 200))
        self.heart_image_3 = pygame.image.load('heal.jpg')
        self.heart_image_3 = pygame.transform.scale(
            self.heart_image_3, (200, 200))
        self.x = screen_width - 50
        self.y = 0
        self.word = pygame.font.SysFont("arial", 16)
        self.word_2 = pygame.font.SysFont("arial", 30)
        self.word_3 = pygame.font.SysFont("arial", 30)
        self.text_surface = self.word.render(
            "{a}/{b}".format(a=self.left_heart, b=self.total_heart), True, (0, 0, 255))
        self.text_surface_2 = self.word_2.render("        {a}>>>{b}".format(
            a=self.total_heart, b=self.total_heart+5), True, (0, 0, 255))
        self.text_surface_3 = self.word_3.render("        {a}>>>{b}".format(
            a=self.left_heart, b=self.left_heart+10), True, (0, 0, 255))
        self.word_x_1 = self.x
        self.word_y_1 = self.y + 50
        self.x_2 = 800
        self.y_2 = 150
        self.x_3 = 200
        self.y_3 = 400
        self.word_x_2 = self.x_2
        self.word_y_2 = self.y_2 + 200
        self.word_x_3 = self.x_3
        self.word_y_3 = self.y_3 + 200
        self.heart_level = 1

    def draw_screen1(self):
        self.text_surface = self.word.render(
            "{a}/{b}".format(a=self.left_heart, b=self.total_heart), True, (0, 0, 255))
        screen.blit(self.heart_image, (self.x, self.y))

    def write_screen1(self):
        screen.blit(self.text_surface, (self.x, self.y+50))

    def draw_screen4(self):
        screen.blit(self.heart_image_2, (self.x_2, self.y_2))

    def write_screen4(self):
        if self.heart_level < 3:
            self.text_surface_2 = self.word_2.render("        {a}>>>{b}".format(
                a=self.total_heart, b=self.total_heart+5), True, (0, 0, 255))
        elif self.heart_level >= 3:
            self.text_surface_2 = self.word_2.render(
                "          {a}".format(a="Max"), True, (0, 0, 255))
        screen.blit(self.text_surface_2, (self.word_x_2, self.word_y_2))

    def draw_screen4_2(self):
        screen.blit(self.heart_image_3, (self.x_3, self.y_3))

    def write_screen4_2(self):
        if self.left_heart < self.total_heart-5:
            self.text_surface_3 = self.word_3.render("        {a}>>>{b}".format(
                a=self.left_heart, b=self.left_heart+5), True, (0, 0, 255))
        elif self.left_heart >= self.total_heart-5:
            self.text_surface_3 = self.word_3.render("        {a}>>>{b}".format(
                a=self.left_heart, b=self.total_heart), True, (0, 0, 255))
        screen.blit(self.text_surface_3, (self.word_x_3, self.word_y_3))


class money_counter(pygame.sprite.Sprite):
    def __init__(self):
        self.total_heart = 0
        self.left_heart = 0
        self.money_image = pygame.image.load('money.png')
        self.money_image = pygame.transform.scale(self.money_image, (50, 50))
        self.x = screen_width - 50
        self.y = 100
        self.word = pygame.font.SysFont("arial", 16)
        self.word_save = 1
        self.text_surface = self.word.render(
            "{a}".format(a=self.word_save), True, (0, 0, 255))
        self.word_x = self.x
        self.word_y = self.y + 50

    def draw(self):
        self.text_surface = self.word.render(
            "{a}".format(a=self.word_save), True, (0, 0, 255))
        screen.blit(self.money_image, (self.x, self.y))

    def write(self):
        screen.blit(self.text_surface, (self.x, self.y+50))


class speed_counter(pygame.sprite.Sprite):
    def __init__(self):
        self.total_speed = 0
        self.left_speed = 0
        self.speed_image_1 = pygame.image.load('speed_image.png')
        self.speed_image_1 = pygame.transform.scale(
            self.speed_image_1, (50, 50))
        self.speed_image_2 = pygame.image.load('speed_image.png')
        self.speed_image_2 = pygame.transform.scale(
            self.speed_image_2, (200, 200))
        self.x_1 = screen_width - 50
        self.y_1 = 200
        self.word_1 = pygame.font.SysFont("arial", 16)
        self.word_2 = pygame.font.SysFont("arial", 30)
        self.word_save = 1
        self.text_surface_1 = self.word_1.render(
            "{a}".format(a=self.word_save), True, (0, 0, 255))
        self.text_surface_2 = self.word_2.render(
            "{a}".format(a=self.word_save), True, (0, 0, 255))
        self.word_x_1 = self.x_1
        self.word_y_1 = self.y_1 + 50
        self.x_2 = 200
        self.y_2 = 150
        self.word_x_2 = self.x_2
        self.word_y_2 = self.y_2 + 200

    def draw_screen1(self):
        screen.blit(self.speed_image_1, (self.x_1, self.y_1))

    def write_screen1(self):
        self.text_surface_1 = self.word_1.render(
            "{a}".format(a=self.word_save), True, (0, 0, 255))
        screen.blit(self.text_surface_1, (self.word_x_1, self.word_y_1))

    def draw_screen4(self):
        screen.blit(self.speed_image_2, (self.x_2, self.y_2))

    def write_screen4(self):
        if self.word_save < 3:
            self.text_surface_2 = self.word_2.render("        {a}>>>{b}".format(
                a=self.word_save, b=self.word_save+1), True, (0, 0, 255))
        elif self.word_save >= 3:
            self.text_surface_2 = self.word_2.render(
                "          {a}".format(a="Max"), True, (0, 0, 255))
        screen.blit(self.text_surface_2, (self.word_x_2, self.word_y_2))


class power_counter(pygame.sprite.Sprite):
    def __init__(self):
        self.total_power = 0
        self.left_power = 0
        self.power_image_1 = pygame.image.load('power.jpg')
        self.power_image_1 = pygame.transform.scale(
            self.power_image_1, (50, 50))
        self.power_image_2 = pygame.image.load('power.jpg')
        self.power_image_2 = pygame.transform.scale(
            self.power_image_2, (200, 200))
        self.x_1 = screen_width - 50
        self.y_1 = 300
        self.word_1 = pygame.font.SysFont("arial", 16)
        self.word_2 = pygame.font.SysFont("arial", 30)
        self.word_save = 1
        self.text_surface_1 = self.word_1.render(
            "{a}".format(a=self.word_save), True, (0, 0, 255))
        self.text_surface_2 = self.word_2.render(
            "{a}".format(a=self.word_save), True, (0, 0, 255))
        self.word_x_1 = self.x_1
        self.word_y_1 = self.y_1 + 50
        self.x_2 = 500
        self.y_2 = 150
        self.word_x_2 = self.x_2
        self.word_y_2 = self.y_2 + 200

    def draw_screen1(self):
        screen.blit(self.power_image_1, (self.x_1, self.y_1))

    def write_screen1(self):
        self.text_surface_1 = self.word_1.render(
            "{a}".format(a=self.word_save), True, (0, 0, 255))
        screen.blit(self.text_surface_1, (self.word_x_1, self.word_y_1))

    def draw_screen4(self):
        screen.blit(self.power_image_2, (self.x_2, self.y_2))

    def write_screen4(self):
        if self.word_save < 3:
            self.text_surface_2 = self.word_2.render("        {a}>>>{b}".format(
                a=self.word_save, b=self.word_save+1), True, (0, 0, 255))
        elif self.word_save >= 3:
            self.text_surface_2 = self.word_2.render(
                "          {a}".format(a="Max"), True, (0, 0, 255))
        screen.blit(self.text_surface_2, (self.word_x_2, self.word_y_2))


class power_counter(pygame.sprite.Sprite):
    def __init__(self):
        self.total_power = 0
        self.left_power = 0
        self.power_image_1 = pygame.image.load('power.jpg')
        self.power_image_1 = pygame.transform.scale(
            self.power_image_1, (50, 50))
        self.power_image_2 = pygame.image.load('power.jpg')
        self.power_image_2 = pygame.transform.scale(
            self.power_image_2, (200, 200))
        self.x_1 = screen_width - 50
        self.y_1 = 300
        self.word_1 = pygame.font.SysFont("arial", 16)
        self.word_2 = pygame.font.SysFont("arial", 30)
        self.word_save = 1
        self.text_surface_1 = self.word_1.render(
            "{a}".format(a=self.word_save), True, (0, 0, 255))
        self.text_surface_2 = self.word_2.render(
            "{a}".format(a=self.word_save), True, (0, 0, 255))
        self.word_x_1 = self.x_1
        self.word_y_1 = self.y_1 + 50
        self.x_2 = 500
        self.y_2 = 150
        self.word_x_2 = self.x_2
        self.word_y_2 = self.y_2 + 200

    def draw_screen1(self):
        screen.blit(self.power_image_1, (self.x_1, self.y_1))

    def write_screen1(self):
        self.text_surface_1 = self.word_1.render(
            "{a}".format(a=self.word_save), True, (0, 0, 255))
        screen.blit(self.text_surface_1, (self.word_x_1, self.word_y_1))

    def draw_screen4(self):
        screen.blit(self.power_image_2, (self.x_2, self.y_2))

    def write_screen4(self):
        if self.word_save < 3:
            self.text_surface_2 = self.word_2.render("        {a}>>>{b}".format(
                a=self.word_save, b=self.word_save+1), True, (0, 0, 255))
        elif self.word_save >= 3:
            self.text_surface_2 = self.word_2.render(
                "          {a}".format(a="Max"), True, (0, 0, 255))
        screen.blit(self.text_surface_2, (self.word_x_2, self.word_y_2))


class staff_list(pygame.sprite.Sprite):
    def __init__(self):
        self.word_save1 = pygame.image.load('20819.png')
        self.word_save1 = pygame.transform.scale(self.word_save1, (200, 50))
        self.word_save2 = pygame.image.load('20930.png')
        self.word_save2 = pygame.transform.scale(self.word_save2, (200, 50))
        self.word_save3 = pygame.image.load('20931.png')
        self.word_save3 = pygame.transform.scale(self.word_save3, (200, 50))
        self.word_save4 = pygame.image.load('image_design.png')
        self.word_save4 = pygame.transform.scale(self.word_save4, (200, 50))
        self.word_save5 = pygame.image.load('program_design.png')
        self.word_save5 = pygame.transform.scale(self.word_save5, (200, 50))
        self.word_save6 = pygame.image.load('scene_design.png')
        self.word_save6 = pygame.transform.scale(self.word_save6, (200, 50))
        self.word_x1 = 300
        self.word_y1 = 100
        self.word_x2 = 550
        self.word_y2 = 100
        self.word_x3 = 800
        self.word_y3 = 100
        self.word_x4 = 100
        self.word_y4 = 100
        self.word_x5 = 100
        self.word_y5 = 200
        self.word_x6 = 100
        self.word_y6 = 300
        self.back = pygame.image.load('back.png')
        self.back = pygame.transform.scale(self.back, (120, 150))
        '''
        self.tanks = ['tank-up.png','tank-right.png','tank-down.png','tank-left.png']
        self.tank1 =  pygame.image.load(self.tanks[0])
        self.tank1 =  pygame.transform.scale(self.tank1,(50,50)) 
        self.tank2 =  pygame.image.load(self.tanks[1])
        self.tank2 =  pygame.transform.scale(self.tank2,(50,50)) 
        self.tank3 =  pygame.image.load(self.tanks[2])
        self.tank3 =  pygame.transform.scale(self.tank3,(50,50)) 
        self.tank4 =  pygame.image.load(self.tanks[3])
        self.tank4 =  pygame.transform.scale(self.tank4,(50,50)) 
        '''

    def write(self):
        screen.blit(self.word_save1, (self.word_x1, self.word_y1))
        screen.blit(self.word_save2, (self.word_x2, self.word_y2))
        screen.blit(self.word_save3, (self.word_x3, self.word_y3))
        screen.blit(self.word_save4, (self.word_x4, self.word_y4))
        screen.blit(self.word_save5, (self.word_x5, self.word_y5))
        screen.blit(self.word_save6, (self.word_x6, self.word_y6))
        screen.blit(self.word_save1, (self.word_x1, self.word_y1+100))
        screen.blit(self.word_save2, (self.word_x2, self.word_y2+100))
        screen.blit(self.word_save3, (self.word_x3, self.word_y3+100))
        screen.blit(self.word_save3, (self.word_x1, self.word_y1+200))
        screen.blit(self.back, (1000, 600))


class shop(pygame.sprite.Sprite):
    def __init__(self):
        self.back = pygame.image.load('back.png')
        self.back = pygame.transform.scale(self.back, (120, 150))
        self.scene = pygame.image.load('shop_scene.png')
        self.scene = pygame.transform.scale(self.scene, (1300, 800))
        self.shop_image = pygame.image.load('shop.png')
        self.shop_image = pygame.transform.scale(self.shop_image, (50, 50))

    def draw_screen4(self):
        screen.blit(self.scene, (0, 0))
        screen.blit(self.back, (1155, 620))

    def draw_screen1(self):
        screen.blit(self.shop_image, (1250, 750))


class between_scene(pygame.sprite.Sprite):
    def __init__(self):
        self.load_1 = pygame.image.load('LOADING_1.png')
        self.load_1 = pygame.transform.scale(self.load_1, (1300, 800))
        self.load_2 = pygame.image.load('LOADING_2.png')
        self.load_2 = pygame.transform.scale(self.load_2, (1300, 800))
        self.load_3 = pygame.image.load('LOADING_3.png')
        self.load_3 = pygame.transform.scale(self.load_3, (1300, 800))

    def drew1(self):
        screen.blit(self.load_1, (0, 0))
        pygame.display.update()

    def drew2(self):
        screen.blit(self.load_2, (0, 0))
        pygame.display.update()

    def drew3(self):
        screen.blit(self.load_3, (0, 0))
        pygame.display.update()


class music(pygame.sprite.Sprite):
    def __init__(self):
        pygame.mixer.music.set_volume(0.2)

    def click(self):
        pygame.mixer.music.load("click.mp3")
        pygame.mixer.music.play()

    def bomb(self):
        pygame.mixer.music.load("bomb.mp3")
        pygame.mixer.music.play()

    def fireworks(self):
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.load("fireworks.mp3")
        pygame.mixer.music.play(0)
        pygame.mixer.music.fadeout(10000)

    def game_over(self):
        pygame.mixer.music.load("game_over.mp3")
        pygame.mixer.music.play(0)
        pygame.mixer.music.fadeout(10000)

    def powerup(self):
        pygame.mixer.music.load("powerup.mp3")
        pygame.mixer.music.play()

    def shoot(self):
        pygame.mixer.music.load("shoot.mp3")
        pygame.mixer.music.play()

    def end(self):
        pygame.time.delay(10000)
        sys.exit()


class score(pygame.sprite.Sprite):
    def __init__(self):
        self.Score = 0
        self.x_1 = 600
        self.y_1 = screen_height - 50
        self.x_2 = 540
        self.y_2 = screen_height - 15
        self.word_1 = pygame.font.SysFont("arial", 30)
        self.word_save = "Score"
        self.text_surface = self.word_1.render(
            "{a}".format(a=self.word_save), True, (0, 0, 0))

    def draw_screen1(self):
        self.text_surface = self.word_1.render("{a} : {b}".format(
            a=self.word_save, b=self.Score), True, (0, 0, 255))
        screen.blit(self.text_surface, (self.x_1, self.y_1))

    def draw_screen6(self):
        self.word_1 = pygame.font.SysFont("arial", 50)
        self.text_surface = self.word_1.render("{a} : {b}".format(
            a=self.word_save, b=self.Score), True, (0, 0, 255))
        screen.blit(self.text_surface, (self.x_2, self.y_2 - 50))
