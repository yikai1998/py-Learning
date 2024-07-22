"""
1.10 数制转换
给定一个M进制的数x，实现对x向任意一个非M进制的数的转换
"""
import datetime
import sys
import math

go = True
while go:
    x = input('>> 输入一个整数数值：')
    y = int(input('>> 设定默认进制：'))
    if max([int(f) for f in x]) >= y:
        print('>> 进制设定错误')
        continue
    original = 0
    pw = 0
    for figure in x[::-1]:
        original += int(figure)*pow(y, pw)
        pw += 1
    print(f'{x}在{y}进制下的数值为{original}')
    _original = original
    z = int(input('>> 输入希望转成的进制：'))
    pw_max = int(math.log(original, z))
    fg_list = []
    while pw_max >= 0:
        fg = int(original / pow(z, pw_max))
        fg_list.append(fg)
        original = original - fg*pow(z, pw_max)
        pw_max -= 1
    fg_list = [str(x) for x in fg_list]
    print(f'{_original}在{z}进制下的数值为{' '.join(fg_list)}')
    _ = input('>> 输入q以退出，否则继续')
    if _ == 'q':
        break

