"""
1.3牛顿迭代法求方程根
编写用牛顿迭代法求方程根的函数，方程为ax3+bx2+cx+d=0，系数a、b、c、d由主函数输入，求x在1附近的一个实根。
求出根后，由主函数输出。
牛顿迭代法的公式：x=x0的-f(x0)/f'(x0)次幂，设迭代到|x-x0|≤10的-5次幂时结束
"""

# 我的答案 (同参考答案)
import datetime

def equation(a=None, b=None, c=None, d=None):
    x0 = 1.5
    while True:
        f_x0 = a*pow(x0,3) + b*pow(x0,2) + c*x0 + d
        f_xok = 3*a*pow(x0,2) + 2*b*x0 + c
        # x = 1 / pow(x0,f_x0/f_xok)
        x = x0 - f_x0/f_xok
        if abs(x - x0) < 1/pow(10,9):
            return x
        x0 = x

a = input('>> a = ')
b = input('>> b = ')
c = input('>> c = ')
d = input('>> d = ')
start = datetime.datetime.now()
print(f'x = {equation(a=float(a), b=float(b), c=float(c), d=float(d))}')
end = datetime.datetime.now()
print(start, end)
print(f'{(end - start).seconds} seconds')

