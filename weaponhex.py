##!/usr/bin/env python3
# -*- coding: UTF-8 -*-


# /utils/
from utils.modules import *
from utils.constants import *
from utils.general import clearScreen, printScreen

# /src/
from src.reverse_tools import *
from src.pwning_tools import *
from src.forensic_tools import *
from src.crypto_tools import *
from src.web_tools import *
from src.osint_tools import *


def menu():
    print(BANNER)
    print(MENU)

    choice = input(f"{PURPLE} [+] Enter your choice  =>> {WHITE}").strip()
    printScreen()

    if choice not in ["1", "2", "3", "4", "5", "6", "99"]:
        print(f"{RED} [-] '{choice}' is an invalid input {WHITE}")
        time.sleep(2)
        menu()

    elif choice == "1": reverse()

    elif choice == "2": pwning()

    elif choice == "3": forensic()

    elif choice == "4": crypto()  

    elif choice == "5": web()

    elif choice == "6": osint()

    elif choice == "99": Exit()


def reverse():
    print(REVERSE_MENU)

    choice = input(f"{PURPLE} [+] Enter your choice  =>> {WHITE}").strip()
    printScreen()
    
    if choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "0", "99"]:
        print(f"{RED} [-] '{choice}' is an invalid input {WHITE}")
        time.sleep(2)
        menu()

    elif choice == "1": rscan()

    elif choice == "2": bninja()

    elif choice == "3": ghidr()

    elif choice == "4": IDA()

    elif choice == "5": uncompyle6()

    elif choice == "6": gdb()

    elif choice == "7": radare2()

    elif choice == "8": apktool()

    elif choice == "99": Exit()

    elif choice == "0": menu()


def pwning():
    print(PWNING_MENU)
    
    choice = input(f"{PURPLE} [+] Enter your choice  =>> {WHITE}").strip()
    printScreen()
    
    if choice not in ["1", "2", "3", "4", "5", "6", "7", "0", "99"]:
        print(f"{RED} [-] '{choice}' is an invalid input {WHITE}")
        time.sleep(2)
        menu()

    elif choice == "1": pwnscan()

    elif choice == "2": pwn_tools()

    elif choice == "3": pwndbg()

    elif choice == "4": IPython()

    elif choice == "5": welpwn()

    elif choice == "6": glibc()

    elif choice == "7": an_important_link()

    elif choice == "99": Exit()

    elif choice == "0": menu()


def forensic():
    print(FORENSIC_MENU)

    choice = input(f"{PURPLE} [+] Enter your choice  =>> {WHITE}").strip()
    printScreen()
    
    if choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "0", "99"]:
        print(f"{RED} [-] '{choice}' is an invalid input {WHITE}")
        time.sleep(2)
        menu()

    elif choice == "1": forenscan()

    elif choice == "2": hexedit()

    elif choice == "3": binwalk()

    elif choice == "4": exiftool()

    elif choice == "5": steg_tools()

    elif chioce == "6": PNGcheck()

    elif choice == "7": PDFparser()

    elif choice == "8": autospy()

    elif choice == "99": Exit()

    elif choice == "0": menu()


def crypto():
    print(CRYPTO_MENU)

    choice = input(f"{PURPLE} [+] Enter your choice  =>> {WHITE}").strip()
    printScreen()
    
    if choice not in ["1", "2", "3", "4", "5", "6", "7", "0", "99"]:
        print(f"{RED} [-] '{choice}' is an invalid input {WHITE}")
        time.sleep(2)
        menu()

    elif choice == "1": cryscan() # RSACTFTool

    elif choice == "2": vigenere() # feather duster

    elif choice == "3": caesar() # XOR tool

    elif choice == "4": hashcat()

    elif choice == "5": john()

    elif choice == "6": cryptool()

    elif choice == "7": an_important_link()

    elif choice == "99": Exit()

    elif choice == "0": menu()


def web():
    print(WEB_MENU)
    
    choice = input(f"{PURPLE} [+] Enter your choice  =>> {WHITE}").strip()
    printScreen()
    
    if choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "0", "99"]:
        print(f"{RED} [-] '{choice}' is an invalid input {WHITE}")
        time.sleep(2)
        menu()

    elif choice == "1": burpsuit()

    elif choice == "2": wireshark()

    elif choice == "3": sqlmap()

    elif choice == "4": dsniff()

    elif choice == "5": subbrute()

    elif choice == "6": gobuster()

    elif choice == "7": w3af()

    elif choice == "8": AXSSer()

    elif choice == "99": Exit()

    elif choice == "0": menu()


def osint():
    print(OSINT_MENU)

    choice = input(f"{PURPLE} [+] Enter your choice  =>> {WHITE}").strip()
    printScreen()
    
    if choice not in ["1", "2", "3", "0", "99"]:
        print(f"{RED} [-] '{choice}' is an invalid input {WHITE}")
        time.sleep(2)
        menu()

    elif choice == "1": social_scan()

    elif choice == "2": data_sploit()

    elif choice == "3": recon_spider()

    elif choice == "99": Exit()

    elif choice == "0": menu()


# ============================== MENU ENDS HERE ==============================



def soscan():
    print("\033[32mSocial Scan Tool is a tool which scans username on most of the popular social media websites.")
    usname = input("\033[35mEnter username =>>\033[32m")
    os.system("./socialscan.sh " + usname + " -fu")
    
def dtsploit():
    print("An OSINT framework to perform various recon techniques on Companies, People, Phone, Number, \nBitcoin Addresses, etc aggregate all the raw data, and give data in multiple formats.")
    print("""
        \033[32m[1]   \033[36mInstall
        \033[32m[99]  \033[36mBack
        """)
    dtchoice = input("\033[35mEnter your choice =>>\033[32m")
    if dtchoice == "1":
        os.system("sudo git clone https://github.com/DataSploit/datasploit.git")
        os.system("cd datasploit && pip install --upgrade --force-reinstall -r requirements.txt")
        print("\033[32m[+]  \033[33mDataSploit Installed Successfully.")
    elif dtchoice == "99":
        osint()
    else:
        menu()
        
def reconspider():
    print("ReconSpider is most Advanced Open Source Intelligence (OSINT) Framework for scanning IP Address, \nEmails, Websites, Organizations and find out information from different sources.")
    print("""
        \033[32m[1]   \033[36mInstall
        \033[32m[2]   \033[36mRun
        \033[32m[99]  \033[36mBack
        """)
    rspidchoice = input("\033[35mEnter your choice =>>\033[32m")
    if rspidchoice == "1":
        os.system("sudo git clone https://github.com/bhavsec/reconspider.git")
        os.system("sudo apt install python3 python3-pip && cd reconspider && sudo python3 setup.py install")
        print("\033[32m[+]  \033[33mReconSpider Installed Successfully.")
    elif rspidchoice == "2":
        os.system("cd reconspider && python3 reconspider.py")
    elif rspidchoice == "99":
        osint()
    else :
        menu()
    

if __name__ == "__main__":
    try:
        if system() == 'Linux':
            if path.exists("/home/"):
                os.chdir("/home/groot/Desktop")
                if os.path.isdir('WeaponHEX'):
                    os.chdir("/home/groot/Desktop/WeaponHEX/")
                    menu()
                else :
                    os.system("mkdir WeaponHEX")
                    os.chdir("/home/groot/Desktop/WeaponHEX/")
                    menu()
        elif path.exists('/data'):
            os.chdir("data/data/com.termux/files/home/")
            if os.path.isdir('WeaponHEX'):
                os.chdir("data/data/com.termux/files/home/WeaponHEX/")
                menu()
            else :
                os.system("mkdir WeaponHEXstore")
                os.chdir("data/data/com.termux/files/home/WeaponHEX/")
                menu()
    except KeyboardInterrupt:
        print(" Terminating ..!!!")
        time.sleep(1)


        