# -*- coding: utf-8 -*-
"""
:author: Lethons
:website: lethons@163.com
:function: Numeric sorting
"""

for bai in range(1, 5):
	for shi in range(1, 5):
		if shi != bai:
			for ge in range(1, 5):
				if bai !=ge and shi != ge:
						num = bai*100 + shi*10 + ge
						print(str(num)) 
