"""
1.2兔子产子
有一对兔子，从出生后的第3个月起每个月都生一对兔子，
小兔子长到第3个月后每个月又生一对兔子。
假设所有的兔子都不死，问30个月内每个月的兔子总对数为多少？
"""

# 我的答案
import datetime
start = datetime.datetime.now()
amt_1m, amt_2m, amt_3m = 1, 0, 0
month = 1
print(amt_1m, amt_2m, amt_3m)
print(f'第{month}个月的兔子总对数为 {amt_3m+amt_2m+amt_1m}对 \n')
while month < 30:
    change_3m = 1*amt_2m
    change_2m = 1*amt_1m - 1*amt_2m
    change_1m = 1 * amt_3m + 1 * amt_2m - 1 * amt_1m

    amt_3m += change_3m
    amt_2m += change_2m
    amt_1m += change_1m

    print(amt_1m, amt_2m, amt_3m)
    print(f'第{month+1}个月的兔子总对数为 {amt_3m+amt_2m+amt_1m}对 \n')
    month += 1
end = datetime.datetime.now()
print(f'{(end - start).total_seconds()} seconds')

# 参考答案
# 这就是Fibonacci数列。总结数列规律即为从前两个月的兔子对数可以推出第3个月的兔子对数。[每个月增加的对数其实就是上个月里2月和3月的兔子总数]
start = datetime.datetime.now()
fib1 = 1
fib2 = 1
i = 3
# 输出前两个月的兔子对数
print('%6d\t%6d' %(fib1, fib2), end='\t')
while i <= 30:
    fib = fib1 + fib2
    print('%6d' %fib, end='\t')
    if i % 4 == 0:
        print() # 每行输出四个
    fib2 = fib1
    fib1 = fib
    i += 1
end = datetime.datetime.now()
print(f'{(end - start).total_seconds()} seconds')

# 进一步改进，减少变量
start = datetime.datetime.now()
fib1 = 1
fib2 = 1
i = 3
# 输出前两个月的兔子对数
print('%6d\t%6d' %(fib1, fib2), end='\t')
while i <= 30:
    print('%6d' %(fib1 + fib2), end='\t')
    if i % 4 == 0:
        print() # 每行输出四个
    fib2 = fib2 + fib1
    fib1 = fib2 - fib1
    i += 1
end = datetime.datetime.now()
print(f'{(end - start).total_seconds()} seconds')
