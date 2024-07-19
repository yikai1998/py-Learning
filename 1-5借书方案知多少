"""
1.5借书方案知多少
小明有5本新书，要借给A、B、C三位小朋友，
若每人每次只能借1本，则可以有多少种不同的借法？
"""

# 我的答案
import datetime
start = datetime.datetime.now()
kids = {
    'A': '',
    'B': '',
    'C': ''
}
books = [['b1', 'b2', 'b3', 'b4', 'b5']] * 3
p = 0
for a in books[0]:
    for b in books[1]:
        if b == a:
            continue
        for c in books[2]:
            if any([a==c, b==c]):
                continue
            kids.update({
                'A': a,
                'B': b,
                'C': c
            })
            print(kids)
            p += 1
print(f'有{p}种不同的借法')
end = datetime.datetime.now()
print(f'{(end - start).total_seconds()} seconds')


# 参考答案
start = datetime.datetime.now()
i = 0
for a in range(1, 6):
    # 用来控制B借阅图书的编号
    for b in range(1, 6):
        # 用来控制C借阅图书的编号
        for c in range(1, 6):
            if a != b and a != c and c != b:
                print("A:%2d B:%2d C:%2d " % (a, b, c), end='')
                i += 1
                if i % 4 == 0:
                    print()  # 换行
print("共有%d种有效借阅方法" % i)
end = datetime.datetime.now()
print(f'{(end - start).total_seconds()} seconds')
