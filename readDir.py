#!/usr/bin/env python3

import os
import os.path

rootDir="/Users/haojianguo/backup/Python2"

def readDir():
	pass

for parent, dirnames, filenames in os.walk(rootDir):
	for dirname in dirnames:
		print("dirname is :"+dirname)

	for filename in filenames:
		print("filename is" + filename)
		print(filename)
