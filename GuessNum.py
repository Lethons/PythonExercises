# -*- coding: utf-8 -*-
"""
:author: Lethons
:website: lethons@163.com
:function: guess number.
"""

import random

def get_random_num():
	rnum = random.randint(0,999)
	return rnum

def input_your_num():
	inum = input('Please input a num(<1000): ')
	inum = int(inum)
	return inum

def compare_num(rnum, inum):
	if inum > rnum:
		print('Your number is bigger')
		flag = True
	elif inum < rnum:
		print('Your number is smaller')
		flag = True
	else:
		print('Success,the number is ' + str(inum))
		flag = False
	return flag


def main():
	flag = True
	rnum = get_random_num()
	while flag:
		inum = input_your_num()
		flag = compare_num(rnum, inum)

if __name__ == '__main__':
	main()
