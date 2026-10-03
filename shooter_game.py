#Create your own shooter
from random import randint
from pygame import *
from time import time as timer
num_fire = 7
rel_time = False
missed = 0
Score = 0
f_s = 20
f_m = 5
mixer.init()
kick = mixer.Sound('fire.ogg')
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(w,h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.player_image = player_image
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        # if keys_pressed[K_UP] and self.rect.y > 0:
        #     self.rect.y -= self.speed
        # if keys_pressed[K_DOWN] and self.rect.y < 395:
        #     self.rect.y += self.speed
        if keys_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 795:
            self.rect.x += self.speed
    def fire (self):
        bullet = bullets('Laser-Beam-PNG-Photos.png', self.rect.centerx - 5, self.rect.top, 5, 10, 45)
        bull.add(bullet)

        
class enemy2(GameSprite):
    def update(self):
        global missed
        self.rect.y += self.speed
        if self.rect.y >= window_h:
            if "d822390713090ba1a6e94b9e35f4381f-removebg-preview.png" in self.player_image:
                missed +=1
            self.rect.y = 0
            self.rect.x = randint(0,800)
class bullets(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        # if self.rect.y <= 0 or colide_rect(self, e1) or colide_rect(self, e2) or colide_rect(self, e3) or colide_rect(self, e4) :
        if self.rect.y <= 0:
            self.kill()

    

window_h = 600
window_w = 900
display.set_caption('Shooter game')
clock = time.Clock()
window = display.set_mode((window_w, window_h))
background = transform.scale(image.load("galaxy.jpg"),(window_w, window_h))
sp1 = player('openclipart-vectors-space-ship-149089_640.png', 0, 500, 9, 85, 85)
# sp2 = player('rocket.png', 800, 400, 9, 100, 100)
e1 = enemy2('d822390713090ba1a6e94b9e35f4381f-removebg-preview.png', 0, 0, randint(1, 3), 65, 65)
e2 = enemy2('d822390713090ba1a6e94b9e35f4381f-removebg-preview.png', randint(0, window_w - 100), 0, randint(1, 3), 65, 65)
e3 = enemy2('d822390713090ba1a6e94b9e35f4381f-removebg-preview.png', randint(0, window_w - 100), 0, randint(1, 3), 65, 65)
e4 = enemy2('d822390713090ba1a6e94b9e35f4381f-removebg-preview.png', randint(0, window_w - 100), 0, randint(1, 3), 65, 65)
e5 = enemy2('d822390713090ba1a6e94b9e35f4381f-removebg-preview.png', randint(0, window_w - 100), 0, randint(1, 3), 65, 65)
e6 = enemy2('d822390713090ba1a6e94b9e35f4381f-removebg-preview.png', randint(0, window_w - 100), 0, randint(1, 3), 65, 65)
a1 = enemy2('asteroid.png', randint(0, window_w - 100), 0, randint(2, 5), 65, 65)
a2 = enemy2('asteroid.png', randint(0, window_w - 100), 0, randint(2, 5), 65, 65)
a3 = enemy2('asteroid.png', randint(0, window_w - 100), 0, randint(2, 5), 65, 65)
monesters = sprite.Group()
monesters.add(e1)
monesters.add(e2)
monesters.add(e3)
monesters.add(e4)
monesters.add(e5)
monesters.add(e6)
a = sprite.Group()
a.add(a1)
a.add(a2)
a.add(a3)
bull = sprite.Group()
mixer.music.load("space.ogg")
mixer.music.play()
kick = mixer.Sound("fire.ogg")
font.init()
font1 = font.SysFont("Arial", 70)
font2 = font.SysFont("Arial", 36)
win = font1.render("YOU WON!", False, (0, 255, 0))
lose = font1.render("YOU LOST!", False, (255, 0, 0))
miss = font2.render("Missed:" + str(missed), True, (255, 255, 255))
score = font2.render("score:" + str(Score), True, (255, 255, 255))
finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if finish !=True:
            if e.type == KEYDOWN:
                if e.key == K_SPACE:
                    if num_fire > 0 and rel_time == False:
                        sp1.fire()
                        kick.play() 
                        num_fire -= 1
                    if num_fire <= 0 and rel_time == False:
                        rel_time = True
                        last_time = timer()
    if finish != True:

        window.blit(background, (0,0))
        if rel_time ==  True:
            now_time = timer()
            if now_time - last_time < 2.5:
                reloading_txt = font2.render("wait, Reloading.....", 1, (255, 0, 0))
                window.blit(reloading_txt, (260, 460))
            else:
                num_fire = 7
                rel_time = False

        collied_list = sprite.groupcollide(monesters, bull, True , True)
        if len(collied_list) > 0:
            for m in collied_list:
                Score+=1
                e = enemy2('d822390713090ba1a6e94b9e35f4381f-removebg-preview.png', randint(0, window_w - 100), 0, randint(1, 3), 65, 65)
                monesters.add(e)
                print (Score)
        if Score >= f_s:
            finish = True
            window.blit(win, (230, 230))
        if missed >= f_m or sprite.spritecollide(sp1, monesters,False) or sprite.spritecollide(sp1, a,False):
            finish = True
            window.blit(lose, (230,230))

        score = font2.render("score:" + str(Score), True, (255, 255, 255))
        miss = font2.render("Missed:" + str(missed), True, (255, 255, 255))
        window.blit(score, (10,10))
        window.blit(miss, (10,40))
        monesters.draw(window)
        bull.draw(window)
        a.draw(window)
        sp1.reset()
        sp1.update()
        #if bullet.rect.y >=450:
            #bullet.rect.x = sp1.rect.x
        # sp2.reset()
        # sp2.update()
        #if colide_rect(bullets, monesters)
            #Score +=1
        bull.update()
        monesters.update()
        a.update()
    display.update()
    clock.tick(500)

