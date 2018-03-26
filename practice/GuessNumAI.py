# -*- coding: utf-8 -*-
"""
:author: Lethons
:website: lethons@163.com
:function: guess number by AI.
"""

def find_num():
	times = 1
	fnum = 500
	Max = 1000
	Min = 0
	inum = input('Please input a number(0~999): ')
	inum = int(inum)
	while fnum != inum:
		fnum = int(fnum)
		if fnum > inum:
			Max = fnum
			if Max - Min < 3:
				fnum = fnum -1
			else:
				fnum = (Min + Max)/2
			times = times + 1
		elif fnum < inum:
			Min = fnum
			if Max - Min < 3:
				fnum = fnum + 1
			else:
				fnum = (Min + Max)/2
			times = times + 1
	print('Use ' + str(times) + ' times.')
	print('The number is ' + str(fnum) + '.')

if __name__ == '__main__':
	find_num()

