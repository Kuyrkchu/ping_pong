from pygame import *
from random import randint
init()
font.init()

game = True 
finish = False
win_w, win_h = (800, 600)
score1, score2 = 0,0
FPS = 60



window = display.set_mode((win_w, win_h))
font0 = font.SysFont('Arial', 50)
clock = time.Clock()
display.set_caption("этa DevePoPa_думать что он умна(-__-).jopag")

class GameSprite(sprite.Sprite):
    def __init__(self,image_file, x, y, speedx, speedy, w, h):
        self.image = transform.scale(image.load(image_file), (w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = speedx
        self.speedy = speedy

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w]:
            self.rect.y -= self.speedy
        if keys[K_s]:
            self.rect.y += self.speedy

class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >= 0 and self.rect.y <= 600:
            self.rect.y -= self.speedy
        if keys[K_DOWN] and self.rect.y >= 0 and self.rect.y <= 600:
            self.rect.y += self.speedy

class Ball(GameSprite):
    def update(self):
        global score1, score2, win_h, win_w
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if (self.rect.y <= 0):
            self.speedy = randint(5, abs(self.speedy)+5)
        if (self.rect.y >= win_h):
            self.speedy = -randint(5, abs(self.speedy)+5)

        if sprite.collide_rect(self,player1):
            self.speedx =  randint(5,abs(self.speedx)+5)
        if sprite.collide_rect(self,player2):
            self.speedx = -randint(5,abs(self.speedx)+5)
        if self.rect.x <= 0:
            score2 += 1
            self.speedx =  randint(5,abs(self.speedx)+5)     
        if self.rect.x >= win_w:
            score1 += 1
            self.speedx = -randint(5,abs(self.speedx)+5)
    

player1 = Player1("palka.png",win_w//10, win_h//2,   0, 10, 50, 200)
player2 = Player2("palka.png",win_w//1.2, win_h//2, 0, 10, 50, 200)
ball = Ball("EGG.png",win_w//2, win_h//2, 13, 16, 75, 100 )

        

                

while game:
    #обновление экрана
    display.update()
    #задержка
    clock.tick(FPS)
    #обработка события
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN and e.key == K_r:
            ball = Ball("EGG.png",win_w//2, win_h//2, 13, 16, 75, 100 )
            player1 = Player1("palka.png",win_w//10, win_h//2,   0, 10, 50, 200)
            player2 = Player2("palka.png",win_w//1.2, win_h//2, 0, 10, 50, 200)
            

    #игровая логика
    player1.update()
    player2.update()
    ball.update()

    image_score1 = font0.render('Игрок1:' +str(score1), True, (50,50,50))
    image_score2 = font0.render('Игрок2:' +str(score2), True, (50,50,50))
    #зачисткаwrrrrrr
    window.fill((111, 0, 0))
    #Отрисовка 
    player1.reset()
    player2.reset()
    ball.reset()
    window.blit(image_score1, (10,20))
    window.blit(image_score2, (575,20))

