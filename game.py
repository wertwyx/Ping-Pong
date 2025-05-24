from pygame import *
clock = time.Clock()
FPS = 60
joystick.init()
joysticks = [joystick.Joystick(x) for x in range(joystick.get_count())]

window = display.set_mode((700, 500), flags = RESIZABLE)
display.set_caption('ping pong')
background = transform.scale(image.load('pingpong.jpg'),(700, 500))

class Gamesprite(sprite.Sprite):

    def __init__(self,pos_x,pos_y,speed,size):
        sprite.Sprite.__init__(self)
        ball = Surface(size)
        ball.fill((100,100,100))
        self.image = transform.scale(ball,size)
        self.size = size
        self.speed = speed
        self.vector = Vector2(1,1).normalize()
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
    def update(self):
        self.rect.x += self.vector.x * self.speed
        self.rect.y += self.vector.y * self.speed
        if self.rect.x <= 0 or self.rect.x >= (700 - self.size[0]):
            self.vector.x = -self.vector.x
            self.speed += 0.1
        if self.rect.y <= 0 or self.rect.y >= (500 - self.size[0]):
            self.vector.y = -self.vector.y
            self.speed += 0.1 




class player(Gamesprite):
    def update(self, K_p = K_p, K_l = K_l, K_r = K_r, K_t = K_t):
        key_pressed = key.get_pressed()
        if key_pressed[K_p] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_pressed[K_l] and self.rect.y < 430:
            self.rect.y += self.speed   
        if key_pressed[K_r] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_pressed[K_t] and self.rect.y < 430:
            self.rect.y += self.speed

    def joystick_update(self, pos_x, pos_y):
        self.rect.x += self.speed * pos_x
        self.rect.y += self.speed * pos_y




ball = Gamesprite(350,250,10,(10,10))
player1 = player(30,250,10,(10,100))
player2 = player(670,250,10,(10,100))
player3 = player(350, 30, 10, (100, 10))
player4 = player(350, 470, 10, (100, 10))
game = True
pos_x = 0

while game:
    clock.tick(FPS)
    for e in event.get():
            if e.type == QUIT:
                game = False
            if e.type == JOYAXISMOTION:
                print("M")
                pos_x = joysticks[0].get_axis(0)
                print(pos_x)
                


    window.blit(background,(0,0))
    ball.reset()
    ball.update()
    player1.reset()
    player1.update(K_p = K_w,K_l = K_s)
    player2.reset()
    player2.update(K_r = K_UP, K_t = K_DOWN)
    player4.reset()
    #player4.update(K_r = K_u, K_t = K_i)
    player3.reset()
    player3.joystick_update(pos_x, 0)
#    if ball.rect.x > 690 or ball.rect.x < 10:
#        game = False
#    if ball.rect.x > 690:
#        player2.kill()


    if sprite.collide_rect(ball,player1):
        ball.vector.x = -ball.vector.x

    if sprite.collide_rect(ball,player2):
        ball.vector.x = -ball.vector.x

    if sprite.collide_rect(ball,player3):
        ball.vector.x = -ball.vector.x

    if sprite.collide_rect(ball,player4):
        ball.vector.x = -ball.vector.x

    
    
    display.update()
