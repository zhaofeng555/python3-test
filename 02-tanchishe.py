# !/usr/bin/env python3
# -*- coding: encoding -*-

import pygame, sys, random
from pygame.locals import *

redColor = pygame.Color(255, 0, 0)
blackColor = pygame.Color(0, 0, 0)
whiteColor = pygame.Color(255, 255, 255)

#游戏结束
def gameOver():
	pygame.quit()
	sys.exit()

# main函数
def main():
	pygame.init()
	fps = pygame.time.Clock()
	pygame.display.set_mode(640, 480)

	snakePosition = [100, 100]

	snakeBody =[[100, 100], [80,100], [60,100]]

	targetPosition = [300, 300]

	targetFlag = 1
	direction = 'right'
	changeDirection = direction

	while True:
		for event in pygame.event.get():
			


