# -*- coding: utf-8 -*-
"""
:author: Lethons
:website: lethons@163.com
:function: A clock that rings the bell.
"""

import time
import winsound

def bee(now_min):
	if now_min == 59:
		winsound.Beep(1000, 600)
	if now_min == 29:
		winsound.Beep(1000, 300)
		winsound.Beep(1000, 300)

def main():
	while True:
		now_time = time.localtime()
		now_min = now_time.tm_min
		now_sec = now_time.tm_sec
		time.sleep(60 - now_sec)
		print(time.asctime())
		bee(now_min)

if __name__ == '__main__':
	main()

