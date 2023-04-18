##!/usr/bin/env python3
# -*- coding: UTF-8 -*-


# /utils/
# from utils.modules import *
from utils.constants import RED, WHITE, PURPLE
from utils.general import printScreen

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
        
    # RSACTFTool
    # feather duster
    # XOR tool
    elif choice == "1": cryscan() # RSACTFTool
    elif choice == "2": vigenere() # feather duster
    elif choice == "3": caesar() # XOR tool
    elif choice == "4": hashcat()
    elif choice == "5": john()
    elif choice == "6": cryptool()
    elif choice == "7": an_important_link() # this is something, will be updated
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


if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print(f"{RED} Terminating ..!!! {WHITE}")
        time.sleep(1)


        