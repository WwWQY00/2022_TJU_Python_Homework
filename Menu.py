import Hash
import DrawDa
import DrawSevenSegDisplay
import CalReservedWord
import debug
import pachong
def displayMenu(): #设定主菜单
    try:
        S=eval(input("如要显示Hash函数实例，请输入“1”\n如要显示turtle绘图演示，请输入“2”\n如要显示七段数码管，请输入“3”\n如要显示计算程序保留字，请输入“4”\n如要显示语法编译器，请输入“5”\n如要显示网络爬虫程序，请输入“6”\n如要退出程序，请输入“7”：\n"))
    except NameError:
        print("请输入一个整数")
        displayMenu()
        if S == 1:
            Hash.main()
            displayMenu()
        elif S == 2:
            DrawDa.main()
            displayMenu()
        elif S == 3:
            displaySubmenu()
        elif S == 4:
            CalReservedWord.main()
        elif S == 5:
            debug.main()
        elif S == 6:
            pachong.main()
        elif S == 7:
            return 0
        else:
            print("请输入提供的选项")
            displayMenu()
def displaySubmenu(): #设定子菜单
    try:
        T=eval(input("如要显示输入时间，请输入“1”\n如要显示系统时间，请输入“2”\n如要显示任意数字，请输入“3”\n如要返回上级菜单，请输入“4”：\n"))
    except NameError:
        print("请输入一个整数")
        displaySubmenu()
    if T == 1:
        DrawSevenSegDisplay.displayInputdate()
        displaySubmenu()
    elif T == 2:
        DrawSevenSegDisplay.displayDate()
        displaySubmenu()
    elif T == 3:
        DrawSevenSegDisplay.displayInt()
        displaySubmenu()
    elif T == 4:
        displayMenu()
    else:
        print("请输入提供的选项")
        displaySubmenu()
def main():
    displayMenu()
main()
