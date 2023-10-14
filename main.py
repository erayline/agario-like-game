 
# """burada windows oluşturuyoruz. herhangi bir değişkeni pygame.display.set_mode(genişlik, yükseklik)"""
# """fps konusunu clock = pygame.time.clock() şeklinde tanımlıyoruz daha sonra ise clock.tick(FPS) yapıyoruz.  clock = """
# """pygame.display.update == yazdirdiğimiz şeyleri güncellememizi sağliyor."""
# """eğer ekrana bir şey eklemek istiyorsam blit yazmam lazım."""
# """pygame.rect ile bir nesne oluşturduğumuzda .x diyerek konumunu öğrenebiliyoruz."""
# """birden çok tuşa basılıp basılmadığını anlamak için mesela key_pressed adında bir değişkene pygame.key.get_pressed"""
import pygame
from pygame import mixer
import os
import random
import math
skor=0
pygame.init()

ses1 = pygame.mixer.Sound("pop1.wav")
ses2 = pygame.mixer.Sound("pop3.wav")
ses4 = pygame.mixer.Sound("pop5.wav")
ses6 = pygame.mixer.Sound("pop7.wav")
sesListesi = [ses1,ses2,ses4,ses6]


WIDTH, HEIGHT = 1700, 800
MYCOLOR = (10,10,40)
FPS = 60
global SNAKE_HEIGHT
global SNAKE_WIDTH
SNAKE_HEIGHT = 100
SNAKE_WIDTH = 100
BUYUME = 5

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("orjinal Agar.io")
"""burada başlik belirle"""
arkaplanResmi = pygame.image.load(os.path.join('space.png'))
arkaplanResmi = pygame.transform.scale(arkaplanResmi,(WIDTH,HEIGHT))
TRANSPARENT_SNAKE = pygame.image.load(os.path.join('göz.png'))
SNAKE = pygame.transform.scale(TRANSPARENT_SNAKE,(SNAKE_WIDTH,SNAKE_HEIGHT))

def konumBelirle(yemek):
    yemek.coorx = random.randint(3,WIDTH - 3)
    yemek.coory = random.randint(3,HEIGHT - 3)
def renkBelirle(yemek):
    yemek.R = random.randint(0,255)
    yemek.G = random.randint(0,255)
    yemek.B = random.randint(0,255)
class yemek:
    def __init__(self):
        self.name = "ben yemek"
        konumBelirle(self)
        renkBelirle(self)
def yemekleriOlustur(adet):
    global yemekListesi
    yemekListesi = []
    for i in range(adet):
        i = yemek()
        yemekListesi.append(i)
def yemekleriYaz(yemekListesi):
    for i in yemekListesi:
        pygame.draw.circle(WIN,(i.R,i.G,i.B),(i.coorx,i.coory),10)
def handle_movement(keys_pressed, green):
        if keys_pressed[pygame.K_UP]:
            if (green.y >= 0): 
                green.y -= 4
        if keys_pressed[pygame.K_DOWN]:
            if (green.y <= HEIGHT-SNAKE_HEIGHT):
                green.y += 4
        if keys_pressed[pygame.K_RIGHT]:
            if (green.x <= WIDTH - SNAKE_WIDTH): 
                green.x += 4
        if keys_pressed[pygame.K_LEFT]:
            if (green.x >= 0): 
                green.x -= 4
    
font = pygame.font.SysFont("arial",50)

def yaziOlustur(text,font,color,x,y):
    img = font.render(text,True,color)
    WIN.blit(img,(x,y))



def yemekYedim():
    global skor
    global SNAKE_HEIGHT
    global SNAKE_WIDTH
    global SNAKE
    skor +=1
    rastgeleSes = random.randint(0,3)
    sesListesi[rastgeleSes].set_volume(0.3)
    sesListesi[rastgeleSes].play()
    SNAKE_WIDTH += BUYUME
    SNAKE_HEIGHT += BUYUME
    SNAKE = pygame.transform.scale(TRANSPARENT_SNAKE,(SNAKE_WIDTH,SNAKE_HEIGHT))
    WIN.blit(SNAKE, (green.x,green.y))
    green.x -=  BUYUME/2
    green.y -=  BUYUME/2
    pygame.display.update()

def collisionCheck(yemekListesi,SNAKE_HEIGHT,SNAKE_WIDTH,green):
    calis=0
    while (calis < len(yemekListesi)):
        for i in yemekListesi: 
            if(green.x < i.coorx < green.x + SNAKE_WIDTH):
                if (green.y < i.coory < green.y +SNAKE_HEIGHT):
                    print("yemek yedim")
                    yemekListesi.remove(i)
                    return True
        calis += 1
level = 1
baslangic = 1
if level == 1:
    yemekleriOlustur(baslangic)
def draw_window(green):
    global level
    global baslangic
    global SNAKE
    WIN.fill(MYCOLOR)
    WIN.blit(arkaplanResmi,(0,0))
    yemekleriYaz(yemekListesi)
    WIN.blit(SNAKE, (green.x,green.y))
    if len(yemekListesi) == 0:
        level = 2
    if level == 2:
        yemekleriOlustur(baslangic)
        level = 0
        baslangic +=1
    yaziOlustur("Skor: {}      LEVEL: {}".format(skor,baslangic),font,(0,200,0),WIDTH/2 - 200,10)
    pygame.display.update()

green = pygame.Rect(0,0,SNAKE_WIDTH,SNAKE_WIDTH)
clock = pygame.time.Clock()
run = True

while run:
    clock.tick(FPS)
    keys_pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys_pressed[pygame.K_ESCAPE]:
            run = False
        if event.type == pygame.K_SPACE:
            yemekleriOlustur(20)
    handle_movement(keys_pressed,green)



    if collisionCheck(yemekListesi,SNAKE_HEIGHT,SNAKE_WIDTH,green):
        yemekYedim()

    draw_window(green)
    


pygame.quit()   