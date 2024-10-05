import lang
import defcmd
import sys
import os

def xay():
    x = input(lang.xx)
    y = input(lang.yy)

while True:
    print(lang.welcome)
    print(" ")
    print(lang.mode02)
    print(lang.mode03)
    print(lang.mode04)
    print(lang.mode05)
    print(lang.mode06)

    mode = input(lang.mode01)

    if mode == "+":
        defcmd.xay1()
        
    else:
        if mode == "-":
            defcmd.xay2()

        else:
            if mode == "*":
                defcmd.xay3()

            else:
                if mode == "/":
                    defcmd.xay4()

                else:
                    if mode == "~":
                        defcmd.xay5()

                    else:
                        print(lang.errormode01)
                        print(lang.error01)
                        print(lang.error02)
                        try:
                            userexit = input()
                        except KeyboardInterrupt:
                            sys.exit()
                        if str(userexit) == "exit":
                            sys.exit()
                        else:
                            defcmd.clear()

    
    defcmd.stop()
                            
                        
                            
                    
