from pygame import *

class GameSprite(sprite.Sprite):
 #конструктор класса
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       #вызываем конструктор класса (Sprite):
       sprite.Sprite.__init__(self)


       #каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed


       #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 #метод, отрисовывающий героя на окне
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
   #метод для управления спрайтом стрелками клавиатуры
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
win_width = 600
win_height = 500
display.set_caption("Ping Pong")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load('background.jpg'), (win_width, win_height))
racket1 = Player('racket2.png', -30, 15, 130, 150, 8)
racket2 = Player('racket2.png', 510, 15, 130, 150, 8)
finish = False
run = True
while run:
   #событие нажатия на кнопку Закрыть
    for e in event.get():
        if e.type == QUIT:
            run = False
    if finish != True:
        window.blit(background,(0,0))
        racket1.update_l()
        racket1.reset()
        racket2.update_r()
        racket2.reset()
        time.delay(50)
    display.update()