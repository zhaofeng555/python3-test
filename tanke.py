#/usr/bin/env python3
import pygame, sys

#初始化
pygame.init()

#初始化混音器
pygame.mixer.init()
#设置背景音乐
pygame.mixer.music.load('resources/Contra.ogg')
#设置背景音乐大小
pygame.mixer.music.set_volume(0.2)
#设置播放次数 -1 无限循环
# pygame.mixer.music.play(loops=-10)

#载入效果音乐
tank_run_sound = pygame.mixer.Sound('resources/Tank_travel.wav')
tank_run_sound.set_volume(0.2)

#设置大小
size = width, height = 600, 400

screen = pygame.display.set_mode(size)
pygame.display.set_caption('第一个小程序！')

#背景图
#bg = (100, 200, 200)
bg = pygame.image.load('resources/bg.jpg')

bgposition = bg.get_rect()

#加载坦克图片
img = pygame.image.load('resources/tank_01.png')
#获取图片位置
position = img.get_rect()

#速度
speed = [1, 0]

#记录帧
i=0;

#记录切换
change = 1

#开关
state = False

#方向
direct = 'R'

while True:
    i= i+1
    if i%10 == 0:
        state = True
    else:
        state = False

    if state:
        if change == 1:
            img = pygame.image.load('resources/tank_02.png')
            change = 2
        else :
            img = pygame.image.load('resources/tank_01.png')
            change = 1

    if direct == 'L':
        img2 = pygame.transform.flip(img, True, False)
    else:
        img2 = img

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            tank_run_sound.play(loops=-1)
            if event.key == pygame.K_RIGHT:
                speed = [2, 0]
                direct = 'R'
            if event.key == pygame.K_LEFT:
                speed = [-2, 0]
                direct = 'L'
            if event.key == pygame.K_UP:
                speed = [0, -2]
            if event.key == pygame.K_DOWN:
                speed = [0, 2]

        if event.type == pygame.KEYUP:
            speed = [0, 0]
            tank_run_sound.stop()
    #填充背景
    #screen.fill(bg)
    screen.blit(bg, bgposition)
    #循环移动
    position = position.move(speed)
    #更新图像
    screen.blit(img2, position)
    #更新界面
    pygame.display.flip()
    pygame.time.Clock().tick(60)

