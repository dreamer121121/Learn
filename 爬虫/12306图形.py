import time,datetime
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Treeview
from stationsInfo import stations_codes,stations_names
from SearchTicketsAPI import *
from datetime import timedelta,date
#全局变量
K = []
D = []
G = []
Z = []
T = []
ticket=[]

def GetStation(var_from,var_to,number,tree,all,d,k,g,t,z):
      del ticket[:]
      cleanTree(tree)
      from_station=var_from.get().strip()
      to_station=var_to.get().strip()
      date=str(number.get())
      # 调用API爬虫获取车票信息
      ticket_list =ShowTicket(stations_codes[stations_names.index(from_station)], stations_codes[stations_names.index(to_station)], date)
      print(ticket_list)
      i = 0
      for item in ticket_list:
          if re.match(r'^K', item[0]):
              K.append(i)
          if re.match(r'^D', item[0]):
              D.append(i)
          if re.match(r'^G|C', item[0]):
              G.append(i)
          if re.match(r'^Z', item[0]):
              Z.append(i)
          if re.match(r'^T', item[0]):
              T.append(i)
          i = i + 1

      print(D)
      length = len(ticket_list)
      for i in range(length):
          ticket.append(ticket_list[i])

      pos = FilterFun(all,d,k,g,t,z)#返回满足条件的车票信息(以列表形式)
      for i in pos:
          tree.insert('', i, values=ticket_list[i])
 
      children = tree.get_children()
      for num in range(len(children)):
          if (num % 2 == 0):
              tree.item(children[num], tags=["evenLine"])
          else:
              tree.item(children[num], tags=["evenLine2"])
      tree.tag_configure("evenLine", background='#DEF1EC')
      tree.tag_configure("evenLine2", background='#F1EBDE')

def cleanTree(tree):
    for item in tree.get_children():
        tree.delete(item)

def FilterFun(all,d,k,g,t,z):
    temp = []
    if all.get() == '1':
        for i in ticket:
            temp.append(i)
    if d.get() == '1':
        for i in D:
            temp.append(i)
    if k.get() == '1':
        for i in K:
            temp.append(i)
    if z.get() == '1':
        for i in Z:
            temp.append(i)
    if t.get() == '1':
        for i in T:
            temp.append(i)
    if g.get() == '1':
        for i in G:
            temp.append(i)
    if g.get() == '0' and d.get() == '0' and k.get() == '0' and z.get() == '0' and t.get() == '0':
        for i in range(len(ticket)):
            temp.append(i)
    del K[:]
    del D[:]
    del G[:]
    del Z[:]
    del T[:]
    return temp

r''' 
def selectall():
    if all.get() == '1':
        g.set('1')
        d.set('1')
        z.set('1')
        t.set('1')
        k.set('1')
    else:
        g.set('0')
        d.set('0')
        z.set('0')
        t.set('0')
        k.set('0')
    FilterFun2()


def filterG():
    all.set('0')
    FilterFun2()
 
def filterD():
    all.set('0')
    FilterFun2()
 
def filterZ():
    all.set('0')
    FilterFun2()
 
def filterT():
    all.set('0')
    FilterFun2()
 
def filterK():
    all.set('0')
    FilterFun2()
'''

r'''
def FilterFun2():
    cleanTree()
    pos = FilterFun()
 
    for i in pos:
        tree.insert('', i, values=ticket[i])
    children = tree.get_children()
    for num in range(len(children)):
        if (num % 2 == 0):
            tree.item(children[num], tags=["evenLine"])
        else:
            tree.item(children[num], tags=["evenLine2"])
    tree.tag_configure("evenLine", background='#DEF1EC')
    tree.tag_configure("evenLine2", background='#F1EBDE')
'''

def CheckTicketswindow():
    window=Tk()
    window.geometry("1135x600+400+300")
    window.title("火车票查询系统")
    window.iconbitmap("train.ico")
    #Frame框架，将几个组件放在一起
    TopFrame=Frame(window,width=1135,height=150)
    TLFrame=Frame(TopFrame,width=985,height=150)
    TRFrame=Frame(TopFrame,width=150,height=150)
    TLTFrame=Frame(TLFrame,width=985,height=75)
    TLBFrame=Frame(TLFrame,width=985,height=75)

    Label(TLTFrame,text="始发站:",font=("宋体",11)).pack(side=LEFT)

    #StringVar跟踪变量的值的变化，以保证值的变更随时可以显示在界面上
    var_from=StringVar()
    From_s=Entry(TLTFrame,textvariable=var_from,width=14).pack(side=LEFT)
    Label(TLTFrame,text="终点站:",font=("宋体",11),padx=20).pack(side=LEFT)
    var_to=StringVar()
    to_s=Entry(TLTFrame,textvariable=var_to,width=14).pack(side=LEFT)

    #创建一个下拉列表
    Label(TLTFrame,text="出发日期:",font=("宋体",11),padx=20).pack(side=LEFT)
    number=StringVar()
    numberChose=ttk.Combobox(TLTFrame,width=12,textvariable=number)
    values=[]
    #获取今年今月今日
    y=int(time.strftime("%Y",time.localtime()))
    m=int(time.strftime("%m",time.localtime()))
    day=int(time.strftime("%d",time.localtime()))
    i=0
    yy=y
    mm=m
    dd=day
    while i<20:#20天数据
          if m in (1,3,5,7,8,10,12):
                if day+i>31:
                      dd=day+i-31
                      mm=m+1
                      if mm>12:
                        yy=y+1
                        mm-=12
                else: dd=day+i
          elif m in (4,6,9,11):
              if day+i>30:
                  dd=day+i-30
                  mm=m+1
                  if mm>12:
                      yy=y+1
                      mm-=12
              else: dd=day+i
          else:
              if day+i>28:
                  dd=day+i-28
                  mm=m+1
                  if mm>12:
                      yy=y+1
                      mm-=12     #有问题闰年呢？
              else: dd=day+i
          Time='%d-%02d-%02d'%(yy,mm,dd)
          values.append(Time)
          i+=1
    numberChose['values']=tuple(values)
    numberChose.current(0)# 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值
    numberChose.pack(side=LEFT)

    Label(TRFrame, text='查询天数：', font=('宋体', (11)),padx=5).pack(side=LEFT)
    days = StringVar()
    daysEntry = Entry(TRFrame, textvariable=days, width=5).pack(side=LEFT)
    days.set('1')
    Label(TRFrame,text=' ',font=("宋体",(11)),padx=5).pack(side=LEFT)

    search=Button(TRFrame,text='查询余票',width=10,command=lambda:GetStation(var_from,var_to,number,tree,all,d,k,g,t,z),bg='Cyan').pack(side=LEFT)

    TLFrame.pack(side=LEFT)
    TLTFrame.pack(side=TOP)
    TLBFrame.pack(side=BOTTOM)
    TRFrame.pack(side=RIGHT)
    TopFrame.pack(side=TOP,pady=5)

    # 车型选择
    Label(TLBFrame, text='车次类型：', font=('宋体', (11))).pack(side=LEFT)
    all = StringVar()

    g = StringVar()

    d = StringVar()

    z = StringVar()

    t = StringVar()

    k = StringVar()

    Checkbutton(TLBFrame, text = '全部',padx=10,variable = all).pack(side=LEFT)#此处的command可用于二次查找
    Checkbutton(TLBFrame, text = 'G/C-高铁/城际',padx=10,variable = g).pack(side=LEFT)
    Checkbutton(TLBFrame, text = 'D-动车',padx=10,variable = d).pack(side=LEFT)
    Checkbutton(TLBFrame, text = 'Z-直达',padx=10,variable = z).pack(side=LEFT)
    Checkbutton(TLBFrame, text = 'T-特快',padx=10,variable = t).pack(side=LEFT)
    Checkbutton(TLBFrame, text = 'K-快车',padx=10,variable = k).pack(side=LEFT)

    all.set('0')
    d.set('0')
    g.set('0')
    t.set('0')
    k.set('0')
    z.set('0')

    # 车票展示
    ShowFrame = Frame(window, width=780, height=450, bg='pink')
    ShowFrame.pack(side=TOP)


    scrollBar = Scrollbar(ShowFrame)
    scrollBar.pack(side=RIGHT,fill=Y)
    tree = Treeview(ShowFrame,
                    columns=('c0','c1','c2','c3','c4','c5','c6','c7','c8','c9','c10','c11','c12','c13','c14','c15'),
                    show="headings",
                    height=540,
                    yscrollcommand=scrollBar.set)
    tree.column('c0',width=50,anchor='center')
    tree.column('c1',width=100,anchor='center')
    tree.column('c2',width=100,anchor='center')
    tree.column('c3',width=100,anchor='center')
    tree.column('c4',width=50,anchor='center')
    tree.column('c5',width=60,anchor='center')
    tree.column('c6',width=60,anchor='center')
    tree.column('c7',width=60,anchor='center')
    tree.column('c8',width=60,anchor='center')
    tree.column('c9',width=60,anchor='center')
    tree.column('c10',width=60,anchor='center')
    tree.column('c11',width=60,anchor='center')
    tree.column('c12',width=60,anchor='center')
    tree.column('c13',width=60,anchor='center')
    tree.column('c14',width=60,anchor='center')
    tree.column('c15',width=60,anchor='center')
    #显示车次,出发/到达站,出发/到达时间,历时,商务座,一等座,二等座,软卧,动卧,硬卧,硬座,无座
    tree.heading('c0',text='车次')
    tree.heading('c1',text='出发/到达站')
    tree.heading('c2',text='出发/到达时间')
    tree.heading('c3',text='历时')
    tree.heading('c4',text='商务座')
    tree.heading('c5',text='一等座')
    tree.heading('c6',text='二等座')
    tree.heading('c7',text='高级软卧')
    tree.heading('c8',text='软卧')
    tree.heading('c9',text='动卧')
    tree.heading('c10',text='硬卧')
    tree.heading('c11',text='软座')
    tree.heading('c12',text='硬座')
    tree.heading('c13',text='无座')
    tree.heading('c14',text='其他')
    tree.heading('c15',text='备注')
    tree.pack(side=LEFT,fill=BOTH)
    window.mainloop()


def Loginwindow():
    root=Tk()
    root.geometry("300x400+500+500")
    root.title('登录窗口')
    root.config(bg='pink')
    root.resizable(0,0)


#Label插件
    L_little=Label(root,text='欢迎使用火车票查询系统')#内容
    L_little.config(font='黑体 -25 bold',fg='blue',bg='yellow')#样式
    L_little.place(x=150,y=50,anchor="center")#位置
    L_author=Label(root,text='Version1.0')
    L_author.config(font='黑体 -10 bold',bg='pink',fg='green')
    L_author.place(x=300,y=390,anchor='e')
    user_name=Label(root,text='用户名:')
    user_name.config(font='Verdana -15 bold',bg='pink')
    user_name.place(x=100,y=280,anchor='e')
    passworld=Label(root,text='登录密码:')
    passworld.config(font='Verdana -15 bold',bg='pink')
    passworld.place(x=100,y=310,anchor='e')

#text插件
    e=StringVar()
    user_text=Entry(root,width=20)
    user_text.place(x=100,y=280,anchor='w')
    pass_text=Entry(root,width=20)
    pass_text['show']='*'
    pass_text.place(x=100,y=310,anchor='w')


#添加button组件
    B_0=Button(root,text='登 录',command=lambda:Login(user_text,pass_text,root))#传递参数必须使用lambda参数
    B_0.config(font='TimesNewRoman -25 bold',fg='white',bg='gold',width=10)
    B_0.place(x=150,y=375,anchor='center')

#插入图片
    photo=PhotoImage(file=r'.\meixi.gif',width=168,height=150)
    Imagelabel=Label(image=photo,bg='green')
    Imagelabel.place(x=150,y=180,anchor='center')
    root.mainloop()

def Login(user,pass_world,root):
    if  user.get() == '' and pass_world.get() == '':
        root.destroy()
        CheckTicketswindow()

    else:
        messagebox.askokcancel('错误提示', '用户名或者密码错误请重新输入')

if __name__=='__main__':
    Loginwindow()



