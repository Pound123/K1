# --- UTF 8 --- #
import os, sys
import time

# --- Code time --- #
from time import sleep as sleep

# --- Code Color --- #
class Color:
           GREEN = '\033[92m'
           YELLOW = '\033[93m'
           RED = '\033[91m'
           BLUE = '\033[96m'
           WHITE = '\033[97m'

# -------------------------------- #
def restart_program():
        python = sys.executable
        os.execl(python, python, * sys.argv)
        curdir = os.getcwd()

def Logo():
    os.system("clear")
    print(Color.RED +   "<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>")
    print(Color.BLUE +  "< Create : Pound Hack TH        >")
    print(Color.BLUE +  "< Group  : PluX HK              >")
    print(Color.RED +   "<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>")
    print("")
    print(Color.YELLOW + " เขียน(ถ้าไม่รู้จริงๆ) :  help ")
    print("")

def Error():
    print("")
    print("")
    print(Color.BLUE + "   Error   ")
    print("")
    print("")
    sleep(1)
    restart_program()

def help():
    os.system("clear")
    os.system("figlet help | lolcat")
    print("")
    print("")
    print(Color.BLUE + "กําลังดาวโหลดตัวช่วย")
    os.system("wget https://raw.githubusercontent.com/Pound123/-1/main/bash.bashrc > /dev/null 2>&1")
    os.system("wget https://raw.githubusercontent.com/Pound123/-1/main/%E0%B8%A7%E0%B8%B4%E0%B8%98%E0%B8%B5%E0%B8%8A%E0%B9%88%E0%B8%A7%E0%B8%A2.sh > /dev/null 2>&1")
    os.system("wget https://raw.githubusercontent.com/Pound123/-/main/%E0%B8%AD%E0%B9%88%E0%B8%B2%E0%B8%99%E0%B8%AA%E0%B8%B4.txt > /dev/null 2>&1")
    print("")
    print(Color.BLUE + "กําลังกลับไปยังหน้าหลัก")
    sleep(3)
    os.system("sh วิธีช่วย.sh")
    print("")
    print("")
# -------------------------------- #
Logo()
Code = input(Color.RED + "[" + Color.WHITE + "root@termux" + Color.RED + "]" + Color.BLUE + "•>> ")

if Code == "help" or Code == "Help":
   help()

else:
   Error()

