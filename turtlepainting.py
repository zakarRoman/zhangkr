# 部门:人工智能
# 编写人:张开然
# 开发日期: 2023/1/13
# !/usr/bin/python
# -*- coding: UTF-8 -*-
import turtle
from turtle import *
from tkinter import *
from turtle import Terminator
import random

def heart(num):
    try:
        # 创建画笔
        tt = turtle.Turtle()
        bgcolor("wheat")
        tt.pensize(12)
        tt.color("pink")
        tt.fillcolor("lightcoral")
        for i in range(num):
            tt.penup()
            tt.goto(random.randint(1, 400), random.randint(1, 400))
            tt.pendown()
            tt.begin_fill()
            tt.left(45)
            tt.forward(100)
            tt.circle(50, 180)
            tt.right(90)
            tt.circle(50, 180)
            tt.forward(100)
            tt.left(45)
            tt.end_fill()
            tt.hideturtle()
        turtle.done()
    except Terminator:
        heart(num)

def flower(num):
    try:
        tt=turtle.Turtle()
        bgcolor("skyblue")
        for i in range(num):
            tt.penup()
            tt.goto(random.randint(1, 400), random.randint(1, 400))
            tt.color("yellow")
            tt.fillcolor("gold")
            tt.pendown()
            tt.begin_fill()
            tt.circle(8)
            tt.end_fill()
            for j in range(6):
                tt.right(120)
                tt.color('white')
                tt.begin_fill()
                tt.circle(20, 90)
                tt.left(110)
                tt.forward(5)
                tt.right(110)
                tt.forward(5)
                tt.left(90)
                tt.circle(20,90)
                tt.end_fill()
                tt.right(90)
            tt.hideturtle()
        turtle.done()
    except Terminator:
        flower(num)
def star(num):
    try:
        app.clearBox()
        tt = turtle.Turtle()
        bgcolor("darkblue")
        tt.color("yellow")
        for i in range(num):
            tt.penup()
            tt.goto(random.randint(1, 400), random.randint(1, 400))
            tt.pendown()
            for j in range(5):
                tt.begin_fill()
                tt.right(30)
                tt.forward(30)
                tt.left(30)
                tt.forward(30)
                tt.left(150)
                tt.forward(30)
                tt.left(30)
                tt.forward(30)
                tt.end_fill()
                tt.right(32)
            tt.hideturtle()
        turtle.done()
    except Terminator:
        star(num)






class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.lab1 = Label(root, text="欢迎来到海龟画图", font=("黑体", 20, "bold"), background="steelblue")
        self.lab1.pack()

        self.lab2 = Label(root, text="在输入框中输入要画的图形数", font=("黑体", 10, "bold")).pack()

        v1 = StringVar()
        self.entry01 = Entry(self, textvariable=v1)
        self.entry01.pack(side='top', anchor='ne')


        self.btn01 = Button(self, text='爱心', activebackground="wheat", activeforeground="pink", command=lambda: heart(int(self.entry01.get())))
        self.btn01.pack()
        self.btn02 = Button(root, text="花朵", activeforeground="salmon", activebackground="pink", command=lambda: flower(int(self.entry01.get())))
        self.btn02.pack()
        self.btn03 = Button(root, text="星星", activeforeground="gold", activebackground="darkblue", command=lambda: star(int(self.entry01.get())))
        self.btn03.pack()

    def clearBox(self):  # 建一个删除函数，t是文本框的名字，每个人的命名不一样
        self.entry01.delete("0", "end")


root = Tk()
root.geometry("300x175")
root.geometry("+500+100")
root.config(bg="lavender")
app = Application(master=root)
root.mainloop()