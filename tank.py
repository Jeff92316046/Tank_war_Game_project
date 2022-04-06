import pygame,time
import pygame.mixer as player
from drew import my_tank, Bullet, screen, Wall, enemy_tank ,staff_list,shop,between_scene,music

pygame.init() 
pygame.mixer.init()                                                                      
pygame.display.set_caption('tank_war')                                             

music = music()
mymusic = pygame.mixer.Sound("backgroundmusic.wav")
mymusic.set_volume(0.2)
mymusic.play(-1)
pygame.time.delay(1000)
running = True
play1 = my_tank()
allsprites = pygame.sprite.Group()
allsprites.add(play1)
wallsgroup = pygame.sprite.Group()
AIsgroup = pygame.sprite.Group()
shop = shop()
between_scene = between_scene()
move = True
kill = False
screen_code = 2
Stage = 2
ai_counter = 0
owo = True
ooo = True
def stage_change(a):
    global ai_counter
    stage = a
    if stage == 1:
        for x in [0,2, 4, 6, 8 , 10, 12, 14, 16, 18, 20, 22, 24]:
            for y in [0,2,4,6,8,10,12,14,16]:
                wallsgroup.add(Wall(x*50, y*50))
        for x in [50,300]:
            for y in [250, 550]:
                AIsgroup.add(enemy_tank(x, y,5,1))
                ai_counter += 1

    if stage == 2:
        for x in [0,1,2,3,4,5,6,7,8,9,10,14,15,16,17,18,19,20,21,22,23,24]:
            for y in [4,8,12]:
                wallsgroup.add(Wall(x*50,y*50))
        for x in range(1):
            AIsgroup.add(enemy_tank(50,50,5,1))
            ai_counter += 1

    if stage == 3:
        for y in [0,14]:
            for x in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [1]:
            for x in [0,9,10,11,12,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [2]:
            for x in [0,9,10,11,12,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [3]:
            for x in [0,3,4,5,15,18,19,20,21,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [4]:
            for x in [0,15,18,19,20,21,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [5]:
            for x in [0,7,8,9,12,15,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [6]: 
            for x in [0,2,3,12,15,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [7]:
            for x in [0,12,15,16,17,18,19,20,21,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [8]:
            for x in [0,7,8,9,10,11,12,21,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [9]:
            for x in [0,3,21,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [10]:
            for x in [0,3,15,16,17,18,21,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [11]:
            for x in [0,3,6,9,10,11,12,13,14,15,16,17,18,21,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [12,13]:
            for x in [0,6,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for z in range(1):
                AIsgroup.add(enemy_tank(500,300,5,1))
                AIsgroup.add(enemy_tank(350,500,5,1))
                ai_counter += 2

    if stage == 4:
        for y in [0,14]:
            for x in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [1]:
            for x in [0,3,4,5,8,9,10,16,17,18,21,22,23,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [2]:  
            for x in [0,3,4,5,21,22,23,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [3]:
            for x in [0,13,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [4]:
            for x in [0,6,8,9,10,13,16,17,18,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [5]:
            for x in [0,1,2,8,9,10,13,16,17,18,21,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [6]:
            for x in [0,1,2,8,17,18,21,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [7]:
            for x in [0,3,6,7,8,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [8]:
            for x in [0,3,11,12,13,14,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [9]:
            for x in [0,3,13,14,17,18,21,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [10]:
            for x in [0,6,7,8,13,14,15,16,17,18,21,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [11]:
            for x in [0,6,7,8,9,0,21,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [12]:
            for x in [0,3,10,21,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [13]:
            for x in [0,3,10,11,12,13,14,15,16,17,18,21,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for z in range(1):
            AIsgroup.add(enemy_tank(400,600,5,1))
            AIsgroup.add(enemy_tank(800,500,5,1))
            ai_counter += 2
    if stage == 5:
        for y in [0,14]:
            for x in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [1]:
            for x in [0,15,16,17,18,19,20,21,22,23,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [2]:
            for x in [0,15,16,17,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [3]:
            for x in [0,3,4,5,8,9,12,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [4]:
            for x in [0,3,8,9,20,21,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [5]:
            for x in [0,3,8,9,15,16,17,20,21,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [6]:
            for x in [0,6,7,8,9,12,13,14,15,20,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [7]:
            for x in [0,6,15,20,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [8]:
            for x in [0,3,4,5,6,15,16,17,18,19,20,23,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [9]:
            for x in [0,9,12,23,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [10]:
            for x in [0,9,12,23,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [11]:
            for x in [0,6,7,8,9,10,21,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [12]:
            for x in [0,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [13]:
            for x in [0,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [15]:
            for x in [0,1,2,3,4,5,6,7,8,9,10,15,16,17,18,19,20,21,22,23,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for z in range(1):
            AIsgroup.add(enemy_tank(400,600,5,1))
            AIsgroup.add(enemy_tank(300,800,5,1))
            AIsgroup.add(enemy_tank(650,650,5,1))
            ai_counter += 1
    if stage == 6:
        for y in [0,14]:
            for x in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [1]:
            for x in [0,3,4,5,8,11,14,18,19,20,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [2]:
            for x in [0,4,5,8,11,14,15,19,22,23,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [3]:
            for x in [0,1,5,11,15,16,21,22,23,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [4]:
            for x in [0,1,2,11,12,16,17,18,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [5]:
            for x in [0,1,2,3,8,12,13,18,23,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [6]:
            for x in [0,7,8,9,13,14,15,18,21,22,23,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [7]:
            for x in [0,6,7,8,9,10,18,21,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [8]:
            for x in [0,3,4,5,6,10,11,18,21,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [9]:
            for x in [0,11,12,13,14,15,18,21,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [10]:
            for x in [0,8,12,13,18,21,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [11]:
            for x in [0,3,4,5,6,7,8,9,12,18,21,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [12]:
            for x in [0,15,16,17,18,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for y in [13]:
            for x in [0,24]:
                wallsgroup.add(Wall(x*50,y*50))
        for z in range(1):
            AIsgroup.add(enemy_tank(1100,600,30,2))
            AIsgroup.add(enemy_tank(400,450,5,1))
            AIsgroup.add(enemy_tank(500,300,5,1))
            ai_counter += 3
    if stage == -1:
        screen.fill((255,255,255))    
        between_scene.drew1()
        time.sleep(0.5)
        between_scene.drew2()
        time.sleep(0.5)
        between_scene.drew3()
        time.sleep(0.5)
            
screen_2_data_1 = pygame.image.load('tank-up.png').convert_alpha()
screen_2_data_1 = pygame.transform.scale(screen_2_data_1,(500,500))
screen_2_data_2 = pygame.image.load('start.png').convert_alpha()
screen_2_data_2 = pygame.transform.scale(screen_2_data_2,(210,70))
screen_2_data_3 = pygame.image.load('staff.png').convert_alpha()
screen_2_data_3 = pygame.transform.scale(screen_2_data_3,(210,70))
screen_2_data_4 = pygame.image.load('tank_war.png').convert_alpha()
screen_2_data_4 = pygame.transform.scale(screen_2_data_4,(500,200))
screen_1_data_1 = pygame.image.load('shop.png').convert_alpha()
screen_1_data_1 = pygame.transform.scale(screen_1_data_1,(50,50))
screen_4_data_1 = pygame.image.load('ban.png').convert_alpha()
screen_4_data_1 = pygame.transform.scale(screen_4_data_1,(200,200))
screen_5_data_1 = pygame.image.load('lose_image.png').convert_alpha()
screen_5_data_1 = pygame.transform.scale(screen_5_data_1,(800,600))
screen_5_data_2 = pygame.image.load('Game Over.png').convert_alpha()
screen_5_data_2 = pygame.transform.scale(screen_5_data_2,(400,100))
screen_5_data_3 = pygame.image.load('back.png')
screen_5_data_3 = pygame.transform.scale(screen_5_data_3,(120,150))
screen_6_data_1 = pygame.image.load('victory.jpg').convert_alpha()
screen_6_data_1 = pygame.transform.scale(screen_6_data_1,(1300,800))
while running:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    
    

    if (screen_code == 2):
        screen.fill((255,255,255))
        screen.blit(screen_2_data_1,(150,150))
        screen.blit(screen_2_data_2,(800,350))
        screen.blit(screen_2_data_3,(800,550))
        screen.blit(screen_2_data_4,(700,100))
        mouse = pygame.mouse.get_pressed()
        
        for index in range(len(mouse)):
            if  mouse[index]:
                if index == 0:
                    mouse_xy = pygame.mouse.get_pos()
                    if  800 < mouse_xy[0] <1010 and 350 < mouse_xy[1] < 420:
                        music.click()
                        screen_code = 1
                        stage_change(Stage)
                    if  800 < mouse_xy[0] <1010 and 550 < mouse_xy[1] < 620:
                        music.click()
                        screen.fill((255,255,255))
                        screen_code = 3
                        

        pygame.display.update()
    elif(screen_code == 1):
        
        

        for each in wallsgroup:
            move = each.hit(play1.rect.left, play1.rect.top, keys)
            if move == False:
                break
            
        for each in wallsgroup:
            play1.bullet.being = each.bullet_hit(play1.bullet.rect.left, play1.bullet.rect.top)
            if play1.bullet.being == False:
                break  
    
        for each in AIsgroup:
            each.hit()
            each.atk(play1.rect.left,play1.rect.top)

        for each in wallsgroup:
            for each2 in AIsgroup:
                owo = False
                each2.bullet.being = each.bullet_hit(each2.bullet.rect.left, each2.bullet.rect.top)
                if each2.bullet.being == False:
                    owo = True
                    break
            if owo:
                break
        for each in AIsgroup:
            if play1.hit(each2.bullet.rect.left, each2.bullet.rect.top):
                
                each.bullet.being = False
                each.bullet.rect.left, each.bullet.rect.top = -50 , -50  
            if keys[pygame.K_9]:
                play1.invincible = True
            else :
                play1.invincible = False
        for each in AIsgroup:
            kill = each.killed(play1.bullet.rect.left, play1.bullet.rect.top)

            if kill :
                music.bomb()
                play1.bullet.rect.top , play1.bullet.rect.left = -50 , -50
                each.health -= play1.power_counter.word_save
                if each.health <= 0:
                    play1.money.word_save += 50
                    AIsgroup.remove(each)
                    play1.score.Score += 100
                    kill = False
                    ai_counter -= 1

        for each in AIsgroup:
            for each2 in wallsgroup:
                each.direction_x, each.direction_y = each2.ai_hit(each.rect.left, each.rect.top, each.direction_x, each.direction_y)   
                
        if move:
            if keys[pygame.K_DOWN]:
                play1.move_down()
            elif keys[pygame.K_UP]:
                play1.move_up()
            elif keys[pygame.K_LEFT]:
                play1.move_left()
            elif keys[pygame.K_RIGHT]:
                play1.move_right()
            elif keys[pygame.K_0]:
                for each in AIsgroup:
                    AIsgroup.remove(each)
                ai_counter = 0
        if keys[pygame.K_SPACE]:
            music.shoot()
            play1.shoot()
        if keys[pygame.K_s]:
            screen_code = 4
        if keys[pygame.K_8]:
            play1.money.word_save +=1000

        screen.fill((255,255,255))
        AIsgroup.update()
        wallsgroup.draw(screen)
        AIsgroup.draw(screen)
        play1.draw()
        play1.update_skin()
        play1.update_heart()
        play1.update_money()
        play1.update_speed()
        play1.update_power()
        play1.update_score()
        shop.draw_screen1()
        
        pygame.display.update()
        mouse = pygame.mouse.get_pressed()

        if ai_counter == 0:
            for each in wallsgroup:
                wallsgroup.remove(each)
            Stage += 1
            if Stage >= 7:
                
                mymusic.stop()
                mymusic = pygame.mixer.Sound("fireworks.wav")
                mymusic.set_volume(0.2)
                mymusic.play()
                #Stage = 1
                screen_code = 6
            else :
                stage_change(-1)
                stage_change(Stage)
            play1.rect.left, play1.rect.top = 50, 50

        for index in range(len(mouse)):
            if  mouse[index]:
                if index == 0:
                    mouse_xy = pygame.mouse.get_pos()
                    if  1250 < mouse_xy[0] <1300 and 750 < mouse_xy[1] < 800:
                        music.click()
                        screen_code = 4
        if play1.Heart.left_heart<= 0:
            mymusic.stop()
            mymusic = pygame.mixer.Sound("game_over.wav")
            mymusic.set_volume(0.2)
            mymusic.play()
            screen_code = 5
            
    elif screen_code == 3:
        staff = staff_list()
        staff.write()
        mouse = pygame.mouse.get_pressed()
        for index in range(len(mouse)):
            if  mouse[index]:
                if index == 0:
                    mouse_xy = pygame.mouse.get_pos()
                    if  1000 < mouse_xy[0] <1120 and 600 < mouse_xy[1] < 750:
                        music.click()
                        screen.fill((255,255,255))
                        screen_code = 2
        pygame.display.update()   
        
    elif screen_code == 4:
        screen.fill((255,255,255))
        shop.draw_screen4()
        play1.speed_counter.draw_screen4()
        play1.speed_counter.write_screen4()   
        play1.power_counter.draw_screen4()
        play1.power_counter.write_screen4()
        play1.Heart.write_screen4_2()
        play1.Heart.draw_screen4_2()
        play1.Heart.draw_screen4()
        play1.Heart.write_screen4()
        if keys[pygame.K_b]:
            screen_code = 1
        mouse = pygame.mouse.get_pressed()
        for index in range(len(mouse)):
            if  mouse[index]:
                if index == 0:
                    mouse_xy = pygame.mouse.get_pos()
                    if  1155 < mouse_xy[0] < 1275 and 620 < mouse_xy[1] < 770:
                        screen.fill((255,255,255))
                        screen_code = 1  
                    
                    if  play1.speed_counter.x_2 < mouse_xy[0] < play1.speed_counter.x_2 + 200 \
                    and play1.speed_counter.y_2 < mouse_xy[1] < play1.speed_counter.y_2 + 200 \
                    and play1.money.word_save >= play1.speed_counter.word_save*10 \
                    and play1.speed_counter.word_save < 3 : 
                        play1.money.word_save -= play1.speed_counter.word_save*10
                        play1.speed_counter.word_save += 1 
                        screen.fill((255,255,255))
                        screen_code = 1
                        play1.speedlv += 1
                    elif play1.speed_counter.x_2 < mouse_xy[0] < play1.speed_counter.x_2 + 200 \
                    and play1.speed_counter.y_2 < mouse_xy[1] < play1.speed_counter.y_2 + 200 \
                    and not(play1.money.word_save >= play1.speed_counter.word_save*10)\
                    or \
                        play1.speed_counter.x_2 < mouse_xy[0] < play1.speed_counter.x_2 + 200 \
                    and play1.speed_counter.y_2 < mouse_xy[1] < play1.speed_counter.y_2 + 200 \
                    and not(play1.speed_counter.word_save < 3 ):
                        screen.blit(screen_4_data_1,(play1.speed_counter.x_2,play1.speed_counter.y_2))



                    
                    if  \
                        play1.power_counter.x_2 < mouse_xy[0] < play1.power_counter.x_2 + 200 \
                    and play1.power_counter.y_2 < mouse_xy[1] < play1.power_counter.y_2 + 200 \
                    and play1.money.word_save >= play1.power_counter.word_save*10 \
                    and play1.power_counter.word_save < 3 : 
                        play1.money.word_save -= play1.power_counter.word_save*10
                        play1.power_counter.word_save += 1 
                        screen.fill((255,255,255))
                        screen_code = 1
                    elif  \
                        play1.power_counter.x_2 < mouse_xy[0] < play1.power_counter.x_2 + 200 \
                    and play1.power_counter.y_2 < mouse_xy[1] < play1.power_counter.y_2 + 200 \
                    and not(play1.money.word_save >= play1.power_counter.word_save*10)\
                    or \
                        play1.power_counter.x_2 < mouse_xy[0] < play1.power_counter.x_2 + 200 \
                    and play1.power_counter.y_2 < mouse_xy[1] < play1.power_counter.y_2 + 200 \
                    and not(play1.power_counter.word_save < 3 ):
                        screen.blit(screen_4_data_1,(play1.power_counter.x_2,play1.power_counter.y_2))


                    
                    if  \
                        play1.Heart.x_2 < mouse_xy[0] < play1.Heart.x_2 + 200 \
                    and play1.Heart.y_2 < mouse_xy[1] < play1.Heart.y_2 + 200 \
                    and play1.money.word_save >= 50 \
                    and play1.Heart.heart_level < 3 : 
                        play1.money.word_save -= 50
                        play1.Heart.total_heart += 5
                        play1.Heart.left_heart +=5
                        play1.Heart.heart_level +=1
                        screen.fill((255,255,255))
                        screen_code = 1
                    elif  \
                        play1.Heart.x_2 < mouse_xy[0] < play1.Heart.x_2 + 200 \
                    and play1.Heart.y_2 < mouse_xy[1] < play1.Heart.y_2 + 200 \
                    and not(play1.money.word_save >= 50)\
                    or \
                        play1.Heart.x_2 < mouse_xy[0] < play1.Heart.x_2 + 200 \
                    and play1.Heart.y_2 < mouse_xy[1] < play1.Heart.y_2 + 200 \
                    and not(play1.Heart.total_heart < 3 ):
                        screen.blit(screen_4_data_1,(play1.Heart.x_2,play1.Heart.y_2))
                    
                    if  \
                        play1.Heart.x_3 < mouse_xy[0] < play1.Heart.x_3 + 200 \
                    and play1.Heart.y_3 < mouse_xy[1] < play1.Heart.y_3 + 200 \
                    and play1.money.word_save >= 10  \
                    and not(play1.Heart.total_heart == play1.Heart.left_heart) : 
                        play1.money.word_save -= 10
                        if play1.Heart.left_heart < play1.Heart.total_heart -5 : 
                            play1.Heart.left_heart +=5
                        else :
                            play1.Heart.left_heart = play1.Heart.total_heart
                        screen.fill((255,255,255))
                        screen_code = 1
                    elif  \
                        play1.Heart.x_3 < mouse_xy[0] < play1.Heart.x_3 + 200 \
                    and play1.Heart.y_3 < mouse_xy[1] < play1.Heart.y_3 + 200 \
                    and not(play1.money.word_save >= 10)\
                    or \
                        play1.Heart.x_3 < mouse_xy[0] < play1.Heart.x_3 + 200 \
                    and play1.Heart.y_3 < mouse_xy[1] < play1.Heart.y_3 + 200 \
                    and play1.Heart.total_heart == play1.Heart.left_heart :
                        screen.blit(screen_4_data_1,(play1.Heart.x_3,play1.Heart.y_3))
        pygame.display.update() 
    elif screen_code == 5:
        screen.fill((255,255,255))
        screen.blit(screen_5_data_2,(450,50))
        screen.blit(screen_5_data_1,(250,150))
        screen.blit(screen_5_data_3,(1300-120,800-150))
        mouse = pygame.mouse.get_pressed()
        for index in range(len(mouse)):
            if  mouse[index]:
                if index == 0:
                    mouse_xy = pygame.mouse.get_pos()
                    if  1180 < mouse_xy[0] <1300 and  650 < mouse_xy[1] < 800:
                        #music.click()
                        #music.end()
                        screen.fill((255,255,255))
                        mymusic.stop()
                        mymusic = pygame.mixer.Sound("backgroundmusic.wav")
                        mymusic.set_volume(0.2)
                        mymusic.play(-1)
                        screen_code = 2
        play1.money.word_save = 0
        play1.rect.left = 50
        play1.rect.top = 50
        play1.speed_counter.word_save = 1
        play1.speed = 10
        play1.score.Score = 0
        play1.power_counter.word_save = 1
        play1.Heart.total_heart = 10
        play1.Heart.left_heart = 10
        for each in AIsgroup:
            AIsgroup.remove(each)
        pygame.display.update()
        #music.end()
    elif screen_code == 6:
        if ooo  :
            play1.score.Score += play1.Heart.left_heart * 100
            ooo = False
        screen.fill((255,255,255))
        #screen.blit(screen_5_data_2,(450,50))
        screen.blit(screen_6_data_1,(0,0))
        play1.score.draw_screen6()
        pygame.display.update()

        #screen.blit(screen_5_data_3,(1300-120,800-150))
        '''
        mouse = pygame.mouse.get_pressed()
        for index in range(len(mouse)):
            if  mouse[index]:
                if index == 0:
                    mouse_xy = pygame.mouse.get_pos()
                    if  1180 < mouse_xy[0] <1300 and  650 < mouse_xy[1] < 800:
                        music.click()
                        screen.fill((255,255,255))
                        screen_code = 2
        play1.Heart.word_save = 10
        play1.money.word_save = 0
        play1.rect.left = 50
        play1.rect.top = 50
        play1.speed_counter.word_save = 1
        play1.speed = 10
        play1.power_counter.word_save = 1
        for each in AIsgroup:
            AIsgroup.remove(each)
        '''
    
pygame.quit()