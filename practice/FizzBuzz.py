# -*- coding: utf-8 -*-
"""
:author: Lethons
:website: lethons@163.com
:function: output FizzBuzz.
"""


def print_num():
    for num in range(0, 101):
        if num % 15 == 0:
            print('FizzBuzz')
        elif num % 3 == 0:
            print('Fizz')
        elif num % 5 == 0:
            print('Buzz')
        else:
            print(num)


def main():
    print_num()


if __name__ == '__main__':
    main()
