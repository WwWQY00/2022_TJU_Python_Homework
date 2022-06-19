from turtle import *
from datetime import *
from math import *
def drawGap(): #每段线间的空隙
    pu()
    fd(2)
def drawLine(draw): #画出一段线
    begin_fill() if draw else None
    drawGap()
    pd()
    lt(45)
    fd(sqrt(18))
    rt(45)
    fd(34)
    rt(45)
    fd(sqrt(18))
    rt(90)
    fd(sqrt(18))
    rt(45)
    fd(34)
    rt(45)
    fd(sqrt(18))
    end_fill() if draw else None
    rt(135)
    pu()
    fd(40)
    drawGap()
    rt(90)
def drawDigit(d): #根据所显示数字需要用到线的位置，来处理七段线的显示
    drawLine(True) if d in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,6,8] else drawLine(False)
    lt(90)
    drawLine(True) if d in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,2,3,4,7,8,9] else drawLine(False)
    lt(180)
    pu()
    fd(20)
def drawDate(date): #写出年月日
    pencolor("red")
    fillcolor("red")
    for i in date:
        if i == '年':
            write('年',font=("Arial", 18, "normal"))
            pencolor("green")
            fillcolor("green")
            fd(40)
        elif i == '月':
            write('月',font=("Arial", 18, "normal"))
            pencolor("blue")
            fillcolor("blue")
            fd(40)
        elif i == '日':
            write('日',font=("Arial", 18, "normal"))
            fd(40)
        else:
            drawDigit(eval(i))
def displayInputdate(): #显示输入的日期
    try:
        date = input("请输入日期，如“2019年2月22日”：\n")
        setup(800, 350, 200, 200)
        pu()
        fd(-350)
        pensize(1)
        drawDate(date)
    except NameError:
        print("请按格式输入日期")
        return 0
    hideturtle()
    exitonclick()
def displayDate(): #显示当前日期
    setup(800, 350, 200, 200)
    pu()
    fd(-350)
    pensize(1)
    drawDate(datetime.now().strftime('%Y年%m月%d日'))
    hideturtle()
    exitonclick()
def displayInt(): #显示一串数字
        try:
            Int=eval(input("请输入一串整数：\n"))
            strInt=str(Int)
            for i in strInt:
                drawDigit(eval(i))
            exitonclick()
        except NameError:
            print("输入错误，请输入一个整数！\n")
def main():
    displayInputdate()
    displayDate()
    displayInt()
if __name__ == "__main__":
    main()