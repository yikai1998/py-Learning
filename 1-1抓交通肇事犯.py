"""
1.1抓交通肇事犯
一辆卡车违反交通规则，肇事逃逸，现场有三位目击者，但都没记住车牌号，只记住了一些特征。
甲：牌照前两位数字相同
乙：牌照后两位数字相同，但与前两位数字不同
丙：四位的车号刚好是一个整数的平方
请根据以上线索推出车牌号
"""

# 我的答案1
import datetime
import math
start = datetime.datetime.now()
car_number = []
a = int(math.sqrt(1000)) + 1
b = int(math.sqrt(9999))
for i in range(a, b):
    number = str(pow(i, 2))
    # print(number)
    if any([number[0]!=number[1], number[2]!=number[3], number[:2]==number[-2:]]):
        continue
    car_number.append(number)
    break
print(car_number)
end = datetime.datetime.now()
print(f'{(end-start).total_seconds()} seconds')

# 我的答案2
start = datetime.datetime.now()
car_number = []
for number in range(1000, 10000):
    if math.sqrt(number) % 1 != 0:
        continue
    number = str(number)
    if any([number[0]!=number[1], number[2]!=number[3], number[:2]==number[-2:]]):
        continue
    car_number.append(number)
    break
print(car_number)
end = datetime.datetime.now()
print(f'{(end-start).total_seconds()} seconds')

# 参考答案
start = datetime.datetime.now()
flog = 0 #标识，一旦找到车牌 就终止全部循环
# i代表车牌前两位的数字，j代表车牌后两位的数字
for i in range(10):
    if flog:
        break
    for j in range(10):
        if flog:
            break
        if i != j:
            k = 1000*i + 100*i + 10*j + 1*j
            for temp in range(31, 100):
                if temp * temp == k:
                    print(f'车牌号为：{k}')
                    flog = 1
                    break
end = datetime.datetime.now()
print(f'{(end-start).total_seconds()} seconds')
