from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and player.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and player.x < win_width:
            self.rect.x += self.speed
        if keys[K_UP] and player.y > 5:
            self.rect.x -= self.speed
        if keys[K_DOWN] and player.y < win_height:
            self.rect.x += self.speed

class Enemy(GameSprite):
    def __init__(self,player_image,player_x, player_y, player_speed, left_border, right_border):
        super().__init__(player_image, player_x, player_y, player_speed)
        self.direction = "left"
        self.left_border = left_border
        self.right_border = right_border

    def update(self):
        if self.direction == "left":
            self.rect.x -= self.speed
            if self.rect.x <= self.left_border:
                self.direction = "right"
        else:
            self.rect.x += self.speed
            if self.rect.x >= self.right_border:
                self.direction = "left"



win_width = 700
win_height = 500


window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))
 

player = GameSprite("hero.png", 100, 100, 10)
cyborg = GameSprite("cyborg.png", 200, 100, 10)
final = GameSprite("treasure.png", 300, 300, 0)




 
game = True
clock = time.Clock()
FPS = 60

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
 
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    
    window.blit(background,(0, 0))

    player.update()
    player.reset()
    cyborg.update
    cyborg.reset()
    final.reset()
    
    display.update()
    clock.tick(FPS)