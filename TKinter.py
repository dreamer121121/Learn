from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog
#label组件
def ui_process():
    root=Tk()
    root.geometry("300x400+500+500")
    root.title('登录窗口')
    root.config(bg='green')
    root.resizable(0,0)
    

#Label插件
    L_little=Label(root,text='欢迎使用火车票查询系统')#内容
    L_little.config(font='Helvetica -25 bold',fg='blue',bg='yellow')#样式
    L_little.place(x=150,y=50,anchor="center")#位置
    L_author=Label(root,text='作者:xiaotao')
    L_author.config(font='Helvetica -10 bold')
    L_author.place(x=300,y=390,anchor='e')
    user_name=Label(root,text='用户名:')
    user_name.config(font='Verdana -15 bold',bg='green')
    user_name.place(x=100,y=280,anchor='e')
    passworld=Label(root,text='登录密码:')
    passworld.config(font='Verdana -15 bold',bg='green')
    passworld.place(x=100,y=310,anchor='e')
    
#text插件
    e=StringVar()
    user_text=Entry(root,width=20,textvariable = e)
    e.set('初始用户名为：miexi')
    user_text.place(x=100,y=280,anchor='w')
    pass_text=Entry(root,width=20)
    pass_text['show']='*'
    pass_text.place(x=100,y=310,anchor='w')


#添加button组件
    B_0=Button(root,text='登 录',command=lambda:Login(user_text,pass_text,root))
    B_0.config(font='TimesNewRoman -25 bold',fg='black',bg='gold')
    B_0.place(x=100,y=350)
    #B_1=Button(root,text='登录',command=lambda:CreateNew(root))
    #B_1.place(x=200,y=200)

    
#插入图片
    photo=PhotoImage(file=r'C:\Users\jack xia\Desktop\连接公司\ARGUS\meixi.gif',width=168,height=150)
    Imagelabel=Label(image=photo,bg='green')
    Imagelabel.place(x=150,y=180,anchor='center')
    root.mainloop()   
    
#def CreateDialog():
    #world=simpledialog.askstring('登录', '密码', initialvalue = '美熙')
    #print(world)
    
def Login(user,pass_world,root):
    if  user.get() == 'meixi' and pass_world.get() == '123':
        root1=Tk()
        root1.title('火车票信息系统')
        root1.geometry('150x200+550+550')
        root.destroy()
        root1.state('zoomed')
        root1.mailoop()
    else:
        messagebox.askokcancel('错误提示', '用户名或者密码错误请重新输入')

if __name__=='__main__':
    ui_process()