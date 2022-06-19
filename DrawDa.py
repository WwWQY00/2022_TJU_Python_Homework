from operator import lt
import turtle
import time

def drawDa(size): #控制画笔画出“大”字
    turtle.lt(40)
    turtle.fd(size)
    turtle.pu()
    turtle.lt(90)
    turtle.circle(size/2, 90)
    turtle.lt(90)
    turtle.pd()
    turtle.fd(size/2)
    turtle.circle(-size/2, 90)
    turtle.pu()
    turtle.lt(180)
    turtle.circle(size/2, 90)
    turtle.lt(180)
    turtle.pd()
    turtle.circle(size/2,90)

def displayProgrambar(): #添加进度条
    scale = 50
    print("执行开始".center(25,'-'))
    start = time.perf_counter()
    for i in range(scale+1):
        a = '*'* i
        b = '.' * (scale - i)
        c = (i/scale)*100
        t = time.perf_counter() - start
        print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,t),end = "")
        time.sleep(0.05)
    print("\n"+"执行结束".center(scale//2,'-'))

def main():
    displayProgrambar()
    turtle.setup(1300, 800, 0, 0)
    pythonsize = 15
    turtle.pensize(pythonsize)
    turtle.pencolor("blue")
    turtle.seth(-40)
    drawDa(200)
if __name__ == "__main__":
    main()