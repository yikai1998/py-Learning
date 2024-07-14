"""
1.4百钱百鸡
中国古代数学家张丘建在他的《算经》中提出了一个著名的“百钱百鸡问题”：
一只公鸡值五钱，一只母鸡值三钱，三只小鸡值一钱，
现在要用百钱买百鸡，请问公鸡、母鸡、小鸡各多少只？
"""

# 我的答案
import datetime
start = datetime.datetime.now()
for ch_a in range(0, 21):
    for ch_b in range(0, 34):
        if (100 - ch_a - ch_b) % 3 != 0:
            continue
        for ch_c in range(3, 300, 3):
            if any([5*ch_a + 3*ch_b + ch_c/3 != 100, ch_a + ch_b + ch_c != 100]):
                continue
            print(f'公鸡{ch_a}只', f'母鸡{ch_b}只', f'小鸡{ch_c}只')
end = datetime.datetime.now()
print(f'{(end-start).total_seconds()} seconds')

# 参考答案
start = datetime.datetime.now()
# 外层循环控制公鸡数量取值范围为0～20
cock = 0
while cock <= 20:
    # 内层循环控制母鸡数量取值范围为0～33
    hen = 0
    while hen <= 33:
        # 小鸡的数量
        chicken = 100 - cock - hen
        if 5 * cock + 3 * hen + chicken / 3.0 == 100:
            print("cock=%2d,hen=%2d,chicken=%2d" %(cock,hen,chicken))
        hen += 1
    cock += 1
end = datetime.datetime.now()
print(f'{(end-start).total_seconds()} seconds')

# 改进
start = datetime.datetime.now()
for ch_a in range(0, 21):
    for ch_b in range(0, 34):
        if any([(100 - ch_a - ch_b) % 3 != 0, 5*ch_a + 3*ch_b + (100 - ch_a - ch_b)/3 != 100, ch_a + ch_b + (100 - ch_a - ch_b) != 100]):
            continue
        print(f'公鸡{ch_a}只', f'母鸡{ch_b}只', f'小鸡{ch_c}只')
end = datetime.datetime.now()
print(f'{(end-start).total_seconds()} seconds')
