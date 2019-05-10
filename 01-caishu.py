#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

inp_list=[]
for i in xrange(3):
	inp_number = input("请输入你猜的数字：")
	inp_list.append(inp_number)
	print ("cuole")
	if i == 2:
		while True:
			number = random.randint(0,9)
			if number in inp_list:
				continue
			break

print ("jieshu")