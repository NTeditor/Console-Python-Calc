import lang
import sys
import os

def xay1():
    clear()
    print(lang.welcome)
    print(" ")
    x = input(lang.xx)
    y = input(lang.yy)
    try:
        print(int(x) + int(y))
    except ValueError:
        print(lang.errormode01)

def xay2():
    clear()
    print(lang.welcome)
    print(" ")
    x = input(lang.xx)
    y = input(lang.yy)
    try:
        print(int(x) - int(y))
    except ValueError:
        print(lang.errormode01)

def xay3():
    clear()
    print(lang.welcome)
    print(" ")
    x = input(lang.xx)
    y = input(lang.yy)
    print(int(x) * int(y))

def xay4():
    clear()
    print(lang.welcome)
    print(" ")
    x = input(lang.xx)
    y = input(lang.yy)
    try:
        print(int(x) / int(y))
    except ValueError:
        print(lang.errormode01)
    
def xay5():
    clear()
    print(lang.welcome)
    print(" ")
    x = input(lang.xx)
    y = input(lang.yy)
    try:
        if int(x) > 100:
            print("")
            print(lang.overflowX)
            usercontinue = input("Проигнорировать предупрежденние? Y/N ")
            if usercontinue == "Y":
                print(int(x) ** int(y))
            else:
                clear()
    except ValueError:
        print(lang.errormode01)
    except MemoryError:
        print(overflow)
        input()
    
    else:
        if int(y) > 100:
                print("")
                print(lang.overflowY)
                usercontinue = input("Проигнорировать предупрежденние? Y/N ")
                if usercontinue == "Y":
                    print(int(x) ** int(y))
        else:
            print(int(x) ** int(y))
        

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def stop():
    print(" ")
    print(" ")
    print(lang.stoptext01)
    print(lang.stoptext02)
    try:
        stop = input(lang.stoptext03)
    except KeyboardInterrupt:
        sys.exit()
    if stop == "exit":
        sys.exit()
    else:
        clear()
