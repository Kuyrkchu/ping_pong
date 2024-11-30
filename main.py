from pygame import *
init()
font.init()

game = True 
finish = False
win_w, win_h = (800, 600)
FPS = 75


window = display.set_mode((win_w, win_h))
font0 = font.SysFont('Arial', 50)
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self,image_file, x, y, speedx, speedy, w, h):
        self.image = transform.scale(image.load(image_file), (w,h))
        self.rect = self.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = x
        self.speedy = y

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
        if keys[K_UP]:
            self.rect.y -= self.speedy
        if keys[K_DOWN]:
            self.rect.y += self.speedy
                

while game:
    #обновление экрана
    display.update()
    #задержка
    clock.tick(FPS)
    #обработка события
    for e in event.get():
        if e.type == QUIT:
            game = False
    #игровая логика
    #зачистка
    window.fill((111, 0, 0))
    #Отрисовка 

