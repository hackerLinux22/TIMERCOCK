import time
from colorama import Fore,Style


def timercock(t):
    
    while(t>=0):
        mins,secs=divmod(t,60)

        hrs,mins=divmod(mins,60)

        timer='{:02d} : {:02d} :{:02d}'.format(hrs,mins,secs)

        print(Fore.GREEN,Style.BRIGHT,timer, end="\r")
        time.sleep(1)
        t-=1

    print(Fore.RED,'\nStop timer')
print(Fore.MAGENTA,Style.BRIGHT,"Enter the time in seconds ~$",end=" ")
t=input()

timercock(int(t))
