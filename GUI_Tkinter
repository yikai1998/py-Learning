# coding=gbk

import tkinter

# 第三章 tkinter窗口设计


win = tkinter.Tk()
#　win.mainloop() #进入等待与处理窗口事件

# 创建窗口、设置窗口属性、设置窗口位置
win.title('tkinter的初级应用') #添加窗口标题
txt = tkinter.Label(win, text='\n\nHello World!\n\n', bg='green').pack() #在窗口中添加一行文字
win.geometry('300x150') #窗口的大小；'300x150+x+y'表示距离屏幕左上角的距离，'300x150-x-y'表示距离屏幕右下角的距离
# 若希望在屏幕中间显示
# x = (win.winfo_screenwidth() - 300) / 2
# y = (win.winfo_screenheight() - 150) / 2
# win.geometry(f'300x150+{int(x)}+{int(y)}')
win.configure(bg='pink') #窗口的背景颜色
win.maxsize(600, 600) #设置窗口的最大尺寸
win.mainloop()

# 窗口设计的核心 -- Widget组件
win2 = tkinter.Tk()
# tkinter模块包含了多种组件，从功能上可以分为7类
# {
#   文本类组件： Label标签组件、Entry单行文本组件、Text多行文本组件、Spinbox输入组件、Scale数字范围组件
#   按钮类组件： Button按钮组件、Radiobutton单选组件、Checkbutton复选框组件
#   选择列表类组件： ListBox列表框组件、Scrollbar滚动条组件、OptionMenu下拉列表、Combobox组合框
#   容器类组件： Frame框架组件、LabelFrame标签框架组件、Toplevel顶层窗口、PaneWindow窗口布局管理、Notebook选项卡
#   会话类组件： Message消息框、Messagebox对话框
#   菜单类组件： Menu菜单组件、Toolbar工具栏、Treeview树菜单
#   进度条组件： Progressbar添加进度条
# }

# 每个组件痘有各自的属性，但有些属性是各组件通用的
# {
#   fg: 设置组件的文字颜色
#   bg: 设置组件的背景颜色
#   width: 设置组件的宽度
#   height: 设置组件的高度
#   anchor: 文字在组件内输出的位置, center/nw/sw/s/e/...
#   padx: 组建的水平间距
#   pady: 组件的垂直间距
#   font: 组件的文字样式
#   relief: 组件的边框样式, solid/raised/sunken/flat/groove/ridge
#   cursor: 鼠标停留在组件上时的样式
# }

# tkinter.Label(win2, text='小扣柴扉久不开', fg='red', bg='blue', font='华文新魏 16 bold italic underline overstrike').pack()
# 上面这个方法是直接在组件中设置属性，此外还可以通过config()来配置参数，如下：
'''label = tkinter.Label(win2, text='小扣柴扉久不开')
label.configure(bg='#DEF1EF', fg='green', font=18)
label.pack()'''

# keys()方法可以获取该组件的所有参数，返回的是一个列表
win2.mainloop()

# coding=gbk

import tkinter

# 第四章 tkinter布局管理

# pack()方法
win = tkinter.Tk()

# 参数：
# side (top, bottom, left, right): 设置组件水平展示或垂直展示
# padx pady: 设置组件距离窗口的水平垂直距离
# ipadx ipady: 设置组件内的文字距离组件边界的水平或垂直距离
# fill: 设置组件填充所在的空白空间的方式
# expand: 设置组件是否完全填充其余空间
# achor: 设置组件在窗口中的位置 [nw, sw, center, s, e, ...]
# before after: 设置该组件应位于指定组件的前面或后面

text1 = '枯藤老树昏鸦'
text2 = '小桥流水人家'
text3 = '古道西风瘦马'
text4 = '夕阳西下'
text5 = '断肠人在天涯'

text1 = tkinter.Label(win, text=text1, bg='green', fg='red', font='华文新魏 20 bold')
text2 = tkinter.Label(win, text=text2, bg='yellow', fg='blue', font='华文新魏 20 bold')
text3 = tkinter.Label(win, text=text3, bg='pink', fg='black', font='华文新魏 20 bold')
text4 = tkinter.Label(win, text=text4, bg='purple', fg='white', font='华文新魏 20 bold')
text5 = tkinter.Label(win, text=text5, bg='orange', fg='blue', font='华文新魏 20 bold')
text1.pack(side='top', fill='y', pady=20, ipadx=10)
text2.pack(side='top', fill='x', pady=20, ipadx=10) # 虽然上面没有被全部填充，但因为顺序是top往下，你没法越级向上填充
text3.pack(side='top', fill='y', pady=20, ipadx=10)
text4.pack(side='top', fill='y', pady=20, ipadx=10)
text5.pack(side='top', fill='y', anchor='ne') # fill是把整行/列填满，但这里他上面没法填满，所以干脆就不填了；如果想至少把下面给填了，“再”传一个expand
win.mainloop()


win2 = tkinter.Tk()

txt1 = '请确认是否要卸载此软件'
txt2 = '继续卸载'
txt3 = '点错了，继续使用'
txt1 = tkinter.Label(win2, text=txt1, bg='blue', font='宋体 20 bold')
txt2 = tkinter.Label(win2, text=txt2, bg='red', fg='white', font='宋体 20 bold')
txt3 = tkinter.Label(win2, text=txt3, bg='green', fg='yellow', font='宋体 20 bold')
txt1.pack(side='top', pady=200)
txt3.pack(side='right', anchor='se', pady=50, padx=120)
txt2.pack(side='right', anchor='se', pady=50, padx=40)
win2.mainloop()


# grid()方法   ----类似EXCEL表格的网格布局方式
win3 = tkinter.Tk()

# 参数
# row column: 组件所在的行 列；第一行和第一列的序号应该是0
# rowspan columnspan: 组件横向纵向合并的行列数 【合并行列时，只是增大了组件的占用空间，而不会增加组件本身】
# sticky:组件填充所分配空间空白区域的方式 (N上对齐, S, W, E) ==>可以组合使用，如'NSE'
'''
默认情况下，宽度较小的组件会以较宽的组建为基准，将同列其他组件居中对齐
所以sticky可以让他们对齐'''
# padx pady: 组件距离窗口边界的水平方向以及垂直方向的距离

# 当窗口大小发生改变时，可以通过 rowconfigure()方法和 columnconfigure()方法改变某行或某列组件所占空间随窗口缩放的比例，针对的是父容器而不是组件
# 第一个参数表示第X行/列，第二个参数weight表示随窗口缩放的比例为XX

win3.rowconfigure(0, weight=1)
win3.columnconfigure(1, weight=1)
txt1 = tkinter.Label(win3, width=30, height=10, relief='groove', bg='yellow')
txt1.grid(row=0, column=0, sticky='NW')
txt2 = tkinter.Label(win3, width=30, height=10, relief='groove', bg='green')
txt2.grid(row=0, column=1, sticky='NE')
win3.mainloop()


# place()方法 ----可以设置组件的大小以及组件在容器中的精准位置

win4 = tkinter.Tk()
# 参数
# x y: 设置组件距离窗口左侧 顶部的水平垂直距离
# width height: 设置组件的宽度  高度
# relx rely: 设置组件距离容器左侧 顶部的相对距离，数值距离在0-1之间
# relwidth relheight: 组件相对父容器的宽度 高度

win4.title('华容道')
pic1 = tkinter.Label(win4, text='赵云', bg='green', relief='groove', font=14)
pic2 = tkinter.Label(win4, text='曹操', bg='pink', relief='groove', font=14)
pic3 = tkinter.Label(win4, text='黄忠', bg='red', relief='groove', font=14)
pic1.place(relwidth=0.25, relheight=0.3, relx=0, rely=0)
pic2.place(relwidth=0.5, relheight=0.3, relx=0.25, rely=0)
pic3.place(relwidth=0.25, relheight=0.3, relx=0.75, rely=0)
win4.mainloop()

# coding=gbk

import tkinter

# 第五章 文本类组件



# Label 标签组件

win = tkinter.Tk()
# 可以添加图片，仅支持.png格式
img = tkinter.PhotoImage(file=r'C:\Users\Ben\Desktop\learnnovel.png')
# 参数compound可以设置图片与文字的显示位置 (top图片位于文字上方, center图片文字重叠且文字在图的上层, bottom, left, right)
tkinter.Label(win, image=img, compound='bottom', text='联想新系列-ThinkPad', font='楷体 20 bold italic').pack()
win.mainloop()

# Label组件中可以用'\n'进行文字换行，也可以用wraplength进行指定位置的换行(单位是像素，当文本到达指定的宽度时就自动换行)


# Entry 单行文本框组件 ---- 用于添加单行文本框 少量文字

# Entry组件中的三个方法：
# get() 获取文本框组件中内容
# insert() 插入文本框组件中内容，参数index为添加的位置 开头为0
# delete() 删除文本框组件中内容 参数first end (前闭后开) ----如果要删除所有内容，可以用delete(0, 'end')

win2 = tkinter.Tk()
entry1 = tkinter.Entry(win2)
entry2 = tkinter.Entry(win2, show='*') # 参数show可以将输入的内容隐藏

def private_notify():
    txt = entry1.get()
    txt2 = entry2.get()
    print('你的账户号码为：' + txt)
    print('你的账户密码为：' + txt2)

def back1():
    length1 = len(entry1.get())
    entry1.delete(length1-1, 'end')

def back2():
    length2 = len(entry2.get())
    entry2.delete(length2-1, 'end')

def reset():
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')

tkinter.Label(win2, text='AccountNumber', font=15).grid(pady=10, row=0, column=0)
tkinter.Label(win2, text='Password', font=15).grid(pady=10, row=2, column=0)
entry1.grid(row=0, column=1)
entry2.grid(row=2, column=1)
tkinter.Button(win2, text='显示', command=private_notify).grid(row=3, column=1, columnspan=2)
tkinter.Button(win2, text='回退', command=back1).grid(row=0, column=2, columnspan=2)
tkinter.Button(win2, text='回退', command=back2).grid(row=2, column=2, columnspan=2)
tkinter.Button(win2, text='重置', command=reset).grid(row=3, column=3, columnspan=2)
win2.mainloop()


# Text 多行文本框组件

win3 = tkinter.Tk()
txt = tkinter.Text(win3)
txt.insert(tkinter.INSERT, 'hello world!\n') # 或'insert', 表示在光标处添加文本
img = tkinter.PhotoImage(file=r'C:\Users\Ben\Desktop\learnnovel.png')
txt.image_create(tkinter.END, image=img) # 或'end', 插入图像
txt.pack()
win3.mainloop()

'''
line.column 表示第几行第几列字符位置，如：text.get(1.2, 1.6)表示索引第一行第3个列至第一行第7列字符
+-count charts 表示指定位置向前向后移动count个字符，如：2.1+2 chars表示第2行第4个字符的位置
line.end 表示第line行的最后一个字符位置
注意：第一行的索引为1，第一列的索引为0
'''

win4 = tkinter.Tk()
# search() 搜索文本
# edit_undo() 撤销操作
# edit_separator() 添加分割线，添加后再进行撤销操作就不会撤销所有操作，只是撤销上一次操作
'''
默认情况下(即：参数autoseparators=True)，每一次完整的操作将会放入栈中.
Tkinter 觉得每次焦点切换、用户按下 Enter 键、删除\插入操作的转换等之前的操作算是一次完整的操作，很容易一次的“撤销”操作就会将所有的内容删除
'''
# edit_redo() 恢复之前的操作

text = tkinter.Text(win4, width=50, height=40, undo=True)
text.pack()
def undo1(event): #推测：一般涉及bind方法时就需要在def里传一个形参
    text.edit_undo()
def redo1(event):
    text.edit_redo()
def call_back(event):
    text.edit_separator() # 每敲击一次键盘就添加一个分割线，否则就撤销或恢复所有内容
text.insert(tkinter.INSERT, '在下方可以添加文本，通过键盘<Ctrl+Z>可以撤销操作，<Ctrl+Y>可以恢复操作:\n\n')
text.bind('<Control-Z>', undo1)
text.bind('<Control-Y>', redo1)
text.bind('<Key>', call_back)
win4.mainloop()


# Spinbox输入选择组件 ----可以理解为Entry组件的变体，可以从多个固定值(汉字、数字)中选取一个

win5 = tkinter.Tk()

# Spinbox(win, from_=n1, to=n2) from_为数值的下限，to为数值的上限;  因为是数字本身，所以是整数
# Spinbox(win, values=('apple', 'banana', 'peach'0))

# 参数
# increment 单击箭头时，Spinbox递增或递减的数值
# readonlybackground Spinbox处于readonly状态时的背景颜色
# state 设置Spinbox组件的状态，可选的值有 normal默认，disabled完全禁止，readonly只读(可以被选中和复制)

win5.title('购买道具')
tkinter.Label(win5, text='购买道具：').grid(row=0, column=0, pady=10)
tkinter.Label(win5, text='购买数量：').grid(row=1, column=0, pady=10)
money = 5 # 因为此处的默认值是绿宝石对应的价格
def typ():
    global money
    if treasure.get() == '红宝石':
        money = 10
    elif treasure.get() == '绿宝石':
        money = 5
    elif treasure.get() == '蓝宝石':
        money = 8
    elif treasure.get() == '黄宝石':
        money = 20
    elif treasure.get() == '无限手套':
        money = 25
    elif treasure.get() == '宇宙魔方':
        money = 23
    calculate()

def calculate():
    vol = int(volume.get())
    ttprice = vol * money
    textshown = '选购'+ treasure.get() + '总价 ' + str(ttprice) + ' 金币'
    lbtxt.configure(text=textshown)

treasure = tkinter.Spinbox(win5, values=('绿宝石', '红宝石', '蓝宝石', '黄宝石', '无限手套', '宇宙魔方'), command=typ, state='readonly') # tuple里的第一个值是默认值
treasure.grid(row=0, column=1, pady=10)
volume = tkinter.Spinbox(win5, from_=0, to=100, increment=10, command=calculate)
volume.grid(row=1, column=1, pady=10)
lbtxt = tkinter.Label(win5)
lbtxt.grid(row=3, column=0, columnspan=3, pady=10)
win5.mainloop()


# Scale 规定数值范围组件 ----以滑块的形式规定数值范围，用户通过拖动滑块选择数值
win6 = tkinter.Tk()
# Scale(win, from_=0, to=50, resolution=1, orient='horizontal')
# resolution=1表示每次滑块增加/减少1； orient='horizontal'表示滑块水平显示

# 参数
# activebackground 鼠标悬停在滑块上时，尺度条的背景颜色
# digits 尺度数值，即尺度条的数字的数字位数（计数时包含"."）
# command 当scale的数值变化时，执行某函数
# ...

# set(value) 设置scale组件的值
# get() 获得当前滑块的值

def typee(self):
    number = str(slide.get())
    print('实时播报：当前数值为 '+ number + ' ！')

slide = tkinter.Scale(win6, from_=-10, to=10, resolution=2, orient=tkinter.HORIZONTAL, width=40, length=600, command=typee)
slide.pack()
win6.mainloop()

# coding=gbk

import tkinter


# 第六章 按钮类组件



# Button组件

win1 = tkinter.Tk()
win1.title('二进制密码小键盘')

def num(a):
    val = psw.get()
    if len(val) < 6:
        psw.delete(0, 'end')
        psw.insert(0, val + a)
def back():
    val = psw.get()
    if len(val) > 0:
        psw.delete(len(val)-1, 'end') #删除最后一位
def check():
    val = psw.get()
    win = tkinter.Toplevel()
    if len(val) == 5:
        tkinter.Label(win, text='密码正确').pack()
    else:
        tkinter.Label(win, text='密码错误').pack()
        psw.delete(0, tkinter.END)


psw = tkinter.Entry(win1, relief='groove', justify='center')
btn1 = tkinter.Button(win1, text='0', command=lambda :num('0'))
btn2 = tkinter.Button(win1, text='1', command=lambda :num('1'))
btn3 = tkinter.Button(win1, text='←', command=back)
btn4 = tkinter.Button(win1, text='OK', command=check)
psw.grid(row=0, column=0, columnspan=4) 
btn1.grid(row=1, column=0, columnspan=2)
btn2.grid(row=1, column=3, columnspan=2)
btn3.grid(row=2, column=0, columnspan=2)
btn4.grid(row=2, column=3, columnspan=2)
win1.mainloop()


# Radiobutton单选按钮组件 ---- 实现单选

win2 = tkinter.Tk()

def result1():
    if v.get() == 1:
        re.config(text='答错了，答案是 小狗， 因为旺旺仙贝！')
    else:
        re.config(text='答对了！因为 旺旺仙贝！')

win2.title('脑筋急转弯')
win2.geometry('300x150')
text = tkinter.Label(win2, text='老师让小猫和小狗去背书，请问谁先背书呢？').pack(anchor='w')
v = tkinter.IntVar() # 可以视作tkinter内置的编程类型，直接用于绑定相应的组件，从而更好的操作组件的值
ans1 = tkinter.Radiobutton(win2, text='小猫', variable=v, value=1, selectcolor='white')
ans1.pack(anchor='w')
ans2 = tkinter.Radiobutton(win2, text='小狗', variable=v, value=2, selectcolor='white')
ans2.pack(anchor='w')
btn = tkinter.Button(win2, text='提交', bg='pink', relief='groove', command=result1).pack()
re = tkinter.Label(win2)
re.pack()
win2.mainloop()



# Checkbutton 复选框组件

# 在一组checkbutton复选框中，用户可以选中多个选项
# 判断复选框是否被选中，实际上判断的是为复选框绑定的变量的值；如果绑定的变量类型为整型，则为01；如果为布尔类型，则为truefalse

win5 = tkinter.Tk()
win5.title('调查问卷')

str1 = ['旅游', '追剧', '聚餐', '健身', '做爱']
text = tkinter.Label(win5, text='选出下方自己喜欢的放松方式：', font='14').grid(row=0, column=0, columnspan=6)
check = []

def result1():
    selection = ''
    for i in range(len(str1)):
        # if check[i].get() == 1:
        if check[i].get():
            selection += (str1[i] + ' ')
    re.config(text=selection)

for i in range(len(str1)):
    # v = tkinter.IntVar()
    v = tkinter.BooleanVar()
    checkbox = tkinter.Checkbutton(win5, text=str1[i], variable=v, font='12', selectcolor='#00ffff', padx=5)
    checkbox.grid(row=1, column=i)
    check.append(v)
button = tkinter.Button(win5, text='提交', command=result1, font='14', bg='pink').grid(row=3, column=0, pady=6, columnspan=6)
re = tkinter.Label(win5, font='12', height='5', width='50', bg='grey')
re.grid(row=4, columnspan=5)
win5.mainloop()

# coding=gbk

import tkinter

# 第七章 选择列表与滚动条



# Listbox列表框组件

# 参数
# listvariable 指向一个StringVar变量，用于存放Listbox组件所有项目
# selectmode 选择模式，值可以是 single单选、browse单选且可以拖动鼠标或使用方向键改变选项、multiple多选、extended多选且可以通过shift/control/拖动鼠标实现多选
# takefocus 指定列表框是否可以通过tab键转移焦点
# xscrollcommand/yscrollcommand 为列表添加水平/垂直滚动条

# 方法
# insert、delete、selection_set、selection_get、size、selection_includes

def show(ele):
    listbox.pack(fill='x')
def typeIn(event):
    enc.delete(0, 'end')
    enc.insert('insert', listbox.get(listbox.curselection()))

win1 = tkinter.Tk()
win1.title('Listbox的初级应用')
win1.geometry('180x150')
val = tkinter.StringVar()
val.set('重庆 北京 天津 上海 广州 深圳')
listbox = tkinter.Listbox(win1, bg='yellow', selectbackground='blue', selectmode='browse', height=6, width=25, listvariable=val)
enc = tkinter.Entry(win1)
enc.pack(fill=tkinter.X)
enc.bind('<Button-1>', show)
listbox.bind('<Double-Button-1>', typeIn)
win1.mainloop()


def gettext(event):
    str= ''
    index1 = fruits.curselection() # 获取选中的项的INDEX
    print(index1)
    for i in index1:
        i = fruits.get(i)
        str += i
        str += '、'
    label.config(text='你选择了 ' + str)

win2 = tkinter.Tk()
win2.title('水果菜单')
win2.geometry('240x240')
label = tkinter.Label(win2, height=5, wraplength=190, justify='left', bg='yellow', relief='groove')
label.pack(side='top', fill='x', padx='10', pady='10')
scr1 = tkinter.Scrollbar(win2)
fruitlist = ['苹果', '香蕉', '火龙果', '西瓜', '猕猴桃', '牛油果', '樱桃', '生梨', '山竹']
fruits = tkinter.Listbox(win2, height=7, yscrollcommand=scr1.set, selectmode='multiple', justify='center', width=30)
for i in fruitlist:
    fruits.insert('end', i)
fruits.pack(side='left', fill='x')
fruits.bind('<<ListboxSelect>>', gettext)
scr1.pack(side='left', fill='y')
scr1.config(command=fruits.yview)
win2.mainloop()


# OptionMenu 下拉列表组件 ----就是下拉单选的效果

# Combobox 组合框组件 ----是ttk模块的组件，相当于Entry组件和OptionMenu组件的组合，用户既可以在文本框中输入组合，也可以单击文本框右侧的按钮展开下拉菜单
import tkinter.ttk

# Combobox常用的三个方法：
# get 获取当前被选中的选项
# set(value) 设置当前选中的值为value
# current(index) 设置默认选中索引为index的选项

def getMon(event):
    items = monOption.get()
    if items in ['4', '6', '9', '11']:
        b = tuple(range(1, 31))
    elif items == '2':
        b = tuple(range(1, 29))
    else:
        b = tuple(range(1, 32))
    dateOption['values'] = b
def getDate():
    info = label3.cget('text') # 获取label里的文字
    temp = monOption.get() + '月' + dateOption.get() + '日：\t' + text.get('0.0', 'end') 
    label3.config(text=info+temp)
    text.delete('0.0', 'end')
win3 = tkinter.Tk()
win3.title('添加日程')
number = tkinter.StringVar()
a = tuple(range(1, 13)) # 月份
monOption = tkinter.ttk.Combobox(win3, width=5, textvariable=number, values=a)
monOption.current(0) # 设定默认值为1月
monOption.grid(row=1, column=0, sticky='w', columnspan=2)
monOption.bind('<<ComboboxSelected>>', getMon)
label1 = tkinter.Label(win3, text='月').grid(row=1, column=2, sticky='w')
b = tuple(range(1, 32)) # 天
dateOption = tkinter.ttk.Combobox(win3, width=5, values=b)
dateOption.grid(row=1, column=3, pady=10, columnspan=2)
dateOption.current(0) # 设定默认值为1号
label2 = tkinter.Label(win3, text='日').grid(row=1, column=5, sticky='w')
text = tkinter.Text(win3, width=40, height=10)
text.grid(row=2, columnspan=8)
button = tkinter.Button(win3, text='确定', command=getDate)
button.grid(row=3, columnspan=8)
label3 = tkinter.Label(win3)
label3.grid(row=4, columnspan=8)
win3.mainloop()

# coding=gbk

import tkinter

# 第八章 容器组件



# Frame组件 ----如果窗口中的组件比较多，管理起来就会比较麻烦，这是就可以使用Frame容器组件将组件分类管理


def rst_test():
    if val.get() == 3:
        print('答对了！')
    else:
        print('你小学没毕业？')
win1 = tkinter.Tk()
win1.geometry('360x120')
box = tkinter.Frame(width=100, height=100, relief='groove', borderwidth=5) #定义容器组件
box.grid(row=0, column=0, pady=10, padx=10) #布局容器组件
txt = '白日依山尽，黄河入_流'
tkinter.Label(box, text=txt, wraplength=320, justify='left', font='14').grid(columnspan=4)
select = ['河', '江', '湖', '海']
val = tkinter.IntVar() # 将这一组单选按钮的值绑定val变量
for i in range(len(select)):
    # 添加单选按钮，并且定义父容器为box
    tkinter.Radiobutton(box, text=select[i], value=i, variable=val, command=rst_test).grid(row=1, column=i)
    # variable = val 是让该组件的数据源类型和intvar绑定
    # value = i 是定义这个组件对于的具体的值
win1.mainloop()

win2 = tkinter.Tk()
def all():
    for index, item in enumerate(checkbox):
        item.set(True)
def none():
    for index, item in enumerate(checkbox):
        item.set(False)
def inverse():
    for index, item in enumerate(checkbox):
        if item.get() == False:
            item.set(True)
        else:
            item.set(False)
frame1 = tkinter.Frame(win2, width=200, height=50)
frame1.grid(row=0, column=0)
frame2 = tkinter.Frame()
frame2.grid(row=1, column=0)
val = tkinter.IntVar()
val.set(200) #默认“重置”
radio1 = tkinter.Radiobutton(frame1, value=0, variable=val, text='全选', command=all)
radio2 = tkinter.Radiobutton(frame1, value=100, variable=val, text='重置', command=none)
radio3 = tkinter.Radiobutton(frame1, value=200, variable=val, text='反选', command=inverse)
radio1.grid(row=0, column=0)
radio2.grid(row=0, column=1)
radio3.grid(row=0, column=2)
fruits = ['苹果', '香蕉', '西瓜', '椰子']
checkbox = []
for index, item in enumerate(fruits):
    str = tkinter.BooleanVar()
    str.set(False) # 默认不选
    tkinter.Checkbutton(frame2, text=item, variable=str).grid(row=index+1, column=1)
    checkbox.append(str)

win2.mainloop()


# LabelFrame标签框架组件 ----可以将一系列关联的组件放在一个容器内，可以绘制边框将子组件包围，并为其展示一个标题


# Toplevel 顶层窗口组件
# 可以弹出一个新窗口，他是显示在父窗口的上层；当父窗口被关闭时，Toplevel窗口也会被关闭，但是Toplevel窗口的关闭并不影响父窗口

def create():
    top = tkinter.Toplevel()
    top.geometry('150x150')
    top.title('创建顶层窗口')
    top.configure(bg='grey')
    tkinter.Label(top, text='这是Toplevel组件窗口').pack()

win3 = tkinter.Tk()
win3.geometry('200x200')
win3.config(bg='pink')
tkinter.Button(win3, text='创建顶层窗口', command=create).pack()
win3.mainloop()


# PaneWindow 窗口布局管理组件
# 可以将自身划分为多个模块，然后将组件放置在不同的子模块内，用户不仅可以设置子模块的排列方式，还可以手动调整各子模块占据空间的大小


# Notebook 选项卡组件 ----是ttk模块提供的组件，可以显示多个选项；当用户单机选项时，下面的面板就会显示对应的内容
import tkinter.ttk
def test1():
    if ans1.get() == '低头思故乡':
        fb = tkinter.Toplevel()
        tkinter.Label(fb, bg='green', text='恭喜你答对了！').pack()
    else:
        fb = tkinter.Toplevel()
        tkinter.Label(fb, bg='green', text='小学没毕业？').pack()
def test2():
    if ans2.get() == '守四方':
        fb = tkinter.Toplevel()
        tkinter.Label(fb, bg='pink', text='恭喜你答对了！').pack()
    else:
        fb = tkinter.Toplevel()
        tkinter.Label(fb, bg='pink', text='小学没毕业？').pack()
win4 = tkinter.Tk()
note = tkinter.ttk.Notebook(win4, width=300, height=400)
pane1 = tkinter.Frame()
label1 = tkinter.Label(pane1, text='举头望明月')
label1.grid(row=0, column=0)
ans1 = tkinter.Entry(pane1)
ans1.grid(row=1, column=0)
button1 = tkinter.Button(pane1, text='交卷', command=test1)
button1.grid(row=2, column=0)
pane2 = tkinter.Frame()
label2 = tkinter.Label(pane2, text='安得猛士兮')
label2.grid(row=0, column=0)
ans2 = tkinter.Entry(pane2)
ans2.grid(row=1, column=0)
button2 = tkinter.Button(pane2, text='交卷', command=test2)
button2.grid(row=2, column=0)
note.add(pane1, text='第一关') # 通过add方法将子组件添加到Notebook组件中；运行时，单击选项卡标题即可显示对应的子组件
note.add(pane2, text='第二关')
note.pack()
win4.mainloop()

# coding=gbk

import tkinter

# 第九章 消息组件与对话框



# Message组件 ----和Label组件类似

# messagebox 会话框模块 ----该模块会根据会话窗口的应用场合，提供了8种会话框
'''
showinfo() 显示消息提醒
showwarning() 显示警告信息
showerror() 显示错误信息
askokcancel() 显示“确定“或”取消“，若用户选择”确定“则返回True，若选择”取消“则返回False
askyesno() 显示“是“或”否“，若用户选择”是“则返回True，若选择”否“则返回False
askyesnocancel() 显示“是“或”否“或”取消“，若用户选择”是“则返回True，若选择”否“则返回False，若选择”取消“则返回None
askretrycancel() 显示“重试“或”取消“，若用户选择”重试“则返回True，若选择”取消“则返回False
'''
import tkinter.messagebox
def mess():
    boo = tkinter.messagebox.askyesnocancel(title='退出提醒', message='您正在退出程序，点击“是”即可退出程序，点击“否”可以后台运行程序，点击“取消则关闭此会话框”')
    if boo:
        win1.quit()
    elif boo == False:
        win1.iconify() #子窗口被关闭 且 母窗口被最小化
    # else就是点击“取消”，效果和点击x一样

win1 = tkinter.Tk()
win1.title('退出会话框')
tkinter.Button(win1, text='退出程序', command=mess).pack(padx=20, pady=20)
win1.mainloop()

# coding=gbk

import tkinter
import tkinter.ttk

# 第十章 菜单组件


# Menu菜单组件
win1 = tkinter.Tk()
win1.geometry('300x200')

def max_win(event):
    win1.geometry('700x700')

def normal_win(event):
    win1.geometry('300x200')

def txt():
    global val
    global font_size
    global top
    top = tkinter.Toplevel(win1)
    val = tkinter.StringVar()
    val.set('宋体')
    font_list = ('宋体', '黑体', '方正舒体', '楷体', '隶书', '方正姚体')
    family = tkinter.ttk.Combobox(top, textvariable=val, values=font_list)
    family.grid(row=0, column=0)
    font_size = tkinter.Spinbox(top, from_=12, to=30, increment=2, width=10) #字号选择
    font_size.grid(row=0, column=1)
    btn1 = tkinter.Button(top, text='确定', command=font_set)
    btn1.grid(row=1, column=1)

def font_set(): #用元组来存储font值
    font1 = (val.get(), font_size.get())
    label.config(font=font1)

menu1 = tkinter.Menu(win1) #创建顶级菜单
menu2_1 = tkinter.Menu(menu1) #创建二级菜单
menu2b_1 = tkinter.Menu(menu1) #创建二级菜单b
menu3_1 = tkinter.Menu(menu2_1, tearoff=False) #创建三级菜单
'''
tearoff 设置菜单能否从窗口中分离
tearoffcommand 当菜单被分离时所执行的方法
postcommand 该属性是一个方法，表示当菜单被打开时会调用该函数
'''
menu1.add_cascade(label='窗体', menu=menu2_1) #将创建的二级菜单添加到顶级菜单里并设置显示的顶级菜单文字
menu2_1.add_cascade(label='功能选项', menu=menu3_1) #将创建的三级菜单添加到二级菜单里并设置显示的顶二级菜单文字
menu2_1.add_command(label='退出')
menu3_1.add_command(label='最大化', accelerator='Ctrl+Up', command=lambda :max_win('anything')) #accelerator参数相当于解释备注
win1.bind_all('<Control-Up>', max_win)
menu3_1.add_command(label='中等窗口', accelerator='Ctrl+Down', command=lambda :normal_win('anything'))
win1.bind_all('<Control-Down>', normal_win)
menu3_1.add_command(label='最小化')

menu1.add_cascade(label='自定义', menu=menu2b_1) #将创建的二级菜单添加到顶级菜单里并设置显示的顶级菜单文字
menu2b_1.add_cascade(label='字体设置', command=txt) #将创建的三级菜单添加到二级菜单里并设置显示的顶二级菜单文字

label = tkinter.Label(win1, text='这是一个窗口')
label.grid(row=0, column=0)

win1.config(menu=menu1) #显示菜单
win1.mainloop()


# Treeview树形菜单组件 ----是ttk模块的组件之一，它集树状结构和表格于一体，用户可以使用该组件设计表格或树形菜单，且设置树形菜单时可以折叠或展开子菜单

#参数
'''
columns 其值为列表(不是python里的列表)，列表的每一个元素代表一个列表标识符名称，列表的长度就是列的长度；用元组/列表表示
displaycolumns 设置列表是否显示以及显示顺序，可以用"#all"表示 全部显示
height 表格中可以显示几行数据
padding 标题栏内容距离组件边缘的间距
selectmode 定义选择行的方式，“expand”表示可以通过 ctrl+鼠标 选择多行，“browse”表示只能选择一行，“none”表示不能改变选择
show 表示显示哪些列。 tree heading显示所有列，tree显示第一列(即 图标列)，headings显示除第一列以外的其他列
'''

win2 = tkinter.Tk()
tree = tkinter.ttk.Treeview(win2, columns=('name', 'type', 'size', 'ability'), show='tree headings', displaycolumns=(1,0,2,3))
tree.heading('name', text='名称', anchor='center')
tree.heading('type', text='类别', anchor='center')
tree.heading('size', text='大小', anchor='center')
tree.heading('ability', text='熟练度', anchor='center')
tree.heading('#0',text='图标列') #设置图标列的标题； 第一列#0表示图标列永远存在，其不会参与displaycolumns的索引范围
img1 = tkinter.PhotoImage(file=r'C:\Users\Ben\Desktop\war3_hlzz.png')
img2 = tkinter.PhotoImage(file=r'C:\Users\Ben\Desktop\war3_bfwz.png')
img3 = tkinter.PhotoImage(file=r'C:\Users\Ben\Desktop\wq.png')
img4 = tkinter.PhotoImage(file=r'C:\Users\Ben\Desktop\py.png')
tree.insert('', tkinter.END, values=('冰封王座','游戏','200M','熟练'), image=img1, text='war3混乱之治')
tree.insert('', tkinter.END, values=('混乱之治','游戏','150M','熟练'), image=img2, text='war3冰封王座')
tree.insert('', tkinter.END, values=('围棋','棋牌','80M','擅长'), image=img3, text='ZenithGo')
tree.insert('', tkinter.END, values=['编程','学习','250M','喜欢'], image=img4, text='Pycharm')
tree.pack()
win2.mainloop()

# 使用Treeview组件添加子菜单时，需要通过ID绑定父元素
win3 = tkinter.Tk()
tree = tkinter.ttk.Treeview(win3)
tree.heading('#0', text='英雄')
tree.insert('',0,'human', text='人族') #写法1
orc = tree.insert('',1, text='兽族') #写法2
tree.insert('',2,'ne', text='暗夜族')
tree.insert('',3,'ud', text='不死族')
tree.insert('human',0, text='圣骑士')#写法1
tree.insert('human',1, text='大法师')#写法1
tree.insert('human',2, text='山丘之王')#写法1
tree.insert(orc,0,text='剑圣')#写法2
tree.insert(orc,1,text='先知')#写法2
tree.insert(orc,2,text='牛头人酋长')#写法2
tree.insert('ne',0,text='丛林守护者')
tree.insert('ne',1,text='女祭司')
tree.insert('ne',tkinter.END,text='恶魔猎手') # 默认追加在最后一条记录
tree.insert('ne',tkinter.END,text='守望者')
tree.insert('ud',0,text='恐惧魔王')
tree.insert('ud',1,text='死亡骑士')
tree.insert('ud',2,text='巫妖')

tree.pack()
win3.mainloop()

#Treeview组件中提供了三个虚拟事件，
'''
<<TreeviewSelect>> 当选项发生变化时，触发某事件
<<TreeviewOpen>> 当菜单项items的open=True时，触发某事件
<<TreeviewClose>> 当菜单项items的open=False时，触发某事件
'''


def setdat(event):
    # 选择月份后，对应的日期列表发生变化
    temp = monsel.get()
    if temp == 2:
        dat['value'] = tuple(range(1, 29))
    elif temp in [4, 6, 9, 11]:
        dat['value'] = tuple(range(1, 31))
    else:
        dat['value'] = tuple(range(1, 32))

def get1():
    # 添加及修改表格
    if len(entry.get()) == 0:
        return False
    else:
        # 将时间格式调整为两位数
        h = str(horsel.get()) if horsel.get() >= 10 else ('0' + str(horsel.get()))
        m = str(minsel.get()) if minsel.get() >= 10 else ('0' + str(min.get()))
        item1 = (str(mon.get()) + '月' + str(datesel.get()) + '日', h + ':' + m, entry.get())
        if tree.focus() == '':
            # 判断菜单项是否有被选中
            tree.insert('', 'end', values=item1)
        else:
            tree.insert('', tree.index(tree.focus()), values=item1)
        reset1()

def del1():
    # 单击删除时，删除获取焦点的菜单
    if tree.focus() == '':
        return False
    else:
        tree.delete((tree.focus()))

def edt(event):
    # 实现双击菜单中某行，修改该行中的内容的功能
    temp = tree.set(tree.focus())
    print(temp)
    d = temp['date'].split('月')
    t = temp['time'].split(':')
    monsel.set(int(d[0]))
    datesel.set(int(d[1].split('日')[0]))
    horsel.set(int(t[0]))
    minsel.set(int(t[1]))
    entry.delete(0, tkinter.END)
    entry.insert(tkinter.INSERT, temp['depart'])

def reset1():
    monsel.set(1)
    datesel.set(1)
    horsel.set(0)
    minsel.set(0)
    entry.delete(0, tkinter.END)

win4 = tkinter.Tk()
frame = tkinter.Frame()
frame.grid()
tkinter.Label(frame, text='日期：').grid(row=0, column=0)
monsel = tkinter.IntVar() #定义月份选项的类型
monsel.set(1) #默认为一月
mon = tkinter.ttk.Combobox(frame, values=tuple(range(1,13)), textvariable=monsel, width=5) #月 下拉框
mon.grid(row=0, column=1)
mon.bind('<<ComboboxSelected>>', func=setdat) # 月份发生变化时，对应的日期也应该发生变化
tkinter.Label(frame, text='-').grid(row=0, column=2)
datesel = tkinter.IntVar() #定义日期选项的类型
datesel.set(1) #默认为一号
dat = tkinter.ttk.Combobox(frame, values=tuple(range(1,32)), textvariable=datesel, width=5) #日下拉框
dat.grid(row=0, column=3)
tkinter.Label(frame, text='时间：').grid(row=0, column=4, columnspan=2)
horsel = tkinter.IntVar() #定义小时选项的类型
horsel.set(0) #默认为零时
hor = tkinter.Spinbox(frame, from_=0, to=24, width=5, textvariable=horsel) #小时选项卡
hor.grid(row=0, column=6)
tkinter.Label(frame, text=':').grid(row=0, column=7)
minsel = tkinter.IntVar() #定义分钟选项的类型
minsel.set(0) #默认为零分
min = tkinter.Spinbox(frame, from_=0, to=59, width=5, textvariable=minsel) #分钟选项卡
min.grid(row=0, column=8)
tkinter.Label(frame, text='出发地：').grid(row=0, column=9)
entry = tkinter.Entry(frame)
entry.grid(row=0, column=10)
tkinter.Button(frame, text='确定', command=get1).grid(row=0, column=11)
tkinter.Button(frame, text='删除', command=del1).grid(row=0, column=12)

tree = tkinter.ttk.Treeview(win4, columns=['date', 'time', 'depart'], show='headings')
tree.heading('date', text='日期')
tree.heading('time', text='时间')
tree.heading('depart', text='出发地')
tree.grid(row=1, column=0)
tree.bind('<<TreeviewSelect>>', edt) #当选项发生变化时 调用edt函数


win4.mainloop()

# coding=gbk

import tkinter
import tkinter.ttk
import time
# 第十一章 进度条组件


# Progressbar进度条组件 ----是ttk模块中的组件，用于显示当前任务的执行进度

#参数
'''
orient 设置进度条 水平显示 或 垂直显示，可选的值有 horizontal/vertical
length 指定进度条的长度
mode 进度条加载动画的模式，可选的值有 determinate(默认值，指针从七点移动到终点后，再从起点开始移动)、indeterminate(指针在起点与终点间来回滚动)
maximum 指定进度条的最大值，默认为100
value 进度条的当前值
variable 为进度条的值绑定一个变量，当变量的值发生变化时，进度条值也会发生变化
'''
val = 0
def add(num):
    global val
    val +=num
    if val > pro['maximum']:
        txtrp.config(text='你妈的，老子吃饱了！')
    else:
        vari.set(val)
        txtrp.config(text='饿死老子了！', foreground='green')

win1 = tkinter.Tk()
win1.geometry('220x190')
tkinter.Label(win1, text='投食：').grid(row=0, column=0, columnspan=1)
tkinter.Button(win1, text='小鱼', command=lambda : add(1)).grid(row=0, column=1, pady=10)
tkinter.Button(win1, text='大鱼', command=lambda : add(2)).grid(row=0, column=2, pady=10)
img = tkinter.PhotoImage(file=r'C:\Users\Ben\Desktop\pet.png')
txtrp = tkinter.Label(win1, image=img, compound='top', foreground='red')
txtrp.grid(row=1, column=0, columnspan=4)
vari = tkinter.IntVar()
vari.set(0)
pro = tkinter.ttk.Progressbar(win1, mode='determinate', variable=vari, maximum=50, length=200)
pro.grid(row=2, column=0, columnspan=4, pady=5)
win1.mainloop()

# Progressbar进度条组件主要提供了三个方法
'''
start(interval=None) 开始自动递增模式，每隔internal时间，就调用一次step(amount=None)方法；interval的默认值为50毫秒
step(amount=None) 设置进度条递增的步进值，默认值的amount为1.0
stop() 停止start(interval)的运行
'''

win2 = tkinter.Tk()
win2.title('灵魂画师')
def rego():
    pro.step(50)
    print(pro['value'])
    go()

def go():
    print('开吃！')
    pro.start()

def record():
    q = pro['value']
    print(q)
    if q >= 150:
        pro.stop()
        print('吃饱了')
    else:
        win2.after(1000, record)

img = tkinter.PhotoImage(file=r'C:\Users\Ben\Desktop\pet.png')
label = tkinter.Label(win2, image=img, text='吃小朋友', fg='red', font=('华文新魏', 19), compound='bottom')
label.grid(row=1, column=0, columnspan=3)
pro = tkinter.ttk.Progressbar(win2, mode='determinate', value=0, maximum=200, length=100)
pro.grid(row=2, column=0, columnspan=3, pady=10)
tkinter.Button(win2, text='开始喂小朋友', command=go, width=17).grid(row=4, column=0, padx=5)
tkinter.Button(win2, text='投喂加速', command=rego, width=7).grid(row=4, column=1, padx=5)
tkinter.Button(win2, text='停止投喂', command=pro.stop, width=7).grid(row=4, column=2, padx=5)
win2.after(1000, record)
'''
tkinter窗口，比如root窗口，以及Toplevel窗口，都有一个after方法。此方法执行后，将会在规定的时间间隔之后，执行一个特定的您指定的函数。
如果在您指定的这个定时执行的函数中，再次调用after方法，就可以起到一个定时器的效果。其实，python中简单的定时器基本都是这个思路。
它相当于不会堵塞进程的sleep
'''
win2.mainloop()

# coding=gbk

import tkinter
import tkinter.ttk
import time
# 第十二章 Canvas绘图


# Canvas组件是tkinter模块中的组件，主要用途是绘制图形，文字，设计动画，也可以将其他的小部件放置在画布上

'''
绘制线条
canvas.create_line(x1, y1, x2, y2, ...., xn, yn, option)
里面的xy依次为直线的起点、第二个顶点、...终点; option为线条的可选参数
'''

'''
绘制矩形
canvas.create_rectangle(x1, y1, x2, y2, option)
里面的x1y1是矩形的左上角定点，x2y2是矩形的右下角定点
'''
win1 = tkinter.Tk()
win1.title('键盘控制矩形移动')
win1.geometry('300x200')
def up1(event):
    canvas.move(rect, 0, -2) #注意别写反了，这里可以理解成距离左上角的距离缩小
def left1(event):
    canvas.move(rect, -2, 0)
def down1(event):
    canvas.move(rect, 0, 2)
def right1(event):
    canvas.move(rect, 2, 0)

canvas = tkinter.Canvas(win1, width=200, height=200, relief='solid')
rect = canvas.create_rectangle(10, 10, 50, 50, fill='#C8F7F2')
canvas.pack()
win1.bind('<Up>', up1)
win1.bind('<Down>', down1)
win1.bind('<Right>', right1)
win1.bind('<Left>', left1)
win1.mainloop()

'''
绘制椭圆
create_oval(x1, y1, x2, y2, option)
里面的x1y1为椭圆的左上角坐标，x2y2为椭圆的右下角坐标
'''

'''
绘制圆弧和扇形
create_arc(x1, y1, x2, y2, extent=-180, style=ARC, option)
里面的x1y1为圆弧的起点坐标，x2y2为圆弧的终点坐标；extent表示圆弧的角度，style表示绘制的类型，有ARC, CHORD, PIESLICE
'''

'''
绘制多边形
create_polygon(x1, y1, x2, y2, xn, yn, option)
其中的x1y1, x2y2, xnyn, 为顺时针方向或逆时针方向依次描绘的多边形的顶点；option为绘制多边形的相关参数
'''

'''
绘制文字
create_text(x, y, text=str, option)
其中的xy为字符串的中心位置，text为输出的字符串，option为文字的相关属性
'''

'''
绘制图像
create_image(x, y, image, option)
其中的xy为图像左上角顶点坐标，image为添加的图像
'''
from tkinter.messagebox import *
win2 = tkinter.Tk()
win2.title('Help the bird back home')
win2.geometry('400x320')
def draw(event):
    canvas.coords(bird, event.x, event.y)
def backhome(event):
    canvas.coords(bird, event.x, event.y)
    x1 = abs(event.x-340)
    y1 = abs(event.y-70)
    if x1<70 and y1<75:
        showinfo('我爱你', '你妈的，老子终于回家了！')
canvas = tkinter.Canvas(win2, width=400, height=320, relief='solid', bg='pink')
bird1 = tkinter.PhotoImage(file=r'C:\Users\Ben\Desktop\pet.png')
house1 = tkinter.PhotoImage(file=r'C:\Users\Ben\Desktop\home.png')
house = canvas.create_image(340 ,70, image=house1)
bird = canvas.create_image(150 ,250, image=bird1)
canvas.grid(row=0, column=0, columnspan=2)
canvas.bind('<B1-Motion>', draw)
canvas.bind('<ButtonRelease-1>', backhome)
win2.mainloop()


win3 = tkinter.Tk()
win3.title('书法秀')
win3.geometry('420x420')
canvas = tkinter.Canvas(win3, width=400, height=400, bg='green', relief='solid')
def draw(event):
    global text1
    text1 = canvas.create_oval(event.x, event.y, event.x+10, event.y+10, fill='blue', outline='')
def delete1():
    canvas.delete('all')
    can()
def can():
    rect = canvas.create_rectangle(4, 4, 400, 385, outline='red', width=2)
    line1 = canvas.create_line(2, 198, 400, 198, dash=(2,2), fill='red')
    line2 = canvas.create_line(198, 2, 198, 400, dash=(2,2), fill='red')
    line3 = canvas.create_line(0, 0, 400, 400, dash=(2,2), fill='red')
    line4 = canvas.create_line(0, 400, 400, 0, dash=(2,2), fill='red')
    canvas.pack(side='bottom')
    canvas.bind('<B1-Motion>', draw)
tkinter.Button(win3, text='重置', command=delete1).pack(side='bottom')
can()
win3.mainloop()

'''
canvas组件还可以涉及动画，主要通过移动或改变canvas组件中元素的坐标来实现，
move(sth, x, y) 将sth水平方向向右移动x单位长度，垂直向下移动y单位长度
coords(sth, (x, y)) 相当于重置sth坐标

每当元素的坐标改变，需要强制刷新窗口中的内容，用update()
'''

# coding=gbk

import tkinter
import tkinter.ttk
import time
# 第十三章 鼠标键盘事件处理


# 鼠标事件 ----tkinter模块中定义鼠标事件，通常将事件名称放置在尖括号"<>"中
'''
widget.bind(event, handle)
widget是鼠标事件的来源(e.g. root窗口,窗口中的组件), event是具体的事件, handle是鼠标事件的处理程序

例如 实现鼠标左键单机label组件时，执行click()方法
label.bind('<Button-1>', click)
'''

'''
<Button-1> 单击鼠标左键
<Button-2> 单击鼠标中间键
<Button-3> 单击鼠标右键
<Button-4> 向上滚动滑轮
<Button-5> 向下滚动滑轮
<B1-Motion> 按下鼠标左键并拖动鼠标
<B2-Motion> 按下鼠标中键并拖动鼠标
<B3-Motion> 按下鼠标右键并拖动鼠标
<ButtonRelease-1> 释放鼠标左键
<ButtonRelease-2> 释放鼠标中键
<ButtonRelease-3> 释放鼠标右键
<Double-Button-1> 双击鼠标左键
<Enter> 鼠标进入控件
<Leaver> 鼠标移出控件
'''

# 当事件发生时，鼠标相对组件的位置(即 event.x, event.y)会被存入事件对象event中，所以在绑定的回调函数中 即使不需要鼠标的位置，也应该接受event参数，否则会报错
def show1(event):
    label1.config(text='你麻痹的，滚！')
def hidden1(event):
    label1.config(text='')
win1 = tkinter.Tk()
win1.geometry('420x200')
label1 = tkinter.Label(win1, text='~~~~', font='华文新魏 15', bg='green', fg='red')
label1.pack(pady=30, padx=30)
label1.bind('<Enter>', show1)
label1.bind('<Leave>', hidden1)
win1.mainloop()


#键盘事件

'''
<Return> 按下回车键
<space> 按下空格键
<Key> 按下某键，键值作为event对象参数被传递
<Shift-Up> 同时按住<Shift>和<Up>键
同理...
'''
def prt(e):
    le = len(text.get('0.0', tkinter.END))
    label.config(text=str(le))
win2 = tkinter.Tk()
text = tkinter.Text(win2, width=20, height=5)
text.pack()
label=tkinter.Label(win2)
label.pack()
text.bind('<Key>', prt)
win2.mainloop()

# 贪吃蛇
win3 = tkinter.Tk()

# 为避免重复代码，通过xx(module), yy(module)方法获取指定组件module的当前位置
def xx(module):
    return int(module.winfo_geometry().split('+')[1])

def yy(module):
    return int(module.winfo_geometry().split('+')[2])

def up1(event):
    for index, ch in enumerate(snake):
        ind = len(snake) - index - 1
        if ind == 0:
            snake[ind].place(x=xx(snake[ind]), y=yy(snake[ind]) - step)
        else:
            snake[ind].place(x=xx(snake[ind-1]), y=yy(snake[ind-1]))

def down1(event):
    for index, ch in enumerate(snake):
        ind = len(snake) - index - 1
        if ind == 0:
            snake[ind].place(x=xx(snake[ind]), y=yy(snake[ind]) + step)
        else:
            snake[ind].place(x=xx(snake[ind-1]), y=yy(snake[ind-1]))

def left1(event):
    for index, ch in enumerate(snake):
        ind = len(snake) - index - 1
        if ind == 0:
            snake[ind].place(x=xx(snake[ind]) - step, y=yy(snake[ind]))
        else:
            snake[ind].place(x=xx(snake[ind-1]), y=yy(snake[ind-1]))

def right1(event):
    for index, ch in enumerate(snake):
        ind = len(snake) - index - 1
        if ind == 0:
            snake[ind].place(x=xx(snake[ind]) + step, y=yy(snake[ind]))
        else:
            snake[ind].place(x=xx(snake[ind-1]), y=yy(snake[ind-1]))


w = 10 #蛇身体由小正方形组成，w为正方形的边长
x1 = 0 #蛇头的初始位置
y1 = 10

num = 15 #初始状态的蛇由5个方块组成
step = 10 #蛇移动的单位距离

snake = []
for i in range(num):
    item1 = tkinter.Frame(width=10, height=10, bg='pink')
    snake.append(item1)
    item1.place(x=x1, y=y1+i*w)
snake[0].config(bg='green')
win3.bind('<Up>', up1)
win3.bind('<Down>', down1)
win3.bind('<Left>', left1)
win3.bind('<Right>', right1)

win3.mainloop()

#一次绑定多个事件处理程序 ---- bind()方法中还有一个可选参数add，其参数值可以为空(默认值)，也可以为+;当为+时，表示将此处理程序添加到此事件类型的函数列表中

#取消事件的绑定 ---- unbind()方法

第十四章-数据库操作 -- skip

# coding=gbk
import shutil
import tkinter
import tkinter.ttk
import time
# 第十五章 文件操作


# python内置的文件以及文件夹操作
# file = open(filename[,mode])
'''
file ----要创建的文件对象
filename ----要创建或打开的文件名称；如果打开的文件和当前文件在同一目录下，那么直接写文件名即可，否则需要指定完整路径
mode ----可选参数，用于指定文件的打开模式，默认是只读(r)

r 文件必须存在。以只读模式打开文件，文件的指针将会放在开头
rb 文件必须存在。以二进制格式打开文件，并且采用只读模式，文件的指针将会放在开头，一般用于非文本文件，如图片音乐
r+ 文件必须存在。打开文件后可以读取文件内容，也可以写入新内容覆盖原有内容(从文件开头进行覆盖)

w 文件如果已经存在则将其覆盖，否则创建新文件。以只写模式打开文件
wb 文件如果已经存在则将其覆盖，否则创建新文件。以二进制格式打开文件，并且采用只写模式，一般用于非文本文件，如图片音乐
w+ 文件如果已经存在则将其覆盖，否则创建新文件。打开文件后，先清空原有内容，使其变成一个空的文件，对这个空文件有读写权限
wb+ 文件如果已经存在则将其覆盖，否则创建新文件。以二进制格式打开文件，并且采用读写模式，一般用于非文本文件，如图片音乐

a 如果该文件已经存在，文件指针将放在文件的末尾(即 新内容会被写入到已有内容中)，否则创建新文件用于写入。 以追加模式打开一个文件
ab 如果该文件已经存在，文件指针将放在文件的末尾(即 新内容会被写入到已有内容中)，否则创建新文件用于写入。 以二进制格式打开文件，并采用追加模式
a+ 如果该文件已经存在，文件指针将放在文件的末尾(即 新内容会被写入到已有内容中)，否则创建新文件用于写入。 以读写模式打开一个文件
ab+ 如果该文件已经存在，文件指针将放在文件的末尾(即 新内容会被写入到已有内容中)，否则创建新文件用于写入。 以二进制格式打开文件，并采用读写模式
'''

# 在使用open(方法打开文件时，默认采用GBK编码，但是当被打开的文件不是GBK编码时，可能会显示异常。解决方法是在调用open()方法时通过添加encoding='utf-8'参数
# 实现将编码指定为UTF-8)

# 打开文件时使用with语句，可以实现在处理文件时 无论是否显示异常，都能保证with语句执行完毕后关闭已打开的文件

# 除了write()方法，python的文件对象还提供了writelines()方法，可以实现把字符串列表写入文件，但不会添加换行符(想换行的话可以开头加'\n')
# file.read([size])可以读取指定个数的字符，size是可选参数，如果省略则一次性读取所有内容
# 在使用read()方法读取文件时，如果文件很大，一次读取全部内容到内存容易造成内存不足，所以通常采取逐行读取
# readline([size])方法用于每次读取一行数据(调用两次就是每次返回当时当前的行), 也可以填size参数
# readlines() 可以以字符串列表的形式读取全部行，每一个元素为文件的一行内容


# 在执行文件操作时，为了确保能够正常执行，可以使用os.path模块的exists()方法先判断要操作的文件是否存在
# if os.path.exists(文件路径):
#   ....

#复制文件 shutil.copyfile(要复制的源文件路径，复制到的目标文件路径)
#移动(剪切)文件 shutil.move(要复制的源文件路径，复制到的目标文件路径) ----也可以用来重命名文件
#重命名文件 os.rename(要进行重命名的文件路径，命名后的文件路径)
#删除文件 os.remove(文件路径)
#获取文件的基本信息----可以通过os模块的stat方法
'''
os.stat(path)
返回的是一个对象，该对象包含多种属性，访问这些属性可以获取文件的基本信息
'''
import os

def show1():
    a = os.stat(r'C:\Users\Ben\Desktop\adhoc.txt')
    text.insert('insert', '文件大小：' + str(a.st_size) + '字节')
    text.insert('insert', '\n\n文件路径：' + os.path.abspath(r'C:\Users\Ben\Desktop\adhoc.txt'))
    text.insert('insert', '\n\n最后访问时间：' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(a.st_atime)))
    text.insert('insert', '\n\n最后修改时间：' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(a.st_mtime)))

win1 = tkinter.Tk()
tkinter.Button(win1, text='显示信息', command=show1).pack(pady=10)
text = tkinter.Text(win1, font=14, width=60, height=10)
text.pack(padx=10)
win1.mainloop()

#输出当前文件夹路径
# print(os.getcwd()) ----相对路径，即依赖于当前工作文件夹，文件路径就是文件名 (绝对路径是指在使用文件时指定文件的实际路径，不依赖当前的工作文件夹)

#拼接路径 ----为了正确处理不同操作系统的路径分隔符，尽量不要用字符串拼接
# os.path.join(path1,path2,....) ----如果拼接的路径中不包含绝对路径，则最后拼接出来的将是相对路径

#创建文件夹
# os.mkdirs(文件夹路径) ----无论路径中间的文件夹是否存在，都可以正常运行

#复制文件夹 ----在复制文件夹时，如果源文件夹下还有子文件夹，那么就会一起复制过去
#shutil.copytree(fromwhere, towhere)

#移动(剪切)文件夹
#shutil.move(fromwhere, towhere)

#删除文件夹
#os.rmdir(文件夹路径) ----只能删除空文件夹
#shutil.rmtree(文件夹路径) ----也可以删除非空文件夹

#遍历文件夹

# os.walk(top[, topdown][, onerror][, followlinks]) ----对指定文件夹下的全部文件夹(包括子文件夹)及文件全部过一遍
'''
top 用于指定要遍历内容的根文件夹
topdown 指定遍历顺序；默认是True，从上至下 即先根文件夹； False，从下至上 即先最后一级子文件夹
onerror 指定报错的处理方式；默认是忽略，
followlinks 指定在支持的系统上访问由符号链接指向的文件夹

返回值 是包含三个元素的元组生成器对象(dirpath,dirname,filenames)，其中
    dirpath是当前遍历的路径，是一个字符串
    dirnames表示当前路径下包含的子文件夹，是一个列表
    filenames表示当前路径下包含的文件，是一个列表
    
'''
# for i in os.walk(r'C:\Users\Ben\Desktop\本科'):
#     print(i)

#os.listdir(path) ----如果我们只需要指定文件夹根目录下的文件和文件夹，返回的是一个列表
# print(os.listdir(r'C:\Users\Ben\Desktop\本科'))


#tkinter模块中的文件对话框 ----tkinter模块提供了filedialog对话框，用户可以通过它对文件进行操作
from tkinter.filedialog import *

#选择文件 ----双击后是不会打开文件的，但是会返回这个文件的路径；如果想打开需要open
# 如果你是希望界面打开，用os.startfile(r'C:\Program Files (x86)\Counter Strike 1.6\cstrike.exe')
#askopenfilename() 选择一个文件，返回文件名
#askopenfilenames() 选择多个文件，返回文件名列表
win2 = tkinter.Tk()
def a():
    bb = askopenfilename(title='选择文件', filetypes=[('txt格式的文件','*.txt'),('jpg格式的图片','*.jpg')], initialdir=r'C:\Users\Ben\AppData\Local')
    print(bb)
    open(bb,mode='w')
tkinter.Button(win2, text='选择', command=a).pack()
win2.mainloop()

#保存文件
#asksaveasfilename 选择以什么文件名保存，返回文件名
#asksaveasfile 创建并保存文件，返回文件流对象
'''
defaultextension 文件默认的拓展名，如.py
initialdir 初始目录
initialfile 初始文件名，默认为空
'''

#打开文件----你双击仍然不会打开，返回的是文件流对象(集合)，想打开的话仍然要用open； e.g. file = open(b.name, 'r')
win3 = tkinter.Tk()
def b():
    bb = askopenfile(title='选择文件', filetypes=[('txt格式的文件','*.txt'),('jpg格式的图片','*.jpg')])
    print(bb)
tkinter.Button(win3, text='选择', command=b).pack()
win3.mainloop()

#选择文件夹 ----askdirectory() 选择或创建一个文件夹，返回文件夹路径
