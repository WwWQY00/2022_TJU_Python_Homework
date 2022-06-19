import re

def findError():
    f = open('pachong.py', encoding='utf-8')
    strdata = f.readline()
    i = 1
    error = 0
    while strdata:
        if "for" in strdata:
            matchObj = re.match('^(\s*)(.*)(for)(\s*)(.*?)(\s*)(in)(\s*)(.*?)[:]$', strdata)
            if matchObj == None:
                print("第",i,"行有错误")
                error += 1
        if "def" in strdata:
            matchObj = re.match('^(\s*)(.*)(def)(\s*)[(](.*?)[)][:]$', strdata)
            if matchObj == None:
                print("第",i,"行有错误")
                error += 1
        if "try" in strdata:
            matchObj = re.match('^(\s*)(.*)(try)(.*?)[:]$', strdata)
            if matchObj == None:
                print("第",i,"行有错误")
                error += 1
            while strdata:
                if "except" in strdata:
                    matchObj = re.match('^(\s*)(.*)(except)(.*?)[:]$', strdata)
                    if matchObj == None:
                        print("第",i,"行有错误")
                        error += 1
                    break
                i=i+1
                strdata = f.readline()
        i=i+1
        strdata = f.readline()
    return error

def showResult(error):
        print("程序有",error,"处错误")

def main():
    error = findError()
    showResult(error)

if __name__ == "__main__":
    main()
