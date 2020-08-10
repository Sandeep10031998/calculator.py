from tkinter import*
win = Tk()
#Line1
def fun7():
    num1=num.get()
    num.set(num1+"7")
def fun8():
    num1=num.get()
    num.set(num1+"8")
def fun9():
    num1=um.get()
    num.set(num1+"9")
def funadd():
    num1=num.get()
    num.set(num1+"+")

##Line2

def fun4():
    num1=num.get()
    num.set(num1+"4")
def fun5():
    num1=num.get()
    num.set(num1+"5")
def fun6():
    num1=num.get()
    num.set(num1+"6")
def funsub():
    num1=num.get()
    num.set(num1+"-")

##Line3

def fun1():
    num1=num.get()
    num.set(num1+"1")
def fun2():
    num1=num.get()
    num.set(num1+"2")
def fun3():
    num1=num.get()
    num.set(num1+"3")
def funmul():
    num1=num.get()
    num.set(num1+"*")

#Line4
def fun0():
    num1=num.get()
    num.set(num1+"0")
def func():
    num.set("")
def funequal():
    num1=num.get()
    
    num.set(eval(num1))
def fundiv():
    num1=num.get()
    num.set(num1+"/")

#Line4
    
num = StringVar()
tb = Entry(win,textvariable=num,font="Vendata 20 bold italic ",relief = SUNKEN,bg="pink",bd=10,justify=RIGHT)
tb.grid(columnspan=4)
b1 = Button(win,text=7,font="Vendata 10 bold italic ",width="8",height="2",relief=RAISED,bd=5,command=fun7)
b1.grid(row = 1,column=0,sticky=W)
b2 = Button(win,text=8,font="Vendata 10 bold italic ",width="8",height="2",relief=RAISED,bd=5,command=fun8)
b2.grid(row = 1,column=1)
b3 = Button(win,text=9,font="Vendata 10 bold italic ",width="8",height="2",relief=RAISED,bd=5,command=fun9)
b3.grid(row = 1,column=2)
b4 = Button(win,text='+',font="Vendata 10 bold italic ",width="8",height="2",relief=RAISED,bd=5,command=funadd)
b4.grid(row = 1,column=3)

#Line5


b5 = Button(win,text=4,font="Vendata 10 bold italic ",width="8",height="2",relief=RAISED,bd=5,command=fun4)
b5.grid(row = 2,column=0)
b6 = Button(win,text=5,font="Vendata 10 bold italic ",width="8",height="2",relief=RAISED,bd=5,command=fun5)
b6.grid(row = 2,column=1)
b7 = Button(win,text=6,font="Vendata 10 bold italic ",width="8",height="2",relief=RAISED,bd=5,command=fun6)
b7.grid(row = 2,column=2)
b8 = Button(win,text='-',font="Vendata 10 bold italic ",width="8",height="2",relief=RAISED,bd=5,command=funsub)
b8.grid(row = 2,column=3)

#
b9 = Button(win,text=1,font="Vendata 10 bold italic ",width="8",height="2",relief=RAISED,bd=5,command=fun1)
b9.grid(row = 3,column=0,sticky=W)
b10 = Button(win,text=2,font="Vendata 10 bold italic ",width="8",height="2",relief=RAISED,bd=5,command=fun2)
b10.grid(row = 3,column=1,sticky=W)
b11 = Button(win,text=3,font="Vendata 10 bold italic ",width="8",height="2",relief=RAISED,bd=5,command=fun3)
b11.grid(row = 3,column=2,sticky=W)
b12 = Button(win,text='x',font="Vendata 10 bold italic ",width="8",height="2",relief=RAISED,bd=5,command=funmul)
b12.grid(row = 3,column=3,sticky=W)

#LIne6

b13 = Button(win,text=0,font="Vendata 10 bold italic ",width="8",height="2",relief=RAISED,bd=5,command=fun0)
b13.grid(row = 4,column=0,sticky=W)
b14 = Button(win,text='c',font="Vendata 10 bold italic ",width="8",height="2",relief=RAISED,bd=5,command=func)
b14.grid(row = 4,column=1,sticky=W)
b15 = Button(win,text='=',font="Vendata 10 bold italic ",width="8",height="2",relief=RAISED,bd=5,command=funequal)
b15.grid(row = 4,column=2,sticky=W)
b16 = Button(win,text='/',font="Vendata 10 bold italic ",width="8",height="2",relief=RAISED,bd=5,command=fundiv)
b16.grid(row = 4,column=3,sticky=W)

