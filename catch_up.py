from pygame import *
from random import choice


#создай окно игры
window = display.set_mode((700, 500))

display.set_caption("Догонялки")

bg = transform.scale(image.load("background.jpg"), (700, 500))


clock = time.Clock()
FPS = 60
speed = 10
game = True


mixer.init()



hit = mixer.Sound("hit.ogg")
hit.set_volume(0.2)



class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size):
        super().__init__()
        self.size = size
        self.image = transform.scale(image.load(player_image), size)
        self.speed_x = player_speed
        self.speed_y = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed_y
        if keys[K_s] and self.rect.y < 380:
            self.rect.y += self.speed_y
    def update2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed_y
        if keys[K_DOWN] and self.rect.y < 380:
            self.rect.y += self.speed_y
            
            

class Enemy(GameSprite):
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.y <= 0:
            self.speed_y *= -1

        if self.rect.y >= 450:
            self.speed_y *= -1

        
       



speed = 5
score1 = 0
score2 = 0


player1 = Player("platform1.png", 30, 250, 7, (30, 120))
player2 = Player("platform2.png", 630, 250, 7, (30, 120))
enemy = Enemy("ball.png", 350, 250, 0, (50, 50))


font.init()
font_win = font.SysFont("Arial", 70)
font_helper = font.SysFont("Arial", 40)
win = font_win.render("", True, (255, 215, 0))
pl1score = font_win.render(str(score1), True, (255, 255, 255))
pl2score = font_win.render(str(score2), True, (255, 255, 255))
helper = font_helper.render("Нажмите пробел для перезапуска", True, (255, 255, 255))



finish = True


while game:

    window.blit(bg, (0, 0))
    clock.tick(FPS)
    player1.reset()
    player2.reset()
    enemy.reset()
    window.blit(pl1score, (250, 20))
    window.blit(pl2score, (450, 20))


    if finish == False:
        player1.update()
        player2.update2()
        enemy.update()


        if sprite.collide_rect(player1, enemy):
            enemy.speed_x = speed
            hit.play()

        if sprite.collide_rect(player2, enemy):
            enemy.speed_x = -speed
            hit.play()
        if enemy.rect.x <= 0:
            finish = True
            score2 += 1

            pl2score = font_win.render(str(score2), True, (255, 255, 255))
            if score2 >= 10:
                win = font_win.render("Победил 2 игрок", True, (255, 255, 255))
                
                
           

        if enemy.rect.x >= 650:
            finish = True
            score1 += 1
            pl1score = font_win.render(str(score1), True, (255, 255, 255))

            if score1 >= 10:
                win = font_win.render("Победил 1 игрок", True, (255, 255, 255))
                
                


    if finish == True:
        enemy.speed_x = 0
        enemy.speed_y = 0

        enemy.rect.x = 350
        enemy.rect.y = 250

        player1.rect.y = 250
        player2.rect.y = 250

       

            
        

        window.blit(helper, (120, 350))
        window.blit(win, (150, 250))


    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE and finish:
                enemy.speed_x = choice([-speed, speed])
                enemy.speed_y = choice([-speed, speed])
                
                

                finish = False
                if score1 >= 10 or score2 >= 10:

                    score1 = 0
                    score2 = 0
                    pl1score = font_win.render(str(score1), True, (255, 255, 255))
                    pl2score = font_win.render(str(score2), True, (255, 255, 255))

                   
                    win = font_win.render("", True, (255, 215, 0))
                     


        

    display.update()

#задай фон сцены

#создай 2 спрайта и размести их на сцене



#обработай событие «клик по кнопке "Закрыть окно"»